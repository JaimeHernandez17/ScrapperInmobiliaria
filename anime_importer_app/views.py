import os

from django.conf import settings
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView

from anime_importer_app.tasks import process_file
from .forms import AnimeFileForm
from .models import AnimeFile


def index(request):
    return render(request, 'anime_importer/index.html')


def success_file(request):
    return render(request, 'anime_importer/success/success_file.html')


class AddFile(CreateView):
    model = AnimeFile
    template_name = 'anime_importer/addfile.html'
    form_class = AnimeFileForm
    success_url = reverse_lazy('success_file')

    def form_valid(self, form):
        data = form.save()
        path = f'{os.path.join(settings.MEDIA_ROOT)}/{str(data.file)}'
        process_file.delay(path)
        return redirect('success_file')
