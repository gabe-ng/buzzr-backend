from rest_framework import generics

from buzzr_app.models import Buzz
from .serializers import BuzzSerializer

class BuzzListView(generics.ListCreateAPIView):
    queryset = Buzz.objects.all()
    serializer_class = BuzzSerializer

class BuzzDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Buzz.objects.all()
    serializer_class = BuzzSerializer