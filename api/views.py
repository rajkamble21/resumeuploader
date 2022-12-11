from django.shortcuts import render
from .serializers import ResumeSerializer
from rest_framework import viewsets
from myapp.models import Resume
from rest_framework.authentication import SessionAuthentication
from rest_framework.permissions import IsAuthenticated


class ResumeModelViewset(viewsets.ModelViewSet):
    queryset = Resume.objects.all()
    serializer_class = ResumeSerializer
    authentication_classes = [SessionAuthentication]
    permission_classes = [IsAuthenticated]
