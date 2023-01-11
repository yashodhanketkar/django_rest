from django.contrib.auth.models import User, Group
from .models import Accounts
from rest_framework import viewsets, permissions
from .serializers import UserSerializers, GroupSerializers, AccountSerializers


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializers
    permission_classes = [permissions.IsAuthenticated]


class GroupViewSet(viewsets.ModelViewSet):
    queryset = Group.objects.all()
    serializer_class = GroupSerializers 
    permission_classes = [permissions.IsAuthenticated]


class AccountViewSet(viewsets.ModelViewSet):
    queryset = Accounts.objects.all().order_by('rank')
    serializer_class = AccountSerializers
    permission_classes = [permissions.AllowAny]
