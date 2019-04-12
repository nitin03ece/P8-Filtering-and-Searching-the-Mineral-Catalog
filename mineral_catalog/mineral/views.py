from django.shortcuts import render, get_object_or_404, reverse
from django.db.models import Q
from .models import Mineral
from . import forms
import random


def search_minerals(search):
    minerals_all = Mineral.objects.filter(
        Q(name__icontains=search)|
        Q(category__icontains=search)|
        Q(strunz_classification__icontains=search)|
        Q(crystal_system__icontains=search)|
        Q(unit_cell__icontains=search)|
        Q(crystal_symmetry__icontains=search)|
        Q(cleavage__icontains=search)|
        Q(mohs_scale_hardness__icontains=search)|
        Q(luster__icontains=search)|
        Q(streak__icontains=search)|
        Q(diaphaneity__icontains=search)|
        Q(optical_properties__icontains=search)|
        Q(refractive_index__icontains=search)|
        Q(crystal_habit__icontains=search)|
        Q(specific_gravity__icontains=search)|
        Q(group__icontains=search)
    )
    return minerals_all


def home(request):
    minerals_alphabet = Mineral.objects.filter(name__startswith='A')
    # minerals_all = Mineral.objects.all()
    # minerals_alphabet = [mineral for mineral in minerals_all if mineral.name.lower().startswith('a')]
    form = forms.SearchForm()
    if request.method == 'POST':
        form = forms.SearchForm(request.POST)
        if form.is_valid():
            search = form.cleaned_data.get('search')
            minerals_search = search_minerals(search)
            return render(request, "home.html", {'minerals': minerals_search, 'form': form})
    return render(request, "home.html", {'minerals' : minerals_alphabet, "bold_alphabet" : 'A', 'form': form})


def mineralsList(request):
    minerals_all = Mineral.objects.all()
    form = forms.SearchForm()
    if request.method == 'POST':
        form = forms.SearchForm(request.POST)
        if form.is_valid():
            search = form.cleaned_data.get('search')
            minerals_search = search_minerals(search)
            return render(request, "home.html", {'minerals': minerals_search, 'form': form})
    return render(request, "mineral/minerals_list.html", {"minerals" : minerals_all, 'form':form})


def alpha_filtered_mineralList(request, alpha):
    minerals = Mineral.objects.filter(name__startswith=alpha)
    # minerals_all = Mineral.objects.all()
    # minerals = [i for i in minerals_all if i.name.lower().startswith(alpha.lower())]
    form = forms.SearchForm()
    if request.method == 'POST':
        form = forms.SearchForm(request.POST)
        if form.is_valid():
            search = form.cleaned_data.get('search')
            minerals_search = search_minerals(search)
            return render(request, "home.html", {'minerals': minerals_search, 'form': form})
    return render(request, "mineral/minerals_list.html", {"minerals": minerals, "bold_alphabet" : alpha, 'form': form})


def group_filtered_mineralList(request, group):
    minerals = Mineral.objects.filter(group=group)
    # minerals_all = Mineral.objects.all()
    # minerals = [i for i in minerals_all if i.group == group]
    form = forms.SearchForm()
    if request.method == 'POST':
        form = forms.SearchForm(request.POST)
        if form.is_valid():
            search = form.cleaned_data.get('search')
            minerals_search = search_minerals(search)
            return render(request, "home.html", {'minerals': minerals_search, 'form': form})
    return render(request, "mineral/minerals_list.html", {"minerals": minerals, 'bold_group' : group, 'form':form})


def mineralDetail(request, name):
    minerals_all = Mineral.objects.all()
    form = forms.SearchForm()
    mineral = get_object_or_404(Mineral, name=name)
    if request.method == 'POST':
        form = forms.SearchForm(request.POST)
        if form.is_valid():
            search = form.cleaned_data.get('search')
            minerals_search = search_minerals(search)
            return render(request, "home.html", {'minerals': minerals_search, 'form': form})
    return render(request, "mineral/mineral_detail.html", {"mineral" : mineral, 'form': form})


def randomMineral(request):
    minerals_all = Mineral.objects.all()
    mineral = random.choice(minerals_all)
    form = forms.SearchForm()
    if request.method == 'POST':
        form = forms.SearchForm(request.POST)
        if form.is_valid():
            search = form.cleaned_data.get('search')
            minerals_search = search_minerals(search)
            return render(request, "home.html", {'minerals': minerals_search, 'form': form})
    return render(request, "mineral/random_mineral.html", {"mineral" : mineral, 'form':form})
