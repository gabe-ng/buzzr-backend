from django.urls import path

from .views import ProfileListView, ProfileDetailView, BuzzListView, BuzzDetailView

urlpatterns = [
    path("buzzs/", BuzzListView.as_view()),
    path("buzzs/<pk>", BuzzDetailView.as_view()),
    path("profiles/", ProfileListView.as_view()),
    path("profiles/<pk>", ProfileDetailView.as_view()),
]