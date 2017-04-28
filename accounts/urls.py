from django.conf.urls import url
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    url(r'^register$', views.RegistrationView.as_view(), name='registration'),
    url(r'^login$', auth_views.login, { 'template_name':'accounts/login.html'}, name='login'),
]