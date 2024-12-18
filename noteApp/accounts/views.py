from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import authentication,permissions
from django.contrib.auth.models import User
from .serializers import RegisterSerializer
from rest_framework import status
from rest_framework_simplejwt.tokens import RefreshToken
# Create your views hefrre.

class RegisterView(APIView):
    def post(self,request):
        data = request.data
        serializer = RegisterSerializer(data=data)
        if serializer.is_valid():
            user = serializer.save()
            return Response(
                {
                    "message" :"user created successfully",
                    "status":True
                },
                status = status.HTTP_201_CREATED
            )
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

    
class LoginView(APIView):
    def post(request):
        data = request.data 
        username = data.get('username')
        password = data.get('password')

        user = User.objects.filter(username = username).first()
        if user and user.check_password(password):
            refresh = RefreshToken.foruser(user)
            return Response({
                "access_token" : str(refresh.access_token),
                "refresh_token" :str(refresh)
            })
        return Response({"message":"credentials"}, status=status.HTTP_400_BAD_REQUEST)
        