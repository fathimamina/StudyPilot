from django import forms 
from .models import Plan 

class PlanForm(forms.ModelForm):
    class Meta:
        model = Plan
        fields = [
            'module',
            'start_date',
            'deadline',
            'available_hours_per_day',
        ]