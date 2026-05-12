from rest_framework import serializers
from accounts.models import User

class UserSerializer(serializers.ModelSerializer):
    re_enter_password = serializers.CharField(write_only=True)
    class Meta:
        model = User
        fields = ['id', 'full_name', 'email', 'gender', 'phone_number', 'address', 'role', 'password', 're_enter_password', 'created_at']
        read_only_fields=["id","role","created_at"]
        extra_kwargs = {
            'password': {'write_only': True},
            're_enter_password': {'write_only': True}
        }

    def validate(self, attrs):
        if attrs['password'] != attrs['re_enter_password']:
            raise serializers.ValidationError("Passwords do not match.")
        return attrs
    
    def create(self, validated_data):
        re_enter_password=validated_data.pop('re_enter_password')
        user = User.objects.create(**validated_data)
        return user