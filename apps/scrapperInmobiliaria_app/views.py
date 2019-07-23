from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import FormView

from apps.scrapperInmobiliaria_app.tasks import searcher_inmobiliaria_1
from .tasks import main
from .forms import ScrapperForm


def results(request):
    return render(request, 'results.html')


class ScrapperViewForm(FormView):
    form_class = ScrapperForm
    template_name = 'index.html'
    success_url = reverse_lazy('results')

    def get_context_data(self, **kwargs):
        context = super(ScrapperViewForm, self).get_context_data(**kwargs)
        if 'form' not in context:
            context['form'] = self.form_class(self.request.GET)
        return context

    def form_valid(self, form):
        email = form.cleaned_data['email']
        sector = form.cleaned_data['sector']
        main.delay(email, sector)
        return HttpResponseRedirect(self.get_success_url())
