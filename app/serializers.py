from rest_framework import serializers
from .models import *



class ParadigmSerializer(serializers.ModelSerializer):
     
    class Meta:
        model = Paradigm
        fields = ("id",'name')

class LanguageSerializer(serializers.ModelSerializer):

    class Meta:
        model = Paradigm
        fields = ("id",'name','paradigm')

class ProgrammerSerializer(serializers.ModelSerializer):

    class Meta:
        model = Programmer
        fields = ("id","name","laguages")
