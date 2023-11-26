from django import forms
from .models import Schedule, Profile

class ScheduleForm(forms.ModelForm):
    class Meta:
        model = Schedule
        fields = ['slot', 'date']
        widgets = {
            'date': forms.DateInput(attrs={'type': 'date'}),
        }

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['bio', 'phone_number']  # Include the fields you want to be editable
