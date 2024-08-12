from rest_framework import serializers
from services.models import Service

class MyDetailsSerialzer(serializers.ModelSerializer):
    class Meta:
        model = Service
        fields = "__all__"