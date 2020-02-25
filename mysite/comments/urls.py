from django.urls import path
from django.conf.urls import url
from . import views
from django.views.generic import TemplateView

app_name="comments"

urlpatterns = [
    path('', views.entries, name="entries"),
    path('make_entry/', views.make_entry, name="make_entry"),
    path('entry/<int:entry_id>/', views.entry_detail, name='entry_detail'),
    path('entry/<int:entry_id>/make_comment', views.make_comment, name='make_comment'),
    path('upvote/<int:entry_id>/', views.upvote, name='upvote'),
    path('downvote/<int:entry_id>/', views.downvote, name='downvote'),
    path('remove_comment/<int:comment_id>/<int:entry_id>/', views.remove_comment, name='remove_comment'),
    path('edit_comment/<int:comment_id>/<int:entry_id>/', views.edit_comment, name='edit_comment'),
]