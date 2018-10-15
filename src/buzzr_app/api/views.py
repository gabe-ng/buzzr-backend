from rest_framework.generics import ListAPIView, RetrieveAPIView

from buzzr_app.models import Buzz
from .serializers import BuzzSerializer

class BuzzListView(ListAPIView):
    queryset = Buzz.objects.all()
    serializer_class = BuzzSerializer

class BuzzDetailView(RetrieveAPIView):
    queryset = Buzz.objects.all()
    serializer_class = BuzzSerializer