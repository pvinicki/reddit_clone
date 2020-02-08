from django.urls import path
from . import views
from django.views.generic import TemplateView

app_name = 'accounts'

urlpatterns = [
    path('register/', views.register_view, name='register_view'),
    path('login/', views.login_view, name='login_view'),
]