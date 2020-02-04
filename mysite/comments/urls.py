from django.urls import path
from . import views
from django.views.generic import TemplateView

app_name="comments"

urlpatterns = [
    path('', views.entries, name="entries"),
    path('make_entry/', views.make_entry, name="make_entry"),
    path('entry/<int:entry_id>/', views.entry_detail, name='entry_detail'),
    path('upvote/<int:entry_id>/', views.upvote, name='upvote'),
    path('downvote/<int:entry_id>/', views.downvote, name='downvote'),
]