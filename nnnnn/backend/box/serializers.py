from rest_framework import serializers
from .models import Users
from django.contrib.auth import authenticate
from django.contrib.auth.hashers import make_password, check_password

class UserSerializers(serializers.ModelSerializer):
    class Meta:
        model = Users
        fields = ['email', 'password', 'username']

    def create(self, validated_data):
        validated_data['password'] = make_password(validated_data['password'])
        return super().create(validated_data)

    def update(self, instance, validated_data):
        if 'password' in validated_data:
            validated_data['password'] = make_password(validated_data['password'])
        return super().update(instance, validated_data)

class LoginSerializer(serializers.Serializer):
    email = serializers.CharField()
    password = serializers.CharField()

    def validate(self, data):
        try:
            user = Users.objects.get(email = data['email'])
        except Users.DoesNotExist:
            raise serializers.ValidationError("User not found")
        
        if not check_password(data['password'], user.password):
            raise serializers.ValidationError("Incorrect password")
        
        data['user'] = user
        return data