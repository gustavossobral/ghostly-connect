from django import forms
from . import models

class ReportForm(forms.ModelForm):
    class Meta:
        model = models.Report
        fields = ['motivo']