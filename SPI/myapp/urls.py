# myapp/urls.py
from django.urls import path
from django.contrib.auth import views as auth_views
from . import views  # Import the whole module
from .views import upload_gallery_image
from django.conf import settings
from django.conf.urls.static import static
from .views import custom_logout_view
from django.urls import path
from .views import custom_logout  




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
    path('home/', views.admin_home, name='admin_home'),
    path('admin_dashboard/', views.admin_dashboard, name='admin_dashboard'), #URL for the admin dashboard
    path('confirmation/<int:application_id>/', views.application_confirmation, name='application_confirmation'),
    path('accept_application/<int:application_id>/', views.accept_application, name='accept_application'),
    path('reject_application/<int:application_id>/', views.reject_application, name='reject_application'),
    path('logout/', auth_views.LogoutView.as_view(next_page='login'), name='logout'),
    path('spiantipolo/', views.spiantipolo, name='spiantipolo'),
    path('spiqc/', views.spiqc, name='spiqc'),
    path('spicabanatuan/', views.spicabanatuan, name='spicabanatuan'),
    path('spiangeles/', views.spiangeles, name='spiangeles'),
    path('application/edit/<int:application_id>/', views.edit_application, name='edit_application'),
    path('admin/upload-gallery/', upload_gallery_image, name='upload_gallery_image'),
    path('contact/', views.contact, name='contact'),
    path('contact/success/', views.contact_success, name='contact_success'),
    path('admin_login', views.contact_messages, name='contact_messages'),
    path('resolve/<int:message_id>/', views.resolve_message, name='resolve_message'),
    path('delete/<int:message_id>/', views.delete_message, name='delete_message'),
    path('upload-folder/', views.upload_folder, name='upload_folder'),
    path('gallery/', views.gallery, name='view_gallery'),
    path('upload-image/', views.upload_image, name='upload_image'),
    path('logout/', custom_logout, name='logout'),
    path('admin_login/', views.admin_login_view, name='admin_login'),  # Admin login URL
    path('delete_image/<str:gallery_name>/<str:image_name>/', views.delete_image, name='delete_image'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)