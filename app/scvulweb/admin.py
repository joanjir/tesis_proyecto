from django.contrib import admin

# Register your models here.
from .models import Site, FileUpload, Test, Test_Import, Test_Type, Test_Site

admin.site.register(Site)
admin.site.register(FileUpload)
admin.site.register(Test)
admin.site.register(Test_Site)
admin.site.register(Test_Type)
admin.site.register(Test_Import)


