from rest_framework import serializers
from .models import Person
from rest_framework.exceptions import NotAuthenticated
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

class UsersSerializer(serializers.ModelSerializer):

    class Meta:
        model = Person
        #fields = ['Email', 'Password']
        fields = '__all__'

    def validate(self, data):
        username = data.get("username", None)
        password = data.get("password", None)
        if Person.objects.filter(username=username).filter(password=password).first():
            return True

        raise NotAuthenticated

        #def create(self, validated_data):
        #    return Person.objects.create(validated_data)
        
        #def update(self, instance, validated_data):
        #    instance.Email = validated_data.get('Email', instance.Email)
        #    instance.Passwrod = validated_data.get('Password', instance.Password)
        #    instance.save()
        #    return instance

class MyTokenObtainPairSerializer(TokenObtainPairSerializer):

        @classmethod

        def get_token(cls, user):
            token = super(MyTokenObtainPairSerializer, cls).get_token(user)

        # Add custom claims
            token['username'] = user.username
            return token

