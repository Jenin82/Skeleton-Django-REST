from datetime import datetime
from django.http import JsonResponse
from rest_framework import generics, permissions, mixins
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework import status
# from user.models import Todo
from user.serializers import MyTokenObtainPairSerializer, RegisterSerializer

# Routes to be displayed
class Routes(APIView):
	def get(self, request, format=None):
		routes = [
			'api/login',
			'api/token/refresh',
			'api/register/',
			# 'api/todo/   - use GET to retrieve all Todo and POST to create a new one. body:[title:'']',
			# 'todo/<str:pk>/   - use PUT or DELETE to update status/delete a Todo, provide todo id in url eg: todo/7/',
			]
		return Response(routes)

# Token Generators
class MyTokenObtainPairView(TokenObtainPairView):
	serializer_class = MyTokenObtainPairSerializer

#Register API
class RegisterApi(generics.GenericAPIView):
    serializer_class = RegisterSerializer
    def post(self, request, *args,  **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        return Response({
            "message": "User Created Successfully.  Now perform Login to get your token",
        })
