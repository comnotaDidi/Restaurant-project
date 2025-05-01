from django.urls import path
from .views import (
    HomeView, MenuView, GalleryView, ContactsView, ReservationPageView,
    ReserveTableView, SubmitReviewView, ReviewThanksView,
    CustomLoginView, CustomLogoutView, RegistrationView, ProfileView,
)

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('menu/', MenuView.as_view(), name='menu'),
    path('gallery/', GalleryView.as_view(), name='gallery'),
    path('contacts/', ContactsView.as_view(), name='contacts'),
    path('reservation/', ReservationPageView.as_view(), name='reservation'),
    path('reserve/', ReserveTableView.as_view(), name='reserve_table'),
    path('submit-review/', SubmitReviewView.as_view(), name='submit_review'),
    path('review/thanks/', ReviewThanksView.as_view(), name='review_thanks'),
    path('login/', CustomLoginView.as_view(), name='login'),
    path('logout/', CustomLogoutView.as_view(), name='logout'),
    path('registration/', RegistrationView.as_view(), name='registration'),
    path('profile/', ProfileView.as_view(), name='profile'),
]
