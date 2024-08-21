from django.urls import path
from .views import ProjectsListView,CreateProjectView,UpdateProjectView,DeleteProjectView


urlpatterns = [
    path('all/',ProjectsListView.as_view(),name='all-projects'),
    path('create/',CreateProjectView.as_view(),name='create-project'),
    path('update/<pk>',UpdateProjectView.as_view(),name='update-project'),
    path('delete/<pk>',DeleteProjectView.as_view(),name='delete-project'),
]