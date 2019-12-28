from django.shortcuts import render
from django.http import HttpResponse
from django.core.files.storage import default_storage
from django.core.files.base import ContentFile


import os

# Create your views here.

def index(request):
    context = {}
    if request.method == 'POST':
        savefiles(request)
        return HttpResponse(context)

    return render(request, 'ModalDZ/index.html', context)

def savefiles(request):
    # A way to access Django-files format
    uploaded_files = [request.FILES.get('file[%d]' % i)
                     for i in range(0, len(request.FILES))]

    # saving onto the media folder
    file_path = os.path.join(os.getcwd(), 'media/')

    for file in uploaded_files:
        default_storage.save(os.path.join(file_path, str(file)), ContentFile(file.read()))
