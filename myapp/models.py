# myapp/models.py
from django.db import models
from django.contrib.auth.models import User  # Import User if you link applications to user accounts

class Application(models.Model):
    STATUS_CHOICES = [
        ('pending', 'Pending'),
        ('accepted', 'Accepted'),
        ('rejected', 'Rejected'),
    ]

    name = models.CharField(max_length=100)  # Applicant's Name
    address = models.TextField()  # Applicant's Address
    email = models.EmailField()  # Applicant's Email
    contact_number = models.CharField(max_length=20)  # Applicant's Phone Number
    previous_school = models.CharField(max_length=100)  # Applicant's Previous School
    application_date = models.DateTimeField(auto_now_add=True)  # Date of Application

    status = models.CharField(  # Status of Application
        max_length=20,
        choices=STATUS_CHOICES,
        default='pending',
        help_text="Status of the application (Pending, Accepted, Rejected)"
    )

    # Optional: Link to the User model if applications are associated with user accounts
    applicant = models.ForeignKey(User, null=True, blank=True, on_delete=models.SET_NULL, related_name='applications')  # Optional
    notes = models.TextField(blank=True)

    def __str__(self):
        return f"{self.name} ({self.email}) - {self.get_status_display()}"

    class Meta:  # Add Meta class for ordering and display name
        verbose_name = "Application"  # Custom name
        verbose_name_plural = "Applications"  # Custom plural name
        ordering = ['application_date']  # Default ordering of entries

class ContactMessage(models.Model):
    STATUS_CHOICES = (
        ('pending', 'Pending'),
        ('resolved', 'Resolved'),
    )

    name = models.CharField(max_length=100)
    email = models.EmailField()
    message = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='pending')

    def __str__(self):
        return f"Message from {self.name} ({self.email})"
    

class Subject(models.Model):
    code = models.CharField(max_length=20, unique=True)
    name = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return f"{self.code} - {self.name}"

from django.db import models

class Class(models.Model):  # or whatever your class model is named
    subject_code = models.CharField(max_length=20)
    subject_name = models.CharField(max_length=100)
    schedule = models.CharField(max_length=50)
    duration = models.PositiveIntegerField()
    room = models.CharField(max_length=20)

    def __str__(self):
        return f"{self.subject_name} ({self.subject_code})"



class TeacherProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=100)
    middle_name = models.CharField(max_length=100, blank=True)
    address = models.TextField(default="Not Provided")  # Default value for the new field

    def __str__(self):
        return self.user.username

class ClassAssignment(models.Model):
    assigned_class = models.ForeignKey(Class, on_delete=models.CASCADE)
    teacher = models.ForeignKey(TeacherProfile, on_delete=models.CASCADE)
    students = models.ManyToManyField(User, related_name='student_classes')

    def __str__(self):
        return f"{self.assigned_class} - {self.teacher}"
    
class Grade(models.Model):
    student = models.ForeignKey('auth.User', on_delete=models.CASCADE)  # Assuming User is the student
    course_name = models.CharField(max_length=255)
    grade = models.CharField(max_length=10)

    def __str__(self):
        return f"{self.student.username} - {self.course_name}: {self.grade}"
    
class Announcement(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    date_posted = models.DateTimeField(auto_now_add=True)  # <- this line used to be `created_at`