from myapp.models import *
from rest_framework import serializers

class userSerializer(serializers.ModelSerializer):
    class Meta:
        model = Myuser
        fields = "__all__"