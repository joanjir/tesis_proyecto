from django.contrib import messages
from django.shortcuts import render, get_object_or_404
from django.urls import reverse
from django.http import HttpResponseRedirect

from scvulweb.models import Test as tests
from scvulweb.models import Test_Site as testsite

from scvulweb.form import TestForm


def detail_Test(request, id_test):
    testd = tests.objects.get(id_test=id_test)
    testimport = testd.test_import_set.all()
    return render(request, "scvulweb/test_detail.html", {'test': testd, 'testimport': testimport})


def add_Test(request, id_test_s):
    testdd = testsite.objects.get(id_test_s=id_test_s)
    form = TestForm()
    if request.method == 'POST':
        form = TestForm(request.POST)
        if form.is_valid():
            new_test = form.save()
            new_test.test_s = testdd
            form.save()
            return HttpResponseRedirect(reverse('all_test_site', args=(id_test_s, )))
    return render(request, 'scvulweb/tests_add.html', {
        'tform': form, 'testdd': testdd
    })


def delete_Test(request, id_test_s, id_test):
    test = tests.objects.get(id_test=id_test)
    testsites = get_object_or_404(testsite, id_test_s=id_test_s)
    if request.method == 'POST':
        test.delete()
        return HttpResponseRedirect(reverse('all_test_site', args=(id_test_s, )))
    return render(request, 'scvulweb/tests_delete.html', {'test': test, 'testsites':testsites})



def edit_Test(request, id_test_s, id_test):
    test = tests.objects.get(id_test=id_test)
    testsites = get_object_or_404(testsite, id_test_s=id_test_s)
    tform = TestForm(instance=test)
    if request.method == 'POST':
        tform = TestForm(request.POST, instance=test)
        if tform.is_valid():
            edit_test = tform.save()
            edit_test.test_s = testsites
            tform.save()
        return HttpResponseRedirect(reverse('all_test_site', args=(id_test_s, )))
    return render(request, 'scvulweb/tests_edit.html', {
        'tform': tform,'testsites': testsites
    })