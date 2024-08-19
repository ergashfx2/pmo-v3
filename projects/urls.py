from django.urls import path
from .views import ProjectsListView


urlpatterns = [
    path('all/',ProjectsListView.as_view(),name='all-projects'),
    path('create/',ProjectsListView.as_view(),name='all-projects'),
    path('update/<pk>',ProjectsListView.as_view(),name='all-projects'),
    path('<pk>/',ProjectsListView.as_view(),name='all-projects'),
    path('delete/<pk>',ProjectsListView.as_view(),name='all-projects')
]
