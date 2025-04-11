from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib import messages
from django.urls import reverse
from .forms import ReservationForm, ReviewForm, LoginForm, RegistrationForm

# Главная страница
def home(request):
    return render(request, 'restaurant/home.html')

# Меню
def menu(request):
    food = [
        ("Kawior Antonius", "kawior Antonius, crème fraîche, bliny, złoto", "350 PLN"),
        ("Sushi Bites", "ryż do sushi, tuńczyk błękitnopłetwy, łosoś, seriola, dodatki", "72 PLN"),
        ("Tartaletka z tuńczykiem", "tuńczyk błękitnopłetwy, emulsja nori, kawior", "88 PLN"),
        ("Ostryga Gillardeau / 1 szt.", "ostryga, imbir, zielone jabłko, kawior limonkowy", "42 PLN"),
        ("Bubu arare", "brokuły, krem z awokado, perły ryżowe", "48 PLN"),
        ("Tsukemono", "ogórek, sezam", "18 PLN"),
        ("Tatar wołowy", "wołowina black angus, domowy tost, kapary, marynowane szalotki", "84 PLN"),
        ("Tuna tataki", "tuńczyk błękitnopłetwy, awokado, ogórek, imbir, yuzu", "92 PLN"),
        ("Tuna toro & crispy rice", "tuńczyk błękitnopłetwy, ryż, aioli z pora", "82 PLN"),
        ("Ravioli z łososiem", "łosoś, seriola, kalarepa, pomidor dashi", "98 PLN"),
        ("Sałatka z okoniem", "chrupiący okoń morski, pomelo, karmelizowane orzechy nerkowca, zioła", "88 PLN"),
        ("Shrimp har gao", "pierożki z krewetkami, bisque z kraba, słodki olej chilli", "72 PLN"),
        ("Nasu miso", "bakłażan, słodka glazura miso, sezam, szczypiorek", "48 PLN"),
        ("Ebi tempura", "krewetki w tempurze, majonez japoński", "92 PLN"),
        ("Gyoza", "wieprzowina lub kurczak, zielona cebulka, sos orientalny", "68 PLN"),
        ("Buns z szarpaną wieprzowiną", "szarpana wieprzowina, orientalne warzywa, Sechuan, Sriracha", "72 PLN"),
        ("Polędwica wołowa Black Angus (170g)", "pak choi, purée ziemniaczane z wasabi, sezam, sos orientalny", "158 PLN"),
    ]

    desserts = [
        ("Choux", "biała czekolada, owoce jagodowe, matcha anglaise", "42 PLN"),
        ("Pomelo", "mus z białej czekoladowy, wanilia, biszkopt kokosowy", "42 PLN"),
        ("Torcik Ruby", "czekolada Ruby, jeżyny, czerwone pomarańcze", "65 PLN"),
        ("Lody", "frosty & fruity", "—"),
    ]

    cocktails = [
        ("Cosmopolitan", "Wódka Belvedere, Cointreau, Żurawina, Limonka 14% ABV", "63 PLN"),
        ("Mai Tai", "Rum Plantation, Cointreau, Limonka, Kordiał Migdałowy 16% ABV", "63 PLN"),
        ("Margarita", "Tequila Don Julio, Cointreau, Sok z Limonki 12% ABV", "66 PLN"),
        ("Moscow Mule", "Wódka Belvedere, Limonka, Imbir, Piwo Imbirowe 17% ABV", "58 PLN"),
        ("Bloody Mary", "Wódka J.A. Baczewski, Sok Pomidorowy, Tabasco, Worchestershire 10% ABV", "55 PLN"),
        ("Piña Colada", "Rum Plantation (ciemny i jasny), Kokos, Ananas 12% ABV", "58 PLN"),
        ("Long Island 90'", "Wódka, Gin, Rum, Tequila, Cointreau, Cytryna, Pepsi 16% ABV", "67 PLN"),
        ("Hugo", "St. Germain, Prosecco, Limonka, Mięta, Woda Gazowana 11% ABV", "64 PLN"),
        ("P**n Star Martini", "Belvedere, Moët, Passoa, Marakuja, Wanilia 11% ABV", "70 PLN"),
        ("Old Cuban", "Rum Plantation, Moët, Mięta, Limonka, Bitters 14% ABV", "68 PLN"),
        ("Espresso Martini", "Rum Plantation, Limonka, Mięta, Cukier, Woda Gazowana 12% ABV", "60 PLN"),
        ("Old Fashioned", "Bourbon Woodford, Cukier Trzcinowy, Bitters, Skórka Pomarańczy 23% ABV", "—"),
    ]

    return render(request, 'restaurant/menu.html', {
        'food': food,
        'desserts': desserts,
        'cocktails': cocktails,
    })

# Гостевая книга
def gallery(request):
    return render(request, 'restaurant/gallery.html')

# Контакты
def contacts(request):
    return render(request, 'restaurant/contacts.html')

# Бронирование
def reservation(request):
    return render(request, 'restaurant/reservation.html')

# Форма бронирования
def reserve_table(request):
    if request.method == 'POST':
        form = ReservationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('reservation')
    else:
        form = ReservationForm()
    return render(request, 'restaurant/reservation.html', {'form': form})

# Отправка отзыва
def submit_review(request):
    if request.method == 'POST':
        form = ReviewForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'restaurant/review_thanks.html')
    else:
        form = ReviewForm()
    return render(request, 'restaurant/review_form.html', {'form': form})

# Логин и логаут с кастомными представлениями
from django.contrib.auth.views import LoginView, LogoutView

class CustomLoginView(LoginView):
    template_name = 'restaurant/login.html'  # Указан правильный путь к шаблону
    authentication_form = AuthenticationForm

    def get_success_url(self):
        return reverse('home')  # Редирект на главную страницу после успешного входа

class CustomLogoutView(LogoutView):
    next_page = 'login'  # Страница, куда будет перенаправляться после выхода

# Логин
def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('home')  # Перенаправление на главную страницу
            else:
                messages.error(request, "Такого пользователя не существует.")
    else:
        form = LoginForm()

    return render(request, 'restaurant/login.html', {'form': form})

# Регистрация
def registration_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()  # Сохраняем пользователя
            messages.success(request, 'Регистрация прошла успешно! Теперь вы можете войти.')
            return redirect('login')  # Перенаправляем на страницу логина после успешной регистрации
        else:
            messages.error(request, "Ошибка регистрации. Пожалуйста, попробуйте еще раз.")
    else:
        form = UserCreationForm()

    return render(request, 'restaurant/registration.html', {'form': form})

def profile(request):
    # Логика для страницы профиля
    return render(request, 'profile.html')
