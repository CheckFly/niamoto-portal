from django.shortcuts import render
from django.views.generic import TemplateView
from django.http import HttpResponse
from django.template import loader
from .models import Ressource, Person, Activity, Tree
import random
# Create your views here.


def home(request):
    return render(request, 'home.html', {})


def methodologie(request):
    return render(request, 'methodologie.html', {})


def maintenance(request):
    return render(request, 'maintenance.html', {})


# def ressources(request):
#     return render(request, 'ressources.html', {})


class RessouresView(TemplateView):

    template_name = 'ressources.html'

    def get_context_data(self, **kwargs):
        ressources = Ressource.objects.all().order_by('-year')
        persons = Person.objects.all().order_by('?')
        activities = Activity.objects.all
        trees = Tree.objects.all().order_by(
            'family_name', 'genus_name', 'name')
        return {
            'ressources': ressources,
            'persons': persons,
            'activities': activities,
            'trees': trees
        }
