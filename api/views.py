from django.shortcuts import render

# Create your views here.
from rest_framework import generics


from menu.models import Menu_Item
from .serializers import MenuSerializer



class MenuListAPIView(generics.ListAPIView):
    queryset = Menu_Item.objects.all()
    serializer_class = MenuSerializer
