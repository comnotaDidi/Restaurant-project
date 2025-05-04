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
from django.views.generic import TemplateView

class MenuView(TemplateView):
    template_name = 'restaurant/menu.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context['food'] = [
            {"name": "Kawior Antonius", "description": "kawior Antonius, crème fraîche, bliny, złoto", "price": "350 PLN"},
            {"name": "Sushi Bites", "description": "ryż do sushi, tuńczyk błękitnopłetwy, łosoś, seriola, dodatki", "price": "72 PLN"},
            {"name": "Tartaletka z tuńczykiem", "description": "tuńczyk błękitnopłetwy, emulsja nori, kawior", "price": "88 PLN"},
            {"name": "Ostryga Gillardeau / 1 szt.", "description": "ostryga, imbir, zielone jabłko, kawior limonkowy", "price": "42 PLN"},
            {"name": "Bubu arare", "description": "brokuły, krem z awokado, perły ryżowe", "price": "48 PLN"},
            {"name": "Tsukemono", "description": "ogórek, sezam", "price": "18 PLN"},
            {"name": "Tatar wołowy", "description": "wołowina black angus, domowy tost, kapary, marynowane szalotki", "price": "84 PLN"},
            {"name": "Tuna tataki", "description": "tuńczyk błękitnopłetwy, awokado, ogórek, imbir, yuzu", "price": "92 PLN"},
            {"name": "Tuna toro & crispy rice", "description": "tuńczyk błękitnopłetwy, ryż, aioli z pora", "price": "82 PLN"},
            {"name": "Ravioli z łososiem", "description": "łosoś, seriola, kalarepa, pomidor dashi", "price": "98 PLN"},
            {"name": "Sałatka z okoniem", "description": "chrupiący okoń morski, pomelo, karmelizowane orzechy nerkowca, zioła", "price": "88 PLN"},
            {"name": "Shrimp har gao", "description": "pierożki z krewetkami, bisque z kraba, słodki olej chilli", "price": "72 PLN"},
            {"name": "Nasu miso", "description": "bakłażan, słodka glazura miso, sezam, szczypiorek", "price": "48 PLN"},
            {"name": "Ebi tempura", "description": "krewetki w tempurze, majonez japoński", "price": "92 PLN"},
            {"name": "Gyoza", "description": "wieprzowina lub kurczak, zielona cebulka, sos orientalny", "price": "68 PLN"},
            {"name": "Buns z szarpaną wieprzowiną", "description": "szarpana wieprzowina, orientalne warzywa, Sechuan, Sriracha", "price": "72 PLN"},
            {"name": "Polędwica wołowa Black Angus (170g)", "description": "pak choi, purée ziemniaczane z wasabi, sezam, sos orientalny", "price": "158 PLN"},
        ]

        context['desserts'] = [
            {"name": "Choux", "description": "biała czekolada, owoce jagodowe, matcha anglaise", "price": "42 PLN"},
            {"name": "Pomelo", "description": "mus z białej czekoladowy, wanilia, biszkopt kokosowy", "price": "42 PLN"},
            {"name": "Torcik Ruby", "description": "czekolada Ruby, jeżyny, czerwone pomarańcze", "price": "65 PLN"},
            {"name": "Lody", "description": "frosty & fruity", "price": "58 PLN"},
        ]

        context['cocktails'] = [
            {"name": "Above The Clouds", "description": "rum, olej kokosowy, masło kakaowe, likier słony karmel, dym, podawany z jadalnym złotem", "price": "—"},
            {"name": "Royal", "description": "Szampan Moet & Chandon Brut Imperial", "price": "—"},
            {"name": "Ichie", "description": "whiskey, ananas, marakuja, likier bananowy", "price": "—"},
            {"name": "The Duchess", "description": "wódka, cytryna, trawa cytrynowa, maliny, imbir, lemoniada", "price": "—"},
            {"name": "Bergamo", "description": "gin z kwiatem bzu, wino, różowy pieprz, zapach bergamotki, oliwa grejpfrutowa", "price": "—"},
            {"name": "Botanist", "description": "gin, likier z kwiatu bzu, ogórek, cytryna, lemoniada różana", "price": "—"},
            {"name": "Capuccini", "description": "bourbon, likier, mleko z orzechów laskowych, espresso, syrop klonowy, kropla śmietanki", "price": "—"},
            {"name": "Ruby Sky", "description": "bourbon, martini, likier z orzechów laskowych, ocet wiśniowy, bitters czekoladowy", "price": "—"},
            {"name": "Pink Flamingo", "description": "tequila, aperol, kordiał grejpfrutowy, nasiona kolendry, różowy pieprz, limonka, sól morska, woda gazowana", "price": "—"},
            {"name": "Bison in the Moss", "description": "wódka żubrówka, jabłko, mięta, imbir, cytryna, rumianek", "price": "—"},
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
    authentication_form = AuthenticationForm

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
