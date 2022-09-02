from django.contrib import messages
from django.http import HttpResponseRedirect, HttpResponse, Http404
from django.shortcuts import render
from django.urls import reverse

from scvulweb.models import Test_Type as test_t
from scvulweb.form import Tool_TypeForm


def Tool_Type(request):
    contexto = {'tool_type': test_t.objects.all()}
    return render(request, 'scvulweb/tool_type_list.html', contexto)


def edit_Tool_Type(request, id):
    toolt = test_t.objects.get(id=id)
    if request.method == 'GET':
        form = Tool_TypeForm(instance=toolt)
    else:
        form = Tool_TypeForm(request.POST, instance=toolt)
        if form.is_valid():
            form.save()
        messages.success(request, 'Editado correctamente')

        return HttpResponseRedirect(reverse('tool_type_list'))
    return render(request, 'scvulweb/tool_type_edit.html', {
        'tform': form,
    })

def add_Tool_Type(request):
    form = Tool_TypeForm()
    if request.method == 'POST':
        form = Tool_TypeForm(request.POST)
        if form.is_valid():
            form.save()

            return HttpResponseRedirect(reverse('tool_type_list'))
    return render(request, 'scvulweb/tool_type_add.html', {
        'tform': form
    })