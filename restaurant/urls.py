from django.urls import path
from . import views
from .views import CustomLoginView, CustomLogoutView
from django.contrib.auth.views import LogoutView
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.home, name='home'),  # Главная страница

    # Страница меню
    path('menu/', views.menu, name='menu'),

    # Гостевая книга
    path('gallery/', views.gallery, name='gallery'),

    # Контакты
    path('contacts/', views.contacts, name='contacts'),

    # Бронирование
    path('reservation/', views.reserve_table, name='reservation'),

    # Отправка отзыва
    path('submit-review/', views.submit_review, name='submit_review'),

    # Страница логина с кастомным представлением
    path('login/', CustomLoginView.as_view(), name='login'),  # Логин с кастомным представлением

    # Страница выхода
    path('logout/', CustomLogoutView.as_view(), name='logout'),  # Выход

    # Страница регистрации
    path('registration/', views.registration_view, name='registration'),  # Регистрация
    path('logout/', LogoutView.as_view(), name='logout'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('profile/', views.profile, name='profile'),
]
