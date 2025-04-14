from django.urls import path
from . import views
from .views import CustomLoginView, CustomLogoutView
from django.contrib.auth.views import LogoutView
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.home, name='home'),  # Home Page

    # Menu page
    path('menu/', views.menu, name='menu'),

    # Guestbook
    path('gallery/', views.gallery, name='gallery'),

    # Contacts
    path('contacts/', views.contacts, name='contacts'),

    # Reservations
    path('reservation/', views.reserve_table, name='reservation'),

    # Sending feedback
    path('submit-review/', views.submit_review, name='submit_review'),

    # Login page with custom view
    path('login/', CustomLoginView.as_view(), name='login'),  # Login with custom representation

    # Exit page
    path('logout/', CustomLogoutView.as_view(), name='logout'),  # Выход

    # Registration page
    path('registration/', views.registration_view, name='registration'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('profile/', views.profile, name='profile'),
]
