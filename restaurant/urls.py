from django.urls import path
from . import views
from .views import home, menu

urlpatterns = [
    path('', views.home, name='home'),
    path('menu/', views.menu, name='menu'),
    path('gallery/', views.gallery, name='gallery'),
    path('contacts/', views.contacts, name='contacts'),
    path('reservation/', views.reserve_table, name='reservation'),
    path('submit-review/', views.submit_review, name='submit_review'),
    
]