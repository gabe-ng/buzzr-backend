from rest_framework import generics

from buzzr_app.models import Profile, Buzz
from .serializers import Profile, BuzzSerializer

class ProfileListView(generics.ListCreateAPIView):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer

class ProfileDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer

class BuzzListView(generics.ListCreateAPIView):
    queryset = Buzz.objects.all()
    serializer_class = BuzzSerializer

class BuzzDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Buzz.objects.all()
    serializer_class = BuzzSerializer