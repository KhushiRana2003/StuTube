from rest_framework import serializers
from .models import Room
class serial(serializers.ModelSerializer):
    class meta:
        model=Room
        fields=('code')

