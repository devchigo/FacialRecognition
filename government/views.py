from django.http import HttpResponse
from django.shortcuts import render
from .models import Criminal
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView
from django.urls import reverse_lazy


# Create your views here.

# def criminal_list(request):
#     criminal = Criminal.objects.all()
#     context = {'criminal': criminal }
#     return render(request, 'criminal_list.html', context)

class CriminalList(ListView):
    model = Criminal
    template_name = "criminal_list.html"
    context_object_name = "criminal_list"


class CriminalDetail(DetailView):
    model = Criminal
    template_name = "criminal_detail.html"
    context_object_name = "criminal_detail"


class CriminalCreate(CreateView):
    model = Criminal
    fields = '__all__'
    success_url = reverse_lazy('criminal_list')
    # template_name = "criminal_form.html"


class CriminalUpdate(UpdateView):
    model = Criminal
    fields = '__all__'
    success_url = reverse_lazy('criminal_list')
