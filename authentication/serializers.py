from rest_framework import serializers
from .models import CustomUser

class UserSerializer(serializers.ModelSerializer):
    nameEmail = serializers.SerializerMethodField()

    def get_nameEmail(self, obj):
        return f"{obj.first_name} {obj.last_name} ({obj.email})"

    class Meta:
        model = CustomUser
        fields = ['nameEmail', 'username', 'email']
