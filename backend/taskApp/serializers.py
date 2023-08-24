from rest_framework import serializers
from .models import TaskManagementModel


class TaskManagementSerializer(serializers.ModelSerializer):
    class Meta:
        model = TaskManagementModel
        fields = '__all__'