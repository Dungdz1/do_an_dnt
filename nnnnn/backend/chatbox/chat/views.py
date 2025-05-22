from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Users
from .serializers import UserSerializer
from rest_framework import status
from rest_framework.views import APIView
from rest_framework import generics

# @api_view(['GET', 'POST'])

# def userlist(request):
#     if request.method == 'GET':
#         user = Users.objects.all() # select * from SinhVien # dung Orm
#         serializer = UserSerializer(user, many=True)
#         return Response(serializer.data)
#     elif request.method == 'POST':
#         serializer = UserSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    
# @api_view(['GET', 'PUT', 'DELETE'])

# def userdetail(request,pk):
#     try:
#         users = Users.objects.get(pk=pk)
#     except Users.DoesNotExist:
#         return Response(status=status.HTTP_404_NOT_FOUND)
#     if request.method == 'GET':
#         serializer = UserSerializer(users)
#         return Response(serializer.data)
#     elif request.method == 'PUT':
#         serializer = UserSerializer(users, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#     elif request.method == 'DELETE':
#         users.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)

class UserService(generics.ListCreateAPIView):
    queryset = Users.objects.all()
    serializer_class = UserSerializer

class UserDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Users.objects.all()
    serializers_class = UserSerializer
