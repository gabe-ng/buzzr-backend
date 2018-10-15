from django.urls import path

from .views import BuzzListView, BuzzDetailView

urlpatterns = [
    path("", BuzzListView.as_view()),
    path("<pk>", BuzzDetailView.as_view())
]