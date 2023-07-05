from rest_framework import serializers
from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password
from Mobile_App.models import *
from rest_framework.validators import UniqueTogetherValidator


class FondateurSerializer(serializers.ModelSerializer):
    class Meta:
        model=Fondateur
        fields='__all__'
        validators=[
            UniqueTogetherValidator(
                queryset=Fondateur.objects.all(),
                fields=['nom','postnom','prenom'],
                message="Ce Fondateur existe déjà"
            )
        ]

class PartiPolitiqueSerializer(serializers.ModelSerializer):
    class Meta:
        model=PartiPolitique
        fields='__all__'


class ViewPartiFondateurSerializer(serializers.ModelSerializer):
    fondateur=FondateurSerializer()
    class Meta:
        model=PartiPolitique
        fields='__all__'

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model=User
        fields="__all__"
    def create(self, validated_data):
        user=User(
            username=validated_data['username'],
            first_name=validated_data['first_name'],
            last_name=validated_data['last_name'],
            email=validated_data['email'],
            password=make_password(validated_data['password'])
            #is_staff=validated_data['is_staff']
        )
        user.save()
        return user
    