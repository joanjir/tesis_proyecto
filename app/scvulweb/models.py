import base64
import hashlib
import logging
import os
import re
import copy
from typing import Dict, Set, Optional
from uuid import uuid4
from django.urls import reverse
from django.utils.functional import cached_property
from django.utils.deconstruct import deconstructible
from django.core.validators import RegexValidator, validate_ipv46_address
from django.core.exceptions import ValidationError
from django.db import models, connection
from django.utils import timezone
from django.utils.html import escape
from django.utils.timezone import now

from pytz import all_timezones
from django.utils.translation import gettext as _

from django.db.models import JSONField
from cvss import CVSS3


@deconstructible
class UniqueUploadNameProvider:
    """
    Un invocable que se pasará como parámetro upload_to a FileField.

    Los archivos cargados obtendrán nombres aleatorios basados ​​en UUID dentro del directorio dado;
    El formato de estilo strftime es compatible con la ruta del directorio. Si mantener_nombre_base
    es True, el nombre del archivo original se antepone al UUID. Si keep_ext está deshabilitado,
    la extensión del nombre de archivo se eliminará.
    """

    def __init__(self, directory=None, keep_basename=False, keep_ext=True):
        self.directory = directory
        self.keep_basename = keep_basename
        self.keep_ext = keep_ext

    def __call__(self, model_instance, filename):
        base, ext = os.path.splitext(filename)
        filename = "%s_%s" % (
            base, uuid4()) if self.keep_basename else str(uuid4())
        if self.keep_ext:
            filename += ext
        if self.directory is None:
            return filename
        return os.path.join(now().strftime(self.directory), filename)


def get_current_date():
    return timezone.now().date()


def get_current_datetime():
    return timezone.now()


class FileUpload(models.Model):
    title = models.CharField(max_length=100, unique=True)
    file = models.FileField(upload_to=UniqueUploadNameProvider('uploaded_files'))


class Site(models.Model):
    id_site = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50, null=True, blank=True)
    url = models.URLField(max_length=500, editable=True, blank=False, null=False)

    def __str__(self):
        return self.name


class Test_Type(models.Model):
    name = models.CharField(max_length=200, unique=True)
    active = models.BooleanField(default=True)

    def active_tool(self):
        if self.active == False:
            self.active = True
        else:
            self.active = False
        self.save()

    def __str__(self):
        return self.name


class Test_Site(models.Model):
    id_test_s = models.AutoField(primary_key=True)
    site = models.OneToOneField(Site, on_delete=models.CASCADE, null=False, blank=False)
    name = models.CharField(max_length=255, null=True, blank=True)
    target_start = models.DateField()

    def __str__(self):
        return self.name


class Test(models.Model):
    id_test = models.AutoField(primary_key=True)
    test_s = models.ForeignKey(Test_Site, on_delete=models.CASCADE,null=True, blank=True)
    title = models.CharField(max_length=255, null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    target_start = models.DateField()
    target_end = models.DateField()
    updated = models.DateTimeField(auto_now=True, null=True)
    created = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return self.title


class Test_Import(models.Model):
    id_test_imp = models.AutoField(primary_key=True)
    test = models.ForeignKey(Test, null=False, blank=False, on_delete=models.CASCADE)
    files = models.ManyToManyField(FileUpload, blank=True)
    created = models.DateTimeField(auto_now_add=True, null=True)
    test_type = models.ForeignKey(Test_Type,on_delete=models.CASCADE)

    class Meta:
        ordering = ('-id_test_imp',)
