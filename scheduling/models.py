
from django.db import models
from django.contrib.auth.models import User
class Slot(models.Model):
    STATUS_CHOICES = [
        ('available', 'Available'),
        ('pending', 'Pending Approval'),
        ('approved', 'Approved'),
        ('taken', 'Taken'),
    ]
    
    location = models.CharField(max_length=200)
    description = models.TextField()
    hourly_rate = models.DecimalField(max_digits=10, decimal_places=2)
    provider = models.CharField(max_length=200)
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='available')

    def __str__(self):
        return f"{self.description} at {self.location} from {self.start_time} to {self.end_time}"
    def is_signed_up(self, user):
        return Schedule.objects.filter(nurse=user, slot=self).exists()
        
from django.db import models
from django.contrib.auth.models import User
from django.core.validators import RegexValidator

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(null=True, blank=True)
    
    # Phone number field with a validator for the format
    phone_number = models.CharField(
        max_length=17, 
        blank=True
    )

    def __str__(self):
        return self.user.username


class Schedule(models.Model):
    STATUS_CHOICES = [
        ('pending', 'Pending Approval'),
        ('approved', 'Approved'),
        ('rejected', 'Rejected'),  # In case you want to allow explicit rejections
    ]

    nurse = models.ForeignKey(User, on_delete=models.CASCADE, related_name='schedules')
    slot = models.ForeignKey(Slot, on_delete=models.CASCADE, related_name='booked_slots')
    date = models.DateField()
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='pending')

    def __str__(self):
        return f"{self.nurse.username} scheduled for {self.slot.description} on {self.date}"