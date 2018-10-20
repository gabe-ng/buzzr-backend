from rest_framework import serializers

from buzzr_app.models import Profile, Buzz

class BuzzSerializer(serializers.ModelSerializer):
    class Meta:
        model = Buzz
        fields = ("profile", "title", "content", "create_date", "num_likes")

class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = ("user", "full_name", "user_name", "email", "followers", "join_date")