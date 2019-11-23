from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from drf.serializers import User_Serializer, Group_Serializer

class User_Viewset(viewsets.ModelViewSet):
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = User_Serializer

class Group_Viewset(viewsets.ModelViewSet):
    queryset = Group.objects.all()
    serializer_class = Group_Serializer
    