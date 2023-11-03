from rest_framework import status
from rest_framework.decorators import permission_classes, api_view
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from trello.api.serializers import WorkspaceSerializer, UserCreateSerializer
from trello.models import Workspace


@api_view(['POST'])
def create_user(request):
    if request.method == 'POST':
        user = UserCreateSerializer(data=request.data)
        if user.is_valid():
            user.save()
            return Response(user.data.username, status=status.HTTP_201_CREATED)
    return Response("nope sorry", status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def index(request):
    workspaces = Workspace.objects.all()
    serialized_workspaces = WorkspaceSerializer(workspaces, many=True)

    return Response(serialized_workspaces.data, status=status.HTTP_200_OK)


def create_workspace(request):
    pass

def edit_workspace(request, id):
    pass

def delete_workspace(request, id):
    pass


def