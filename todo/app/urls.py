from django.urls import path
from .views import *

from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

urlpatterns = [
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('register/', register, name='register'),
    path('signin/', signin, name='signin'),
    path('getTodos/', getTodos, name='getTodos'),
    path('addTodo/', addTodo, name='addTodo'),
    path('updateTodo/<int:id>/', updateTodo, name='updateTodo'),
    path('deleteTodo/<int:id>/', deleteTodo, name='deleteTodo'),
    path('signout/',signout,name='signout')
]