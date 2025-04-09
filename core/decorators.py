from django.contrib.auth.decorators import user_passes_test
from django.http import HttpResponseRedirect

def student_required(view_func):
    def _decorator(request, *args, **kwargs):
        if not request.user.is_authenticated or not request.user.groups.filter(name='student').exists():
            return HttpResponseRedirect('/no-access/')
        return view_func(request, *args, **kwargs)
    return _decorator

def mentor_required(view_func):
    def _decorator(request, *args, **kwargs):
        if not request.user.is_authenticated or not request.user.groups.filter(name='mentor').exists():
            return HttpResponseRedirect('/no-access/')
        return view_func(request, *args, **kwargs)
    return _decorator

def admin_required(view_func):
    def _decorator(request, *args, **kwargs):
        if not request.user.is_authenticated or not request.user.groups.filter(name='admin').exists():
            return HttpResponseRedirect('/no-access/')
        return view_func(request, *args, **kwargs)
    return _decorator