from django.contrib.auth.models import User


def isAdmin(user):
    user = User.objects.get(pk=user.pk)
    if user.role == 'Admin':
        return True
    return False

def isCurator(user):
    user = User.objects.get(pk=user.pk)
    if user.role == 'Loyiha kuratori':
        return True
    return False

def isManager(user):
    user = User.objects.get(pk=user.pk)
    if user.role == 'Loyiha menejeri':
        return True
    return False

def isProjectOwner(user):
    user = User.objects.get(pk=user.pk)
    if user.role == 'Loyiha egasi':
        return True
    return False

def isSimpleUser(user):
    user = User.objects.get(pk=user.pk)
    if user.role == 'Oddiy':
        return True
    return False