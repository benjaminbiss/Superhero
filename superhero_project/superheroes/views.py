from django.shortcuts import redirect, render
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.urls.base import reverse_lazy
from .models import Superhero

# Create your views here.
def index(request):
    all_heroes = Superhero.objects.all()
    context = {
        'all_heroes' : all_heroes
    }
    return render(request, 'superheroes/index.html', context)

def detail(request, hero_id):
    single_hero = Superhero.objects.get(pk=hero_id)
    context = {
        'single_hero' : single_hero
    }
    return render(request, 'superheroes/detail.html', context)

def create(request):
    if request.method == "POST":
        name = request.POST.get('name')
        alter_ego = request.POST.get('alter_ego')
        primary_ability = request.POST.get('primary')
        secondary_ability = request.POST.get('secondary')
        catchphrase = request.POST.get('catchphrase')
        new_hero = Superhero(name=name, alter_ego=alter_ego, primary_ability=primary_ability, secondary_ability=secondary_ability, catch_phrase=catchphrase)
        new_hero.save()
        return HttpResponseRedirect(reverse('superheroes:index'))
    else:
        return render(request, 'superheroes/create.html')

def delete(request, hero_id):
    hero = Superhero.objects.get(pk=hero_id)
    context = {
        'hero' : hero
    }
    if request.method != "POST":
        return render(request, 'superheroes/delete.html', context)
    else:
        hero.delete()
        return HttpResponseRedirect(reverse('superheroes:index'))

def edit(request, hero_id):
    hero = Superhero.objects.get(pk=hero_id)
    context = {
        'hero' : hero
    }
    if request.method != 'POST':
        return render(request, 'superheroes/edit.html', context)
    else:
        hero.name = request.POST.get('name')
        hero.alter_ego = request.POST.get('alter_ego')
        hero.primary_ability = request.POST.get('primary')
        hero.secondary_ability = request.POST.get('secondary')
        hero.catch_phrase = request.POST.get('catchphrase')
        hero.save()
        return HttpResponseRedirect(reverse('superheroes:index'))
