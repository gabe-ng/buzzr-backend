from rest_framework import serializers

from buzzr_app.models import Buzz

class BuzzSerializer(serializers.ModelSerializer):
    class Meta:
        model = Buzz
        fields = ("title", "content")