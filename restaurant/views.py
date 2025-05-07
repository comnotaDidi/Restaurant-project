from django.shortcuts import redirect
from django.views.generic import TemplateView, FormView
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib import messages
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_protect

from .forms import ReservationForm, ReviewForm, LoginForm
from .models import MenuItem

# Главная страница
class HomeView(TemplateView):
    template_name = 'restaurant/home.html'

# Страница меню — теперь загружает данные из базы
class MenuView(TemplateView):
    template_name = 'restaurant/menu.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        # Используем filter вместо get, чтобы избежать ошибки DoesNotExist
        food_category = MenuItem.objects.filter(category__name='food')
        dessert_category = MenuItem.objects.filter(category__name='dessert')
        cocktail_category = MenuItem.objects.filter(category__name='cocktail')

        context['food'] = food_category
        context['desserts'] = dessert_category
        context['cocktails'] = cocktail_category
        
        return context

# Галерея
class GalleryView(TemplateView):
    template_name = 'restaurant/gallery.html'

# Контакты
class ContactsView(TemplateView):
    template_name = 'restaurant/contacts.html'

# Страница бронирования
class ReservationPageView(TemplateView):
    template_name = 'restaurant/reservation.html'

# Отправка формы бронирования
class ReserveTableView(FormView):
    template_name = 'restaurant/reservation.html'
    form_class = ReservationForm
    success_url = reverse_lazy('reservation')

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)

# Отправка отзыва
class SubmitReviewView(FormView):
    template_name = 'restaurant/review_form.html'
    form_class = ReviewForm
    success_url = reverse_lazy('review_thanks')

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)

# Страница благодарности за отзыв
class ReviewThanksView(TemplateView):
    template_name = 'restaurant/review_thanks.html'

# Вход
class CustomLoginView(LoginView):
    template_name = 'restaurant/login.html'
    authentication_form = AuthenticationForm

# Выход
class CustomLogoutView(LogoutView):
    next_page = reverse_lazy('login')

# Регистрация
@method_decorator(csrf_protect, name='dispatch')
class RegistrationView(FormView):
    template_name = 'restaurant/registration.html'
    form_class = UserCreationForm
    success_url = reverse_lazy('login')

    def form_valid(self, form):
        form.save()
        messages.success(self.request, 'Регистрация прошла успешно! Теперь вы можете войти.')
        return super().form_valid(form)

    def form_invalid(self, form):
        messages.error(self.request, "Ошибка регистрации. Пожалуйста, попробуйте еще раз.")
        return super().form_invalid(form)

# Профиль пользователя
class ProfileView(TemplateView):
    template_name = 'profile.html'
