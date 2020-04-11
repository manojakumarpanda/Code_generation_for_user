from .models import User_codes,User,profile
from rest_framework import serializers
from rest_framework.validators import UniqueTogetherValidator
from rest_framework import exceptions


class profile_serialiser(serializers.ModelSerializer):
    class Meta:
        model = profile
        fields = '__all__'

    def create(self, validated_data):
        return profile.objects.get_or_create(**validated_data)

from django.contrib.auth.models import User
class User_serialiser(serializers.ModelSerializer):
    def validate(self, data):
        username=data.get('username')
        password=data.get('password')
        email=data.get('email')
        first_name=data.get('first_name')
        last_name=data.get('last_name')
        if username and password and email and first_name and last_name:
            user=User(username=username,email=email,last_name=last_name,first_name=first_name)
            user.set_password(raw_password=password)
            user.save()
            return user

    class Meta:
        model=User
        fields = ['first_name', 'last_name', 'username', 'email', 'password',]
        validators = [
            UniqueTogetherValidator(
                queryset=User.objects.all(),
                fields=['username', 'email']
            )
        ]



class User_Create_serialiser(serializers.ModelSerializer):
    profile=profile_serialiser()
    class Meta:
        model=User
        fields = '__all__'
        validators = [
            UniqueTogetherValidator(
                queryset=User.objects.all(),
                fields=['username', 'email']
            )
        ]

    def create(self, validated_data):
        return User.objects.get_or_create(**validated_data)


class code_serialisers(serializers.ModelSerializer):
    class Meta:
        model=User_codes
        fields='__all__'

    def create(self, validated_data):
        return User_codes.objects.get_or_create(**validated_data)

from django.contrib.auth import authenticate,login
class Login_serialiser(serializers.Serializer):
    username=serializers.CharField(max_length=50)
    password=serializers.CharField(max_length=50)

    def validate(self, attrs):
        username=attrs.get('username','')
        password=attrs.get('password','')

        if username and password:
            user=authenticate(username=username,password=password)
            if user:
                if user.is_active:
                    attrs['user']=user
                else:
                    raise  exceptions.ValidationError('Use is no more active')
        else:
            raise exceptions.ValidationError('password and username is require')
        return attrs