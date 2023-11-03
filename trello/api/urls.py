from django.urls import path
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
from trello import views

urlpatterns = [
    path('register', views.create_user, name='createUser'),
    path('index', views.index, name='index'),
    path('workspace/create', views.create_workspace, name='createWorkspace'),
    path('workspace/edit/<str:id>', views.edit_workspace, name='editWorkspace'),
    path('workspace/delete/<str:id>', views.delete_workspace, name='deleteWorkspace'),
    path('board/create/', views.create_board, name='createBoard'),
    path('board/show/<str:id>', views.show_board, name='showBoard'),
    path('board/edit/<str:id>', views.edit_board, name='editBoard'),
    path('board/delete/<str:id>', views.delete_board, name='deleteBoard'),
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]
