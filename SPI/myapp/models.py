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