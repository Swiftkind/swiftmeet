from django.shortcuts import render, redirect
from .forms import CustomUserCreationForm
from django.views.generic import TemplateView
from .models import Account

# Create your views here.
class RegistrationView(TemplateView):
    template_name = 'accounts/register.html'
    form_class = CustomUserCreationForm
    initial = {'key': 'value'}
    def get(self, request, *args, **kwargs):
        form = self.form_class()
        return render(request, self.template_name, {'form': form})
    def post(self, request, *args, **kwargs):
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
        else:
            print form.errors
            return render(request, self.template_name, {'form': form})
