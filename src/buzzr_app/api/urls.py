from django.urls import path

from .views import BuzzListView, BuzzDetailView

urlpatterns = [
    path("buzzs/", BuzzListView.as_view()),
    path("buzzs/<pk>", BuzzDetailView.as_view())
]