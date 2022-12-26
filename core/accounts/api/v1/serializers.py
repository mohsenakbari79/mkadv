from django.contrib.auth import get_user_model
from django.contrib.auth.password_validation import validate_password
from django.core import exceptions
from rest_framework import serializers

# Create your views here.



User = get_user_model()

class RegistrationSerializer(serializers.ModelSerializer):
    repeatpassword = serializers.CharField(max_length=255, write_only=True)

    class Meta:
        model = User
        fields = ["email", "password", "repeatpassword"]

    def validate(self, attrs):
        if attrs.get("password") != attrs.get("repeatpassword"):
            raise serializers.ValidationError({"detail": "passswords doesnt match"})

        try:
            validate_password(attrs.get("password"))
        except exceptions.ValidationError as e:
            raise serializers.ValidationError({"password": list(e.messages)})

        return super().validate(attrs)

    def create(self, validated_data):
        validated_data.pop("repeatpassword", None)
        return User.objects.create_user(**validated_data)
