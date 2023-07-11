from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings 


urlpatterns=[
path('homearticle',views.homearticle,name='homearticle'),
path(r'^contentpage/(?P<title>\w+))/$', views.contentpage, name = 'contentpage'),
path('myblog',views.myblog,name='myblog'),
path('create',views.create,name='create'),
path('search',views.search,name='search'),
]+static(settings.STATIC_URL,document_root=settings.STATIC_ROOT)
