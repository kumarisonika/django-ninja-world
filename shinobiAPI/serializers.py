from dataclasses import fields
from rest_framework import serializers
from .models import Village
from .models import Nation
from .models import User


class VillageSerializer(serializers.ModelSerializer):

    class Meta:
        model = Village
        fields = ('id',
                  'village_name',
                  'description',
                  'nation',
                  'kage_name',
                  'element')

class NationSerializer(serializers.ModelSerializer):

    class Meta:
        model = Nation
        fields = ('id',
                  'nation_name',
                  'element',
                  'kage_name',
                  'description')

class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields=('username',
                'salt',
                'hashed_password')
