from rest_framework import status
from rest_framework.decorators import permission_classes, api_view
from rest_framework.generics import get_object_or_404
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from trello.api.serializers import *
from trello.models import Workspace, Board


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


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def create_workspace(request):
    if request.method == 'POST':
        workspace = WorkspaceCreateSerializer(data=request.data)
        if workspace.is_valid():
            workspace.save(owner=request.user, members=[request.user])
            return Response(workspace.data, status=status.HTTP_201_CREATED)
    return Response("Bad Request, an error occurred", status=status.HTTP_400_BAD_REQUEST)


@api_view(['PUT'])
@permission_classes([IsAuthenticated])
def edit_workspace(request, id):
    workspace = get_object_or_404(Workspace, id=id)
    if workspace is not None:
        if workspace.owner != request.user:
            return Response("Vous n'êtes pas le propriétaire de cette workspace", status=status.HTTP_403_FORBIDDEN)
        workspace_serialized = WorkspaceSerializer(data=request.data, instance=workspace)
        if workspace_serialized.is_valid():
            workspace_serialized.save(owner=request.user, members=[request.user])
            return Response(workspace_serialized.data, status=status.HTTP_200_OK)
    return Response("Bad Request", status=status.HTTP_400_BAD_REQUEST)


@api_view(['DELETE'])
@permission_classes([IsAuthenticated])
def delete_workspace(request, id):
    workspace = get_object_or_404(Workspace, id=id)
    if workspace is not None:
        if workspace.owner != request.user:
            return Response("Vous n'êtes pas le propriétaire de cette workspace", status=status.HTTP_403_FORBIDDEN)
    workspace.delete()
    return Response("Supprimé avec success", status=status.HTTP_200_OK)


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def show_board(request, id):
    board = get_object_or_404(Board, id=id)
    if board is not None:
        serialized_board = BoardSerializer(board)
        return Response(serialized_board.data, status=status.HTTP_200_OK)
    return Response("Ce tableau n'a pas été trouvé", status=status.HTTP_404_NOT_FOUND)


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def create_board(request, id):
    if request.method == 'POST':
        workspace = get_object_or_404(Workspace, id=id)
        if workspace is not None:
            board = BoardCreateSerializer(data=request.data)
            if board.is_valid():
                board.save(members=[request.user])
                workspace.boards.add(board.data.get('id'))
                return Response(board.data, status=status.HTTP_201_CREATED)
        return Response('Pas de workspace où ajouter ce tableau', status=status.HTTP_400_BAD_REQUEST)
    return Response("Mauvaise requete", status=status.HTTP_400_BAD_REQUEST)


@api_view(['PUT'])
@permission_classes([IsAuthenticated])
def edit_board(request, id):
    board = get_object_or_404(Board, id=id)
    if board is not None:
        if not board.members.filter(id=request.user.id).exists():
            return Response("Vous n'êtes pas membre de ce tableau", status=status.HTTP_403_FORBIDDEN)
        board_serialized = BoardCreateSerializer(data=request.data, instance=board)
        if board_serialized.is_valid():
            board_serialized.save(owner=request.user, members=[request.user])
            return Response(board_serialized.data, status=status.HTTP_200_OK)
    return Response("Mauvaise requete", status=status.HTTP_400_BAD_REQUEST)


@api_view(['DELETE'])
@permission_classes([IsAuthenticated])
def delete_board(request, id):
    board = get_object_or_404(Board, id=id)
    if board is not None:
        if not board.members.filter(id=request.user.id).exists():
            return Response("Vous n'êtes pas membre de ce tableau", status=status.HTTP_403_FORBIDDEN)
    board.delete()
    return Response("Supprimé avec success", status=status.HTTP_200_OK)


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def create_list(request):
    if request.method == 'POST':
        list = BoardCreateSerializer(data=request.data)
        if list.is_valid():
            list.save(members=[request.user])
            return Response(list.data, status=status.HTTP_201_CREATED)
    return Response("Mauvaise requete", status=status.HTTP_400_BAD_REQUEST)


def edit_list(request, id):
    pass


def delete_list(request, id):
    # put items in the archive list and remove it from the board
    pass


def show_card(request):
    pass


def create_card(request):
    pass


def edit_card(request, id):
    pass


def delete_card(request, id):
    pass

# pouvoir envoyer des requetes pour rejoindre des workspaces et des tableaux
