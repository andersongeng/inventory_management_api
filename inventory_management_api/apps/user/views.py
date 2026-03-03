from django.shortcuts import render

# Create your views here.
from rest_framework import generics, permissions
from .serializers import RegisterSerializer

class RegisterView(generics.CreateAPIView):
    serializer_class = RegisterSerializer
    # Permitimos que cualquiera pueda acceder a este endpoint para registrarse
    permission_classes = [permissions.AllowAny]