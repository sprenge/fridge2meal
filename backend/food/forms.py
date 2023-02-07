from django import forms
import os
from django import forms


class UploadExcelForm(forms.Form):
    file = forms.FileField()
