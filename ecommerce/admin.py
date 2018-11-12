from django.contrib import admin
from import_export.admin import ImportExportModelAdmin

from ecommerce.models import Marca, Produto


@admin.register(Marca)
class MarcaResource(ImportExportModelAdmin):
    pass


@admin.register(Produto)
class ProdutoResource(ImportExportModelAdmin):
    pass