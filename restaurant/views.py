# Home page
class HomeView(TemplateView):
    template_name = 'restaurant/home.html'

# Menu page — now loads data from the database
class MenuView(TemplateView):
    template_name = 'restaurant/menu.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        # Use filter instead of get to avoid DoesNotExist error
        food_category = MenuItem.objects.filter(category__name='food')
        dessert_category = MenuItem.objects.filter(category__name='dessert')
        cocktail_category = MenuItem.objects.filter(category__name='cocktail')

        context['food'] = food_category
        context['desserts'] = dessert_category
        context['cocktails'] = cocktail_category
        
        return context

# Gallery
class GalleryView(TemplateView):
    template_name = 'restaurant/gallery.html'

# Contacts
class ContactsView(TemplateView):
    template_name = 'restaurant/contacts.html'

# Reservation page
class ReservationPageView(TemplateView):
    template_name = 'restaurant/reservation.html'

# Reservation form submission
class ReserveTableView(FormView):
    template_name = 'restaurant/reservation.html'
    form_class = ReservationForm
    success_url = reverse_lazy('reservation')

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)

# Review submission
class SubmitReviewView(FormView):
    template_name = 'restaurant/review_form.html'
    form_class = ReviewForm
    success_url = reverse_lazy('review_thanks')

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)

# Thank you page for review
class ReviewThanksView(TemplateView):
    template_name = 'restaurant/review_thanks.html'

# Login
class CustomLoginView(LoginView):
    template_name = 'restaurant/login.html'
    authentication_form = AuthenticationForm

# Logout
class CustomLogoutView(LogoutView):
    next_page = reverse_lazy('login')

# Registration
@method_decorator(csrf_protect, name='dispatch')
class RegistrationView(FormView):
    template_name = 'restaurant/registration.html'
    form_class = UserCreationForm
    success_url = reverse_lazy('login')

    def form_valid(self, form):
        form.save()
        messages.success(self.request, 'Registration successful! You can now log in.')
        return super().form_valid(form)

    def form_invalid(self, form):
        messages.error(self.request, "Registration error. Please try again.")
        return super().form_invalid(form)

# User profile
class ProfileView(TemplateView):
    template_name = 'profile.html'
