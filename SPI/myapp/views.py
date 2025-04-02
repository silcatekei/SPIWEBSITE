import os
from django.conf import settings
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib import messages
from django.core.files.storage import default_storage, FileSystemStorage
from django.core.exceptions import ValidationError
from django.utils.text import slugify
from .models import Application, ContactMessage
from .forms import ApplicationForm, ContactForm
from django.utils import timezone
from django.utils.crypto import get_random_string


# --- Basic Page Views ---
def home(request):
    return render(request, 'myapp/home.html')

def about(request):
    return render(request, 'myapp/about.html')

def mission(request):
    return render(request, 'myapp/mv.html')

def history(request):
    return render(request, 'myapp/hist.html')

def admissions(request):
    return render(request, 'admissions.html')

def requirements(request):
    return render(request, 'myapp/req.html')

def application_process(request):
    return render(request, 'myapp/appprocess.html')

def gallery(request):
    return render(request, 'myapp/gallery.html')

def academics(request):
    return render(request, 'myapp/academics.html')

def programs(request):
    return render(request, 'myapp/programs.html')

def faculty(request):
    return render(request, 'myapp/faculty.html')

def calendar(request):
    return render(request, 'myapp/acc_calendar.html')

def contact(request):
    return render(request, 'myapp/contact.html')

def quick_links(request):
    return render(request, 'myapp/quick_links.html')

def spiantipolo(request):
    return render(request, 'myapp/spiantipolo.html')

def spiqc(request):
    return render(request, 'myapp/spiqc.html')

def spicabanatuan(request):
    return render(request, 'myapp/cabanatuan.html')

def spiangeles(request):
    return render(request, 'myapp/angeles.html')

 #gallery options codes



def upload_image(request):
    galleries_path = os.path.join(settings.BASE_DIR, 'myapp', 'static', 'images', 'galleries')  # Correct path to static/images/galleries
    
    # Ensure that the folder exists
    if not os.path.exists(galleries_path):
        os.makedirs(galleries_path)

    # Get the list of galleries in the 'galleries' folder
    galleries = [f.name for f in os.scandir(galleries_path) if f.is_dir()]

    if request.method == 'POST':
        gallery_name = request.POST.get('gallery')  # Get the selected gallery from the form
        new_gallery_name = request.POST.get('new_gallery_name')  # Get the new gallery name from the form
        
        if 'image' not in request.FILES:
            messages.error(request, "No image selected.")
            return redirect('upload_image')

        uploaded_file = request.FILES['image']

        # If no gallery is selected and a new name is provided, create a custom folder with the new name
        if not gallery_name and new_gallery_name:
            gallery_name = new_gallery_name  # Use the new gallery name provided by the user
            custom_gallery_path = os.path.join(galleries_path, gallery_name)
            
            # Create the gallery folder if it doesn't exist
            if not os.path.exists(custom_gallery_path):
                os.makedirs(custom_gallery_path)
            gallery_path = custom_gallery_path
            messages.info(request, f"New gallery '{gallery_name}' created.")
        elif not gallery_name:
            # If no gallery name is provided, create a random gallery name
            gallery_name = get_random_string(8)  # Create a unique folder name
            custom_gallery_path = os.path.join(galleries_path, gallery_name)
            
            # Create the gallery folder if it doesn't exist
            if not os.path.exists(custom_gallery_path):
                os.makedirs(custom_gallery_path)
            gallery_path = custom_gallery_path
            messages.info(request, f"New gallery '{gallery_name}' created.")
        else:
            gallery_path = os.path.join(galleries_path, gallery_name)

            # Check if the directory exists, and if not, create it
            if not os.path.exists(gallery_path):
                os.makedirs(gallery_path)

        # Create a unique filename to prevent collisions
        unique_filename = get_random_string(8) + os.path.splitext(uploaded_file.name)[1]
        
        # Save the uploaded file to the correct location
        file_storage = FileSystemStorage(location=gallery_path)
        filename = file_storage.save(unique_filename, uploaded_file)

        # Show a success message
        messages.success(request, f"Image uploaded successfully to '{gallery_name}' gallery.")

        return redirect('upload_image')  # Redirect after successful upload

    return render(request, 'upload_image.html', {'galleries': galleries})

def get_gallery_folders():
    gallery_folder_path = os.path.join(settings.MEDIA_ROOT,  'galleries')
    if not os.path.exists(gallery_folder_path):
        os.makedirs(gallery_folder_path)
    
    return [f for f in os.listdir(gallery_folder_path) if os.path.isdir(os.path.join(gallery_folder_path, f))]

def upload_folder(request):
    if request.method == 'POST' and 'images' in request.FILES:
        uploaded_images = request.FILES.getlist('images')  # Get all uploaded images
        gallery_name = request.POST.get('gallery_name')  # Get the selected gallery name
        gallery_path = os.path.join(settings.BASE_DIR, 'myapp', 'static', 'images', 'galleries', gallery_name)
        
        if not os.path.exists(gallery_path):
            os.makedirs(gallery_path)

        fs = FileSystemStorage(location=gallery_path)

        for image in uploaded_images:
            unique_filename = get_random_string(8) + os.path.splitext(image.name)[1]
            fs.save(unique_filename, image)  # Save each image with a unique name

        messages.success(request, f"Images uploaded successfully to '{gallery_name}' gallery.")
        return redirect('upload_image')  # Redirect back after successful upload
    
    return render(request, 'upload_folder.html')



def upload_gallery_image(request):
    if request.method == 'POST' and request.FILES.get('gallery_image'):
        image = request.FILES['gallery_image']
        gallery_name = request.POST.get('gallery_name')  # Get the gallery name from the form
        gallery_path = os.path.join(settings.BASE_DIR, 'myapp', 'static', 'images', 'galleries', gallery_name)
        
        if not os.path.exists(gallery_path):
            os.makedirs(gallery_path)
        
        fs = FileSystemStorage(location=gallery_path)
        unique_filename = get_random_string(8) + os.path.splitext(image.name)[1]
        fs.save(unique_filename, image)

        messages.success(request, f"Image uploaded successfully to '{gallery_name}' gallery.")
        return redirect('admin_home')  # Redirect back after successful upload

    return render(request, 'admin_base.html')

import os
from django.conf import settings

def gallery(request):
    galleries = {}
    
    # Path to the 'galleries' folder where images are stored
    gallery_path = os.path.join(settings.BASE_DIR, 'myapp', 'static', 'images', 'galleries')

    if os.path.exists(gallery_path):  # Check if directory exists
        for folder in os.listdir(gallery_path):
            folder_path = os.path.join(gallery_path, folder)
            if os.path.isdir(folder_path):  # Ensure it's a folder
                images = [
                    f'images/galleries/{folder}/{img}' 
                    for img in os.listdir(folder_path) 
                    if img.endswith(('png', 'jpg', 'jpeg', 'gif'))
                ]
                
                if images:
                    galleries[folder] = images  # Store images by folder

    return render(request, 'myapp/gallery.html', {'galleries': galleries})



# --- Apply Online View ---
def apply_online(request):
    if request.method == 'POST':
        form = ApplicationForm(request.POST)
        if form.is_valid():
            application = form.save() # Save the form
            messages.success(request, "Application submitted successfully!")
            return redirect('application_confirmation', application_id=application.id)
        else:
            messages.error(request, "Please correct the errors below.")

    else:
        form = ApplicationForm()

    return render(request, 'myapp/apply_online.html', {'form': form})

def application_confirmation(request, application_id):
    application = get_object_or_404(Application, pk=application_id) # get_object_or_404 if does not exist will display a 404 instead of displaying nothing
    return render(request, 'myapp/application_confirmation.html', {'application': application})

# --- Login Views ---
def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(request, username=username, password=password) # Authentication with request argument

            if user is not None:
                login(request, user)
                messages.success(request, f"Welcome, {username}!")  # Add success message on login
                return redirect('student_dashboard')
            else:
                messages.error(request, 'Invalid username or password.')
        else:
            messages.error(request, 'Invalid username or password.')

    else:
        form = AuthenticationForm()

    return render(request, 'login.html', {'form': form}) # Updated path

@login_required(login_url='/login/')
def student_dashboard(request):
    context = {'user': request.user}
    return render(request, 'student_dashboard.html', context)

# --- Admin Views ---
def is_admin(user):
    return user.is_staff and user.is_superuser # checks if the user is both of the condition

@login_required
@user_passes_test(is_admin) # checks user is an admin before accessing
def admin_dashboard(request):
    applications = Application.objects.all().order_by('-application_date')
    application_count = Application.objects.count()
    accepted_count = Application.objects.filter(status='accepted').count()
    rejected_count = Application.objects.filter(status='rejected').count()
    pending_count = Application.objects.filter(status='pending').count()

    context = {
        'applications': applications,
        'application_count': application_count,
        'accepted_count': accepted_count,
        'rejected_count': rejected_count,
        'pending_count': pending_count,
    }
    return render(request, 'admin_dashboard.html', context)

def admin_login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(request, username=username, password=password)

            if user is not None:
                login(request, user)

                if is_admin(user):
                    messages.success(request, f"Admin {username} logged in successfully.") # message to the user
                    return redirect('admin_home')
                else:
                    logout(request)
                    messages.error(request, "You do not have admin privileges.")
                    return redirect('login')  # or redirect to some unauthorized page
            else:
                messages.error(request, 'Invalid username or password')
        else:
            messages.error(request, 'Invalid username or password')

    else:
        form = AuthenticationForm() # if there is no data

    return render(request, 'admin_login.html', {'form': form}) # renders the form

@login_required
@user_passes_test(is_admin)
def accept_application(request, application_id):
    application = get_object_or_404(Application, pk=application_id)
    application.status = 'accepted' # update application
    application.save() # save it
    messages.success(request, f"Application for {application.name} accepted.") # send a message to the screen
    return redirect('admin_dashboard')

@login_required
@user_passes_test(is_admin)
def reject_application(request, application_id):
    application = get_object_or_404(Application, pk=application_id) # application id check
    application.status = 'rejected' # changes the status to reject in case that exist
    application.save()
    messages.success(request, f"Application for {application.name} rejected.")#message to the screen
    return redirect('admin_dashboard') # returns to the dashboard
@login_required
@user_passes_test(is_admin)
def admin_home(request):
    # Application Counts
    application_count = Application.objects.count()
    accepted_count = Application.objects.filter(status='accepted').count()
    rejected_count = Application.objects.filter(status='rejected').count()
    pending_count = Application.objects.filter(status='pending').count()
    message_count = ContactMessage.objects.count()

    # Recent Contact Messages
    recent_messages = ContactMessage.objects.order_by('-timestamp')[:5]  # Get the 5 most recent messages

    context = {
        'application_count': application_count,
        'accepted_count': accepted_count,
        'rejected_count': rejected_count,
        'pending_count': pending_count,
        'recent_messages': recent_messages,
        'message_count': message_count,  # Add contact messages to the context
    }
    return render(request, 'admin_home.html', context)

def application_confirmation(request, application_id):
    application = Application.objects.get(pk=application_id)

    context = {'application': application}
    return render(request, 'myapp/application_confirmation.html', context)

def edit_application(request, application_id):
    application = get_object_or_404(Application, pk=application_id)
    if request.method == 'POST':
        form = ApplicationForm(request.POST, instance=application)  # Use instance=application to update
        if form.is_valid():
            form.save()
            return redirect('admin_dashboard')  # Or wherever you want to redirect
    else:
        form = ApplicationForm(instance=application)
    return render(request, 'myapp/edit_application.html', {'form': form, 'application': application})

def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            # Save the message to the database
            contact_message = ContactMessage(
                name=form.cleaned_data['name'],
                email=form.cleaned_data['email'],
                message=form.cleaned_data['message']
            )
            contact_message.save()

            # Optionally, send an email to the admin

            # Redirect to a success page or back to the contact form
            return redirect('contact_success')
    else:
        form = ContactForm()
    return render(request, 'myapp/contact.html', {'form': form})

def contact_success(request):
    return render(request, 'myapp/contact_success.html')  # Create this template

def contact_messages(request):
    """Displays a list of contact form messages."""
    # Application Counts (same as in admin_home)
    application_count = Application.objects.count()
    accepted_count = Application.objects.filter(status='accepted').count()
    rejected_count = Application.objects.filter(status='rejected').count()
    pending_count = Application.objects.filter(status='pending').count()

    messages = ContactMessage.objects.order_by('-timestamp')  # Order by newest first

    # Fetch total message count
    message_count = ContactMessage.objects.count()

    context = {
        'messages': messages,
        'application_count': application_count,
        'accepted_count': accepted_count,
        'rejected_count': rejected_count,
        'pending_count': pending_count,
        'message_count': message_count,  # Add message count to the context
    }
    return render(request, 'contact_messages.html', context)
def resolve_message(request, message_id):
    """Marks a contact message as resolved."""
    message = get_object_or_404(ContactMessage, pk=message_id)
    message.status = 'resolved' #Set the status resolve or delete in table
    message.save()
    return redirect('contact_messages')  # Redirect back to the messages list

def delete_message(request, message_id):
    """Deletes a contact message."""
    message = get_object_or_404(ContactMessage, pk=message_id)
    message.delete()
    return redirect('contact_messages')  # Redirect back to the messages list