from django.shortcuts import render, redirect, get_object_or_404
from .forms import ApplicationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib import messages  # Always good to use messages for feedback
from .models import Application  # Import your Application model
from django.utils import timezone

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
    application_count = Application.objects.count()
    accepted_count = Application.objects.filter(status='accepted').count()
    rejected_count = Application.objects.filter(status='rejected').count()
    pending_count = Application.objects.filter(status='pending').count()

    context = {
        'application_count': application_count,
        'accepted_count': accepted_count,
        'rejected_count': rejected_count,
        'pending_count': pending_count,
    }
    return render(request, 'admin_home.html',context)

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