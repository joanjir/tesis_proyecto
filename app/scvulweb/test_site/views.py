from django.contrib import messages
from django.shortcuts import render, get_object_or_404
from django.urls import reverse
from django.http import HttpResponseRedirect

from scvulweb.models import Test_Site as tests
from scvulweb.models import Test 
from scvulweb.form import TestSiteForm



def Test_Site(request):
    contexto = {'test': tests.objects.all()}
    return render(request, 'scvulweb/test_site_list.html', contexto)




def add_test_site(request):
    form = TestSiteForm()
    if request.method == 'POST':
        form = TestSiteForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Registrado correctamente')

            return HttpResponseRedirect(reverse('test_site_list'))
    return render(request, 'scvulweb/test_site_add.html', {
        'tform': form
    })




def all_Test(request, id_test_s):
    testd = tests.objects.get(id_test_s= id_test_s)
    testall = Test.objects.filter(test_s=testd).order_by('title')
    return render(request, "scvulweb/tests_list.html", {'testd': testd, 'testall': testall})


#delete 
#def delet_test                         
    
#editar
def edit_test_site(request, id_test_s):
    test = get_object_or_404(tests, id_test_s=id_test_s)
    form = TestSiteForm(instance=test)
    if request.method == 'POST':
        form = TestSiteForm(request.POST, instance=test)
        if form.is_valid():
            form.save()
            messages.success(request, 'Registrado correctamente')

            return HttpResponseRedirect(reverse('test_site_list'))
    return render(request, 'scvulweb/test_site_edit.html', {
        'tform': form
    })    