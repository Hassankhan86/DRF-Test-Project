from rest_framework import serializers
from users.models import Profile


class ProfileSerializers(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = '__all__'

