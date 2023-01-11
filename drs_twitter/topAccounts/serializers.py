from django.contrib.auth.models import User, Group
from .models import Accounts
from rest_framework import serializers


class UserSerializers(serializers.HyperlinkedModelSerializer):
    class Meta:
        model: User = User
        fields: list = ['url', 'username', 'email', 'groups']


class GroupSerializers(serializers.HyperlinkedModelSerializer):
    class Meta:
        model: Group = Group
        fields: list = ['url', 'name']


class AccountSerializers(serializers.HyperlinkedModelSerializer):
    class Meta:
        model: Accounts = Accounts
        fields: list = ['rank', 'account_name', 'brand_account', 'followers']
