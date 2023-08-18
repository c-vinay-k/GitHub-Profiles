import requests
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic
from django.http import HttpResponse, Http404
from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate
from .forms import SignUpForm
from .models import Profile
from django.shortcuts import render, redirect
# Create your views here.

#class SignUpView(generic.CreateView):
 #   form_class = UserCreationForm
  #  success_url = reverse_lazy('login')
   # template_name = 'registration/signup.html'


def home_view(request):
    return render(request, 'home.html')


def signup_view(request):
    if request.method=='POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            user.refresh_from_db()
        #    user.profile.first_name = form.cleaned_data.get('first_name')
        #    user.profile.last_name = form.cleaned_data.get('last_name')
            #changes
            response=requests.get(f'https://api.github.com/users/{user.username}')
            jsonformat=response.json()
            user.profile.followers=jsonformat['followers']
            user.profile.save()
        #    user.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=password)
            login(request, user)
            return redirect('home')
    else:
        form = SignUpForm()
    return render(request, 'registration/signup.html', {'form': form})


#def user_view(request):
 #   username = None
  #  first_name = None
   # last_name = None
    #if request.user.is_authenticated():
     #   username = request.user.username
      #  first_name = request.user.first_name
       # last_name = request.user.last_name

def prof(request):
    try:
        userf = User.objects.get(username=request.user.username)
    except:
        raise Http404('Requested User not found')
    response = requests.get(f'https://api.github.com/users/{request.user.username}')
    jsonformat = response.json()
    request.user.profile.followers = jsonformat['followers']
    print(request.user.profile.followers)
    return render(request , 'myprofile.html')

def explore(request,username):
    try:
        user = User.objects.get(username=username)
    except:
        raise Http404('Requested User not found')

#    results=Profile.objects.all().filter(request.first_name)
#    print(results)
#     data = Profile.objects.all()
#     prof = {
#         "first_name" : data
 #    }
  #   return render('explore.html',prof)






