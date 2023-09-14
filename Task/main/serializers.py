from rest_framework import serializers
from .models import Customer

class CustomerRegistrationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = ('name', 'email', 'password')
        extra_kwargs = {'password': {'write_only': True}}
