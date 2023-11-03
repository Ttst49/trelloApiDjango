from rest_framework.serializers import ModelSerializer
from trello.models import *


class UserCreateSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'password']


class UserSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = ["id", "username"]


class WorkspaceSerializer(ModelSerializer):
    owner = UserSerializer()
    members = UserSerializer(many=True)

    class Meta:
        model = Workspace
        fields = ['id', 'name', 'description', 'type', 'owner', 'members']


class WorkspaceCreateSerializer(ModelSerializer):
    class Meta:
        model = Workspace
        fields = ['id', 'name', 'description', 'type']


class VisibilitySerializer(ModelSerializer):
    class Meta:
        model = Visibility
        fields = ['name']


class BoardSerializer(ModelSerializer):
    visibility = VisibilitySerializer()

    class Meta:
        model = Board
        fields = ['id', 'name', 'description', 'visibility']

class BoardCreateSerializer(ModelSerializer):
    class Meta:
        model = Board
        fields = ['id', 'name', 'description', "visibility"]
