from builtins import filter
from datetime import datetime

from django.forms import modelformset_factory
from django.forms.widgets import Widget, Select
import pickle

from django import forms
from scvulweb.models import Site, Test_Site, Test_Type, Test, Test_Import, FileUpload


# Formulario de Sitio
class SiteForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(SiteForm, self).__init__(*args, **kwargs)
        self.fields['name'].widget.attrs['autofocus'] = True

        self.fields['name'].widget.attrs = {

        }

    class Meta:
        model = Site
        fields = '__all__'
        exclude = ['']

        # formulario de prueba


# formulario de prueba sitios
class TestSiteForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(TestSiteForm, self).__init__(*args, **kwargs)

    class Meta:
        model = Test_Site
        fields = '__all__'
        exclude = ['']
        widgets = {
            'site': forms.Select(attrs={
                'autofocus': 'True',
                'class': 'custom-select select2',
                # 'style': 'width: 100%'
            }),
            'name': forms.TextInput(attrs={
                'class': 'form-control ',
            }),
            'target_start': forms.DateInput(
                format='%Y-%m-%d',
                attrs={
                    'value': datetime.now().strftime('%Y-%m-%d'),
                    'autocomplete': 'off',
                    'class': 'form-control datetimepicker-input',
                    'id': 'target_start',
                    'data-target': '#target_start',
                    'data-toggle': 'datetimepicker'
                }
            ),

        }


# Formulario de prueba
class TestForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(TestForm, self).__init__(*args, **kwargs)

    class Meta:
        model = Test
        fields = '__all__'
        exclude = ['']
        widgets = {
            'title': forms.TextInput(attrs={
                'class': 'form-control ',
            }),
            'description': forms.Textarea(attrs={
                'class': 'form-control ',
            }),
            'target_start': forms.DateInput(
                format='%Y-%m-%d',
                attrs={
                    'value': datetime.now().strftime('%Y-%m-%d'),
                    'autocomplete': 'off',
                    'class': 'form-control datetimepicker-input',
                    'id': 'target_start_test',
                    'data-target': '#target_start_test',
                    'data-toggle': 'datetimepicker'
                }
            ),
            'target_end': forms.DateInput(
                format='%Y-%m-%d',
                attrs={
                    'value': datetime.now().strftime('%Y-%m-%d'),
                    'autocomplete': 'off',
                    'class': 'form-control ',
                    'id': 'target_end_test',
                    'data-target': '#target_end_test',
                    'data-toggle': 'datetimepicker'
                }
            ),

        }


# formulario de herramientas
class Tool_TypeForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(Tool_TypeForm, self).__init__(*args, **kwargs)

    class Meta:
        model = Test_Type
        fields = '__all__'
        exclude = ['']
        required = False,
        initial = True
        widgets = {
            'name': forms.TextInput(attrs={
                'class': 'form-control ',
            }),
            'active': forms.CheckboxInput(attrs={
                'style': 'width:30px;height:30px;',
                'class': 'form-check-input form-control ',
                'id': 'flexCheckChecked',
            }),
        }


class ImportReportForm(forms.Form ):
    pass  

class UploadFileForm(forms.ModelForm):
    
    class Meta:
        model = FileUpload
        fields = ['title', 'file']
    



