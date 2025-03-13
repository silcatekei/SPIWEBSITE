from django.shortcuts import render, redirect
from .forms import ApplicationForm

def home(request):
    return render(request, 'myapp/home.html')  # Create home.html in myapp/templates/myapp/

def about(request):
    return render(request, 'myapp/about.html')

def mission(request):
    return render(request, 'myapp/mission.html')

def history(request):
    return render(request, 'myapp/history.html')

def admissions(request):
    return render(request, 'myapp/admissions.html')

def requirements(request):
    return render(request, 'myapp/requirements.html')

def application_process(request):
    return render(request, 'myapp/application_process.html')

def tuition(request):
    return render(request, 'myapp/tuition.html')

def academics(request):
    return render(request, 'myapp/academics.html')

def programs(request):
    return render(request, 'myapp/programs.html')

def faculty(request):
    return render(request, 'myapp/faculty.html')

def calendar(request):
    return render(request, 'myapp/calendar.html')

def contact(request):
    return render(request, 'myapp/contact.html')

def quick_links(request):
    return render(request, 'myapp/quick_links.html')

def apply_online(request):
    if request.method == 'POST':
        form = ApplicationForm(request.POST)
        if form.is_valid():
            form.save()  # Now this will work
            return redirect('home')
    else:
        form = ApplicationForm()
    return render(request, 'myapp/apply_online.html', {'form': form})