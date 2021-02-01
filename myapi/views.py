from django.shortcuts import render
from rest_framework import viewsets, mixins

from .serializers import HeroSerializer, PeopleSerializer
from .models import Hero
from myapi import serializers

class HeroViewSet(viewsets.ModelViewSet):
    queryset = Hero.objects.all().order_by('name')
    serializer_class = HeroSerializer

class PeopleViewSet(mixins.ListModelMixin, mixins.RetrieveModelMixin, viewsets.GenericViewSet):
    queryset = Hero.objects.all().order_by('name')
    serializer_class = PeopleSerializer