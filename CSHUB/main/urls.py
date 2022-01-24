from django.urls import path
from . import views
# from .views import home
# from ..artGallery import settings

urlpatterns = [
    path('', views.home, name='home'),
    path('signup/', views.signup, name='signup'),
    path('signin/', views.signin, name='signin'),
    path('logout/', views.logout, name='logout'),
    path('addPage/', views.addPage, name='addPage'),
    path('add/', views.add, name='add'),
    path('searchResults/', views.searchResults, name='searchResults'),
]