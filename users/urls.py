from django.urls import path
from .views import ProfilesView,UpdateProfile,DeleteProfile,ProfileView,MyProfileView,UpdateMyProfileView

urlpatterns = [
    path('my-profile/', MyProfileView.as_view(), name='my-profile'),
    path('my-profile/update', UpdateMyProfileView.as_view(), name='my-profile-update'),
    path('<pk>', ProfileView.as_view(), name='profile'),
    path('all/', ProfilesView.as_view(), name='profiles'),
    path('update/<pk>', UpdateProfile.as_view(), name='update-profile'),
    path('delete/<pk>', DeleteProfile.as_view(), name='delete-profile'),

]
