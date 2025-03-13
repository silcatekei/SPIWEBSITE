# myapp/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),  # Home page
    path('about/', views.about, name='about'),
    path('mission/', views.mission, name='mission'),
    path('history/', views.history, name='history'),
    path('admissions/', views.admissions, name='admissions'),
    path('requirements/', views.requirements, name='requirements'),
    path('application_process/', views.application_process, name='application_process'),
    path('tuition/', views.tuition, name='tuition'),
    path('academics/', views.academics, name='academics'),
    path('programs/', views.programs, name='programs'),
    path('faculty/', views.faculty, name='faculty'),
    path('calendar/', views.calendar, name='calendar'),
    path('contact/', views.contact, name='contact'),
    path('quick-links/', views.quick_links, name='quick_links'),
    path('apply/', views.apply_online, name='apply_online'),
]