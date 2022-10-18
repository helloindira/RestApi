from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
# Create your views here.
from .models import Paradigm,Language,Programmer
from .serializers import ParadigmSerializer,LanguageSerializer,ProgrammerSerializer


class ParadigmView(APIView):
    @staticmethod
    def get(self):
        serializer = ParadigmSerializer(Paradigm.objects.all(),many=True)
        return Response(serializer.data)
    @staticmethod
    def post(request):
        serializer = ParadigmSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            Paradigm.objects.create(**(serializer.validated_data)) 
            return Response(serializer.validated_data)
        

class ParadigmDetailView(APIView):
    @staticmethod
    def get(request,pk):
        try:
            return Response(ParadigmSerializer(Paradigm.objects.get(pk=pk), many=False))
        except Paradigm.DoesNotExist:
            #f"my name is {pk}"
            return Response({"Error":f"Invalid Student Id {pk}"})

    @staticmethod
    def put(request,pk):
        paradigm = Paradigm.objects.get(pk=pk)
        serializer = ParadigmSerializer(instance=paradigm,data=request.data)
        if serializer.is_valid():
            serializer.save()
        return Response(serializer.validated_data)


    @staticmethod
    def delete(self,request,pk):
        try:
            Paradigm.objects.get(pk=pk).delete()
            return Response({"Message":"Data Successfully Delete"})
        except Paradigm.DoesNotExist:
            return Response({"Error":"Invalid Data"})

# Create Language Apiview

class LanguageView(APIView):
    @staticmethod
    def get(self):
        serializer = LanguageSerializer(Language.objects.all(),many=True)
        return Response(serializer.data)
    @staticmethod
    def post(request):
        serializer = LanguageSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            Language.objects.create(**(serializer.validated_data)) 
            return Response(serializer.validated_data)
        

class LanguageDetailView(APIView):
    @staticmethod
    def get(request,pk):
        try:
            return Response(LanguageSerializer(Language.objects.get(pk=pk), many=False))
        except Language.DoesNotExist:
            #f"my name is {pk}"
            return Response({"Error":f"Invaid Student Id {pk}"})

    @staticmethod
    def put(request,pk):
        language = Language.objects.get(pk=pk)
        serializer = LanguageSerializer(instance=language,data=request.data)
        if serializer.is_valid():
            serializer.save()
        return Response(serializer.validated_data)


    @staticmethod
    def delete(self,request,pk):
        try:
            Language.objects.get(pk=pk).delete()
            return Response({"Message":"Data Successfully Delete"})
        except Language.DoesNotExist:
            return Response({"Error":"Invalid Data"})

# Created Programmer ApiView


class ProgrammerView(APIView):
    @staticmethod
    def get(self):
        serializer = ProgrammerSerializer(Programmer.objects.all(),many=True)
        return Response(serializer.data)
    @staticmethod
    def post(request):
        serializer = ProgrammerSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            Programmer.objects.create(**(serializer.validated_data)) 
            return Response(serializer.validated_data)
        

class ProgrammerDetailView(APIView):
    @staticmethod
    def get(request,pk):
        try:
            return Response(ProgrammerSerializer(Programmer.objects.get(pk=pk), many=False))
        except Programmer.DoesNotExist:
            #f"my name is {pk}"
            return Response({"Error":f"Invaid Student Id {pk}"})

    @staticmethod
    def put(request,pk):
        language = Programmer.objects.get(pk=pk)
        serializer = ProgrammerSerializer(instance=language,data=request.data)
        if serializer.is_valid():
            serializer.save()
        return Response(serializer.validated_data)


    @staticmethod
    def delete(self,request,pk):
        try:
            Programmer.objects.get(pk=pk).delete()
            return Response({"Message":"Data Successfully Delete"})
        except Programmer.DoesNotExist:
            return Response({"Error":"Invalid Data"})