from django.views.generic import CreateView
from django.urls import reverse_lazy

from .forms import RegistrationForm

# Create your views here.

class RegistrationView(CreateView):
    form_class = RegistrationForm
    template_name = "accounts/register.html"
    success_url = reverse_lazy("login")