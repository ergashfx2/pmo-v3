from django.contrib.auth.models import User


def isAdmin(user):
    user = User.objects.get(pk=user.pk)
    return user.role == 'Admin'

def isCurator(user):
    user = User.objects.get(pk=user.pk)
    return user.role == 'Loyiha kuratori'

def isManager(user):
    user = User.objects.get(pk=user.pk)
    return user.role == 'Loyiha menejeri'

def isProjectOwner(user):
    user = User.objects.get(pk=user.pk)
    return user.role == 'Loyiha egasi'

def isSimpleUser(user):
    user = User.objects.get(pk=user.pk)
    return user.role == 'Oddiy'