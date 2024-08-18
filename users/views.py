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

class MyProfileView(RetrieveAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = ProfileSerializer

    def get_object(self):
        return Profile.objects.get(user_id=self.request.user)


class UpdateMyProfileView(UpdateAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = ProfileSerializer
    def get_object(self):
        print(self.request.user)
        return Profile.objects.get(user_id=self.request.user.pk)
