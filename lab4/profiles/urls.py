from django.urls import path
from .views import signup_view
from . import views
from django.views.generic.base import TemplateView

urlpatterns = [
        path('signup/',signup_view, name='signup'),
        path('profile/',TemplateView.as_view(template_name='myprofile.html'),name='myprofile'),
        path('explore',views.explore,name='explore'),
]  
