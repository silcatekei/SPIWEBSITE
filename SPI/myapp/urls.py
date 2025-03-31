# myapp/urls.py
from django.urls import path
from django.contrib.auth import views as auth_views
from . import views  # Import the whole module


urlpatterns = [
    path('', views.home, name='home'),  # Home page
    path('about/', views.about, name='about'),
    path('mission/', views.mission, name='mission'),
    path('history/', views.history, name='history'),
    path('admissions/', views.admissions, name='admissions'),
    path('requirements/', views.requirements, name='requirements'),
    path('application_process/', views.application_process, name='application_process'),
    path('gallery/', views.gallery, name='gallery'),
    path('academics/', views.academics, name='academics'),
    path('programs/', views.programs, name='programs'),
    path('faculty/', views.faculty, name='faculty'),
    path('calendar/', views.calendar, name='calendar'),
    path('contact/', views.contact, name='contact'),
    path('quick-links/', views.quick_links, name='quick_links'),
    path('apply/', views.apply_online, name='apply_online'),
    path('login/', views.login_view, name='login'),
    path('dashboard/', views.student_dashboard, name='student_dashboard'),
    path('logout/', auth_views.LogoutView.as_view(next_page='/login/'), name='logout'),
    path('home/', views.admin_home, name='admin_home'),
    path('admin_dashboard/', views.admin_dashboard, name='admin_dashboard'), #URL for the admin dashboard
    path('admin_login/', views.admin_login_view, name='admin_login'), #admin login url
    path('confirmation/<int:application_id>/', views.application_confirmation, name='application_confirmation'),
    path('accept_application/<int:application_id>/', views.accept_application, name='accept_application'),
    path('reject_application/<int:application_id>/', views.reject_application, name='reject_application'),
    path('logout/', auth_views.LogoutView.as_view(next_page='login'), name='logout'),
    path('spiantipolo/', views.spiantipolo, name='spiantipolo'),
    path('spiqc/', views.spiqc, name='spiqc'),
    path('spicabanatuan/', views.spicabanatuan, name='spicabanatuan'),
    path('spiangeles/', views.spiangeles, name='spiangeles'),
    path('application/edit/<int:application_id>/', views.edit_application, name='edit_application'),
]