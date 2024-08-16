from rest_framework import serializers
from services.models import MyService

class MyDetailsSerialzer(serializers.ModelSerializer):
    class Meta:
        model = MyService
        fields = "__all__"