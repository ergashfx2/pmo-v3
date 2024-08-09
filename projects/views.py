from django.shortcuts import render
from .serializers import ProjectSerializer, PhaseSerializer, TaskSerializer, DocumentSerializer, CommentSerializer
from rest_framework.permissions import IsAuthenticated, IsAdminUser, AllowAny
from .models import Project, Phase, Task, Document, Comment
from rest_framework.generics import CreateAPIView, UpdateAPIView, DestroyAPIView, RetrieveAPIView, ListAPIView


class ProjectsListView(ListAPIView):
    queryset = Project.objects.all()
    permission_classes = [AllowAny]
    serializer_class = ProjectSerializer





class CreateProjectView(CreateAPIView):
    queryset = Project.objects.all()
    permission_classes = [IsAuthenticated]
    serializer_class = ProjectSerializer


class UpdateProjectView(UpdateAPIView):
    queryset = Project.objects.all()
    permission_classes = [IsAuthenticated]
    serializer_class = ProjectSerializer


class DeleteProjectView(DestroyAPIView):
    queryset = Project.objects.all()
    permission_classes = [IsAuthenticated]
    serializer_class = ProjectSerializer


class ProjectView(RetrieveAPIView):
    queryset = Project.objects.all()
    permission_classes = [IsAuthenticated]
    serializer_class = ProjectSerializer


class PhaseView(RetrieveAPIView):
    queryset = Phase.objects.all()
    permission_classes = [IsAuthenticated]
    serializer_class = PhaseSerializer


class PhasesView(ListAPIView):
    queryset = Phase.objects.all()
    permission_classes = [IsAuthenticated]
    serializer_class = PhaseSerializer


class PhaseCreateView(CreateAPIView):
    queryset = Task.objects.all()
    permission_classes = [IsAuthenticated]
    serializer_class = PhaseSerializer

class PhaseUpdateView(UpdateAPIView):
    queryset = Phase.objects.all()
    permission_classes = [IsAuthenticated]
    serializer_class = PhaseSerializer


class PhaseDeleteView(DestroyAPIView):
    queryset = Phase.objects.all()
    permission_classes = [IsAuthenticated]
    serializer_class = PhaseSerializer


class TasksView(ListAPIView):
    queryset = Task.objects.all()
    permission_classes = [IsAuthenticated]
    serializer_class = TaskSerializer


class TaskCreateView(CreateAPIView):
    queryset = Task.objects.all()
    permission_classes = [IsAuthenticated]
    serializer_class = TaskSerializer


class TaskView(RetrieveAPIView):
    queryset = Task.objects.all()
    permission_classes = [IsAuthenticated]
    serializer_class = TaskSerializer


class TaskUpdateView(UpdateAPIView):
    queryset = Task.objects.all()
    permission_classes = [IsAuthenticated]
    serializer_class = TaskSerializer


class TaskDeleteView(DestroyAPIView):
    queryset = Task.objects.all()
    permission_classes = [IsAuthenticated]
    serializer_class = TaskSerializer


class CommentsView(ListAPIView):
    queryset = Comment.objects.all()
    permission_classes = [IsAuthenticated]
    serializer_class = CommentSerializer


class CommentView(RetrieveAPIView):
    queryset = Comment.objects.all()
    permission_classes = [IsAuthenticated]
    serializer_class = CommentSerializer


class CommentCreateView(CreateAPIView):
    queryset = Comment.objects.all()
    permission_classes = [IsAuthenticated]
    serializer_class = CommentSerializer


class CommentUpdateView(UpdateAPIView):
    queryset = Comment.objects.all()
    permission_classes = [IsAuthenticated]
    serializer_class = CommentSerializer


class CommentDeleteView(DestroyAPIView):
    queryset = Comment.objects.all()
    permission_classes = [IsAuthenticated]
    serializer_class = CommentSerializer
