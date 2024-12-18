from rest_framework import serializers
from django.contrib.auth.models import User

class RegisterSerializer(serializers.ModelSerializer):

    password2 = serializers.CharField(write_only = True)
    class Meta:
        model = User
        fields = ['username','email','password', 'password2']
    
    def validate(self, data):
        if data['password'] != data['password2']:
            raise serializers.ValidationError("password must match")
        return data
    
    def create(self, validate_data):
        user = User.objects.create_user(
            username=validate_data['username'],
            email=validate_data['email'],
            passwors=validate_data['password']
            )
        return user
