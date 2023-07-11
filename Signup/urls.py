from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings 


urlpatterns=[
path('',views.home,name='home'),
path('home',views.home,name='home'),
path('signup',views.signup,name='signup'),    
path('login',views.login,name='login'), 
]+static(settings.STATIC_URL,document_root=settings.STATIC_ROOT)
