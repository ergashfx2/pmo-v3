from rest_framework import status
from rest_framework.generics import ListAPIView, RetrieveAPIView, CreateAPIView, UpdateAPIView, DestroyAPIView
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Profile
from rest_framework.permissions import IsAuthenticated, IsAdminUser

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
        return Profile.objects.get(user_id=self.request.user.pk)


class BlockProfileView(APIView):
    permission_classes = [IsAuthenticated, IsAdminUser]
    def patch(self, request, pk):
        try:
            profile = Profile.objects.get(id=pk)
            profile.block()
            return Response(data={'status':200,'profile':pk,'message': "Profile has been blocked"}, status=status.HTTP_200_OK)
        except:
            return Response({'message': 'User not found'}, status=status.HTTP_404_NOT_FOUND)


class UnBlockProfileView(APIView):
    permission_classes = [IsAuthenticated, IsAdminUser]
    serializer_class = ProfileSerializer

    def patch(self, request, pk):
        try:
            profile = Profile.objects.get(id=pk)
            profile.unblock()
            return Response(data={'status':200,'profile':pk,'message': "Profile has been unblocked"}, status=status.HTTP_200_OK)
        except:
            return Response({'message': 'User not found'}, status=status.HTTP_404_NOT_FOUND)
