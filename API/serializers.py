from django.db.models import fields
from rest_framework import serializers
from .models import Prod


class prodSerializer(serializers.ModelSerializer):
    class Meta:
        model = Prod
        fields = '__all__'