from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.response import Response
from .serializers import TaskManagementSerializer
from .models import TaskManagementModel
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAuthenticated
from django.shortcuts import get_object_or_404

class TaskManagementView(viewsets.ViewSet):
    permission_classes = [IsAuthenticated]
    authentication_classes = [JWTAuthentication]

    def create(self, request):
        serializer = TaskManagementSerializer(data=request.data)
        if serializer.is_valid():
            # Assign the currently authenticated user as the task's creator
            serializer.save(created_by=request.user)
            return Response(data=serializer.data, status=201)
        return Response(data=serializer.errors, status=400)

    def list(self, request):
        user = request.user  # Get the authenticated user
        queryset = TaskManagementModel.objects.filter(created_by=user)
        serializer = TaskManagementSerializer(queryset, many=True)
        return Response(data=serializer.data, status=200)
    

    def retrieve(self, request, pk=None):
        user = request.user
        queryset = TaskManagementModel.objects.filter(created_by=user)
        taskManagement = get_object_or_404(queryset, pk=pk)
        serializer = TaskManagementSerializer(taskManagement)
        return Response(data=serializer.data, status=200)

    def destroy(self, request, pk=None):
        user = request.user
        queryset = TaskManagementModel.objects.filter(created_by=user)
        taskManagement = get_object_or_404(queryset, pk=pk)
        taskManagement.delete()
        return Response(data="Data Deleted", status=205)
    
    def update(self, request, pk=None):
        user = request.user
        queryset = TaskManagementModel.objects.filter(created_by=user)
        taskManagement = get_object_or_404(queryset, pk=pk)
        serializer = TaskManagementSerializer(data=request.data, instance=taskManagement)
        if serializer.is_valid():
            serializer.save(created_by=user)
            return Response(data=serializer.data, status=204)
        return Response(data=serializer.errors, status=400)

