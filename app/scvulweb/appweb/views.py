from typing import re

from django.contrib import messages
from django.shortcuts import render, get_object_or_404
from django.urls import reverse
from django.http import HttpResponseRedirect

from scvulweb.models import Site as site

from scvulweb.form import SiteForm


def Site(request):
    contexto = {'site': site.objects.all()}
    return render(request, 'scvulweb/site_list.html', contexto)


def delete_Site(request, id_site):
    sitee = site.objects.get(id_site=id_site)
    if request.method == 'POST':
        sitee.delete()
        return HttpResponseRedirect(reverse('site_list'))
    return render(request, 'scvulweb/site_delete.html', {'sitee': sitee})


def add_Site(request):
    form = SiteForm()
    if request.method == 'POST':
        form = SiteForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Registrado correctamente')

            return HttpResponseRedirect(reverse('site_list'))
    return render(request, 'scvulweb/site_add.html', {
        'form': form
    })


def edit_Site(request, id_site):
    sitee = site.objects.get(id_site=id_site)
    if request.method == 'POST':
        form = SiteForm(request.POST, instance=sitee)
        if form.is_valid():
            form.save()
        messages.success(request, 'Editado correctamente')

        return HttpResponseRedirect(reverse('site_list'))
    else:
        form = SiteForm(instance=sitee)
    return render(request, 'scvulweb/site_edit.html', {
        'form': form,
    })
