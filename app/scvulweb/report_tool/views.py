from django.shortcuts import render, get_object_or_404
from django.urls import reverse
from django.http import HttpResponseRedirect

from scvulweb.models import Test as tests


from scvulweb.form import ImportReportForm, UploadFileForm


def report_tool_test_add(request, id_test):
    testdd = tests.objects.get(id_test=id_test)
    form = ImportReportForm()
    if request.method == 'POST':
        form = ImportReportForm(request.POST)
        if form.is_valid():
            addfm = form.save()
            addfm.test = testdd
            form.save()

            return HttpResponseRedirect(reverse('detail_test', args=(id_test, )))
    return render(request, 'scvulweb/report_tool_test_add.html', {
        'tform': form,  'testdd': testdd
    })
