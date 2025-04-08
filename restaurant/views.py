from django.shortcuts import render
from .forms import ReservationForm
from django.shortcuts import redirect
from django.http import HttpResponse

def home(request):
    return render(request, 'home.html')

def home(request):
    return render(request, 'restaurant/home.html')

def menu(request):
    return render(request, 'restaurant/menu.html')

def gallery(request):
    return render(request, 'restaurant/gallery.html')

def contacts(request):
    return render(request, 'restaurant/contacts.html')

def home(request):
    return render(request, "restaurant/home.html")

def reservation(request):
    return render(request, "restaurant/reservation.html")

def gallery(request):
    return render(request, "restaurant/gallery.html")

def submit_review(request):
    # Логика для обработки отзыва
    return HttpResponse("Review submitted!")

def reserve_table(request):
    if request.method == 'POST':
        form = ReservationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('reservation')  # Или на страницу "Спасибо"
    else:
        form = ReservationForm()
    return render(request, 'restaurant/reservation.html', {'form': form})

