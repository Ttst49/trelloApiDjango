from rest_framework.serializers import ModelSerializer
from trello.models import *


class WorkspaceSerializer(ModelSerializer):
    class Meta:
        model = Workspace
        fields = ['name', 'description', 'type']


class UserCreateSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'password']
