from django.contrib.auth.views import LoginView as BaseLoginView
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.contrib.auth.models import Group
from django.contrib.auth import login  # Добавлен импорт login

@login_required
def dashboard(request):
    if request.user.is_superuser:
        return redirect('admin:index')  # Перенаправление суперпользователя на админ-панель Django
    user_groups = request.user.groups.values_list('name', flat=True)
    if 'student' in user_groups:
        return redirect('student_dashboard')
    elif 'mentor' in user_groups:
        return redirect('mentor_dashboard')
    elif 'admin' in user_groups:
        return redirect('administration')
    else:
        return render(request, 'core/no_access.html', {'message': 'У вас нет назначенной роли.'})

def handle_no_access(request):
    return render(request, 'core/no_access.html', {'message': 'У вас нет прав доступа к этому разделу.'})

@login_required
def administration(request):
    if not request.user.groups.filter(name='admin').exists():
        return render(request, 'core/no_access.html', {'message': 'У вас нет прав доступа к разделу администрации.'})
    return render(request, 'core/administration.html', {'message': 'Добро пожаловать в панель управления!'})

class CustomLoginView(BaseLoginView):
    template_name = 'core/login.html'

    def form_valid(self, form):
        """Успешная аутентификация"""
        self.request.session.flush()  # Очистка предыдущей сессии
        login(self.request, form.get_user())  # Теперь работает благодаря импорту
        return super().form_valid(form)  # Оставляем стандартное перенаправление

    def get_success_url(self):
        return '/'  # Перенаправление на дашборд после входа