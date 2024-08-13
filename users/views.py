from rest_framework.exceptions import PermissionDenied
from rest_framework.views import APIView
from rest_framework.generics import ListAPIView, RetrieveAPIView, CreateAPIView, UpdateAPIView, DestroyAPIView
from .models import Profile
from rest_framework.permissions import IsAuthenticated

from .permissions.permissions import IsProfileOwner
from .serializers import ProfileSerializer


class ProfilesView(ListAPIView):
    queryset = Profile.objects.all()
    permission_classes = [IsAuthenticated]
    serializer_class = ProfileSerializer


class UpdateProfile(UpdateAPIView):
    queryset = Profile.objects.all()
    permission_classes = [IsAuthenticated, IsProfileOwner]
    serializer_class = ProfileSerializer


class DeleteProfile(DestroyAPIView):
    queryset = Profile.objects.all()
    permission_classes = [IsAuthenticated, IsProfileOwner]
    serializer_class = ProfileSerializer


class ProfileView(RetrieveAPIView):
    queryset = Profile.objects.all()
    permission_classes = [IsAuthenticated]
    serializer_class = ProfileSerializer
