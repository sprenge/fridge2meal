from django.http import HttpResponseRedirect
from django.shortcuts import render
from food.forms import UploadExcelForm

# Imaginary function to handle an uploaded file.
# from somewhere import handle_uploaded_file


def upload_file(request):
    if request.method == 'POST':
        form = UploadExcelForm(request.POST, request.FILES)
        if form.is_valid():
            # handle_uploaded_file(request.FILES['file'])
            return HttpResponseRedirect('/success/url/')
    else:
        form = UploadExcelForm()
    return render(request, 'upload.html', {'form': form})
