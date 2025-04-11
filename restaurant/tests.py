from django.test import TestCase
from django.urls import reverse
from restaurant.models import Reservation
from restaurant.forms import ReservationForm

class ReservationModelTest(TestCase):
    def test_create_reservation(self):
        reservation = Reservation.objects.create(
            name="John Doe",
            email="john@example.com",
            date="2025-05-01",
            time="19:00",
            guests=2
        )
        self.assertEqual(reservation.name, "John Doe")
        self.assertEqual(reservation.guests, 2)

class GalleryViewTest(TestCase):
    def test_gallery_page(self):
        response = self.client.get(reverse('gallery'))  # Убедись, что в urls.py используется имя 'gallery'
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'restaurant/gallery.html')

class ReservationFormTest(TestCase):
    def test_valid_form(self):
        form_data = {
            'name': 'Alice',
            'email': 'alice@example.com',
            'date': '2025-05-01',
            'time': '20:00',
            'guests': 4
        }
        form = ReservationForm(data=form_data)
        self.assertTrue(form.is_valid())
