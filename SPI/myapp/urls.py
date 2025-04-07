from django.urls import path
from django.contrib.auth import views as auth_views
from django.conf import settings
from django.conf.urls.static import static
from . import views
from .views import upload_gallery_image, custom_logout
from .views import add_class

urlpatterns = [
    # Public Pages
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('mission/', views.mission, name='mission'),
    path('history/', views.history, name='history'),
    path('admissions/', views.admissions, name='admissions'),
    path('requirements/', views.requirements, name='requirements'),
    path('application_process/', views.application_process, name='application_process'),
    path('apply/', views.apply_online, name='apply_online'),

    # SPI Campuses
    path('spiantipolo/', views.spiantipolo, name='spiantipolo'),
    path('spiqc/', views.spiqc, name='spiqc'),
    path('spicabanatuan/', views.spicabanatuan, name='spicabanatuan'),
    path('spiangeles/', views.spiangeles, name='spiangeles'),

    # Academic Info
    path('academics/', views.academics, name='academics'),
    path('programs/', views.programs, name='programs'),
    path('faculty/', views.faculty, name='faculty'),
    path('calendar/', views.calendar, name='calendar'),

    # Contact & Messages
    path('contact/', views.contact, name='contact'),
    path('contact/success/', views.contact_success, name='contact_success'),
    path('messages/', views.contact_messages, name='contact_messages'),
    path('resolve/<int:message_id>/', views.resolve_message, name='resolve_message'),
    path('delete/<int:message_id>/', views.delete_message, name='delete_message'),

    # Gallery
    path('gallery/', views.gallery, name='gallery'),
    path('admin/upload-gallery/', upload_gallery_image, name='upload_gallery_image'),
    path('upload-image/', views.upload_image, name='upload_image'),
    path('upload-folder/', views.upload_folder, name='upload_folder'),
    path('delete_image/<str:gallery_name>/<str:image_name>/', views.delete_image, name='delete_image'),


    # User Auth & Dashboard
    path('login/', views.login_view, name='login'),
    path('logout/', custom_logout, name='logout'),
    path('admin_login/', views.admin_login_view, name='admin_login'),
    path('home/', views.admin_home, name='admin_home'),
    path('admin_dashboard/', views.admin_dashboard, name='admin_dashboard'),
    path('manage-classes/', views.manage_classes, name='manage_classes'),
    path('add-class/', add_class, name='add_class'),
    path('assign_class_teacher/', views.assign_class_teacher, name='assign_class_teacher'),
    path('assign_class_student/', views.assign_class_student, name='assign_class_student'),
    path('add_delete_admin/', views.add_delete_admin, name='add_delete_admin'),
    path('teacher_dashboard/', views.teacher_dashboard, name='teacher_dashboard'),
    path('student_dashboard/', views.student_dashboard, name='student_dashboard'),
    path('teacher/profile/', views.teacher_profile, name='teacher_profile'),
    path('teacher/profile/update/', views.update_teacher_profile, name='update_teacher_profile'),
    path('delete-class/<int:class_id>/', views.delete_class, name='delete_class'),
    
    # Applications
    path('confirmation/<int:application_id>/', views.application_confirmation, name='application_confirmation'),
    path('accept_application/<int:application_id>/', views.accept_application, name='accept_application'),
    path('reject_application/<int:application_id>/', views.reject_application, name='reject_application'),
    path('application/edit/<int:application_id>/', views.edit_application, name='edit_application'),

    # Quick Links
    path('quick-links/', views.quick_links, name='quick_links'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
