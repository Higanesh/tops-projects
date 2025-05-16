from rest_framework import serializers
from myapp.models import *

class EmpSerializer(serializers.ModelSerializer):
    class Meta:
        model=Employee
        fields='__all__'