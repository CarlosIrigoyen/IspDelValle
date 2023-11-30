from django.contrib import admin
from import_export import resources, fields
from import_export.admin import ImportExportModelAdmin
from .models import Cliente

# Register your models here.
class clienteAdmin(admin.ModelAdmin):
    list_display = ('nombre','apellido','dni')



admin.site.register(Cliente, clienteAdmin)