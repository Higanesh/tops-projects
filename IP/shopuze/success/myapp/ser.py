from myapp.models import *
from rest_framework import serializers

class NameSer(serializers.ModelSerializer):
    class Meta:
        model = Name
        fields = '__all__'