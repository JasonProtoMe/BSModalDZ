from django.shortcuts import render
from django.http import HttpResponse
from django.core.files.storage import default_storage
from django.core.files.base import ContentFile

from .forms import InfoForm

import os

# Create your views here.

def index(request):
    context = {}
    if request.method == 'POST':
        info_form = InfoForm(request.POST)
        if info_form.is_valid():
            savefiles(request)
        return HttpResponse(context)

    # different request method (ie. GET request)
    else:
        info_form = InfoForm()
        context['info_form'] = info_form


    return render(request, 'ModalDZ/index.html', context)

def savefiles(request):
    # A way to access Django-files format
    uploaded_files = [request.FILES.get('file[%d]' % i)
                     for i in range(0, len(request.FILES))]

    # saving onto the media folder
    file_path = os.path.join(os.getcwd(), 'media/')

    for file in uploaded_files:
        default_storage.save(os.path.join(file_path, str(file)), ContentFile(file.read()))
