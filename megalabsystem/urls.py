from django.contrib import admin
from django.urls import path
from django.views.generic import TemplateView
from django.contrib.auth.views import LogoutView
from django.contrib.auth.decorators import login_required
from core.decorators import student_required, mentor_required, admin_required
from core.views import dashboard, handle_no_access, CustomLoginView, administration

urlpatterns = [
    path('admin/', admin.site.urls),  # Стандартная админ-панель Django
    path('login/', CustomLoginView.as_view(template_name='core/login.html'), name='login'),
    path('logout/', LogoutView.as_view(next_page='login'), name='logout'),
    path('', login_required(dashboard), name='dashboard'),
    path('student/', student_required(TemplateView.as_view(template_name='core/student.html')), name='student_dashboard'),
    path('mentor/', mentor_required(TemplateView.as_view(template_name='core/mentor.html')), name='mentor_dashboard'),
    path('administration/', administration, name='administration'),  # Кастомная админка
    path('no-access/', handle_no_access, name='no_access'),
]