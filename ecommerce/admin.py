from django.contrib import admin
from import_export.admin import ImportExportModelAdmin

from ecommerce.models import Marca


@admin.register(Marca)
class MarcaResource(ImportExportModelAdmin):
    pass
