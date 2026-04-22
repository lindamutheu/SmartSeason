from .models import User, Field, Update
from rest_framework import serializers

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = [
            'id',
            'username',
            'first_name',
            'last_name',
            'email',
            'role',
            'employee_id',
            'region',
        ]



class FieldSerializer(serializers.ModelSerializer):
    status = serializers.ReadOnlyField()

    class Meta:
        model = Field
        fields = [
            'id',
            'crop_type',
            'planting_date',
            'stage',
            'status',
            'agent',
            'created_at',
            'updated_at',
        ]

class UpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Update
        fields = [
            'id',
            'field',
            'agent',
            'stage',
            'description',
            'created_at',
        ]

    