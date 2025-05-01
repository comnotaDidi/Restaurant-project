from django.shortcuts import redirect
from django.views.generic import TemplateView, FormView, CreateView
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib import messages
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_protect
from .forms import ReservationForm, ReviewForm, LoginForm

# Home Page
class HomeView(TemplateView):
    template_name = 'restaurant/home.html'

# Menu Page
class MenuView(TemplateView):
    template_name = 'restaurant/menu.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['food'] = [
            # same food list as before...
        ]
        context['desserts'] = [
            # same desserts list as before...
        ]
        context['cocktails'] = [
            # same cocktails list as before...
        ]
        return context

# Gallery Page
class GalleryView(TemplateView):
    template_name = 'restaurant/gallery.html'

# Contacts Page
class ContactsView(TemplateView):
    template_name = 'restaurant/contacts.html'

# Reservation Page
class ReservationPageView(TemplateView):
    template_name = 'restaurant/reservation.html'

# Reserve Table (Form Submission)
class ReserveTableView(FormView):
    template_name = 'restaurant/reservation.html'
    form_class = ReservationForm
    success_url = reverse_lazy('reservation')

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)

# Submit Review
class SubmitReviewView(FormView):
    template_name = 'restaurant/review_form.html'
    form_class = ReviewForm
    success_url = reverse_lazy('review_thanks')

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)

# Review Thanks Page
class ReviewThanksView(TemplateView):
    template_name = 'restaurant/review_thanks.html'

# Custom Login View
class CustomLoginView(LoginView):
    template_name = 'restaurant/login.html'
    authentication_form = LoginForm

    def get_success_url(self):
        return reverse_lazy('home')

# Custom Logout View
class CustomLogoutView(LogoutView):
    next_page = reverse_lazy('login')

# Registration View
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

# Profile Page
class ProfileView(TemplateView):
    template_name = 'profile.html'
