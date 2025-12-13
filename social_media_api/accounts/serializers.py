from rest_framework import serializers
from django.contrib.auth import authenticate
from rest_framework.authtoken.models import Token
from .models import CustomUser
from django.contrib.auth import get_user_model
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from django.shortcuts import get_object_or_404


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['id', 'username', 'email', 'first_name', 'last_name', 'bio', 'profile_picture']

User = get_user_model()

class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ['username', 'email', 'password', 'first_name', 'last_name', 'bio']

    def create(self, validated_data):
        password = validated_data.pop('password')

        # This automatically hashes password + handles custom user correctly
        user = get_user_model().objects.create_user(
            password=password,
            **validated_data
        )

        Token.objects.create(user=user)
        return user

class LoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField(write_only=True)

    def validate(self, data):
        user = authenticate(username=data['username'], password=data['password'])
        if not user:
            raise serializers.ValidationError("Invalid credentials")
        data['user'] = user
        return data
    
class FollowUserAPIView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request, user_id):
        target_user = get_object_or_404(User, id=user_id)

        if target_user == request.user:
            return Response(
                {"error": "You cannot follow yourself"},
                status=400
            )

        # YOU follow THEM → YOU are added to THEIR followers
        target_user.followers.add(request.user)

        return Response(
            {"message": f"You are now following {target_user.username}"}
        )


class UnfollowUserAPIView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request, user_id):
        target_user = get_object_or_404(User, id=user_id)

        target_user.followers.remove(request.user)

        return Response(
            {"message": f"You unfollowed {target_user.username}"}
        )