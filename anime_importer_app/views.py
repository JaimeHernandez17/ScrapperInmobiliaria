from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView

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
