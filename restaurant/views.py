from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import ReservationForm
from .forms import ReviewForm, Review

def home(request):
    return render(request, 'restaurant/home.html')

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

def gallery(request):
    return render(request, 'restaurant/gallery.html')

def contacts(request):
    return render(request, 'restaurant/contacts.html')

def reservation(request):
    return render(request, 'restaurant/reservation.html')

def submit_review(request):
    return HttpResponse("Review submitted!")

def reserve_table(request):
    if request.method == 'POST':
        form = ReservationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('reservation')
    else:
        form = ReservationForm()
    return render(request, 'restaurant/reservation.html', {'form': form})

def submit_review(request):
    if request.method == 'POST':
        form = ReviewForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'restaurant/review_thanks.html')
    else:
        form = ReviewForm()
    return render(request, 'restaurant/review_form.html', {'form': form})

def submit_review(request):
    if request.method == 'POST':
        form = ReviewForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'restaurant/review_thanks.html')
    else:
        form = ReviewForm()
    return render(request, 'restaurant/review_form.html', {'form': form})