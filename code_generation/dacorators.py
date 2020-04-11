from django.http import HttpResponseRedirect
from django.urls import reverse


def roles_allowed(func):
    def wrap(request,*args,**kwargs):
        if request.user.is_superuser==True or request.user.is_staff==True:
            return func(request,*args,**kwargs)
        else:
            return HttpResponseRedirect(reverse('Login'))

    return wrap
