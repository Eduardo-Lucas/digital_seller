from django.contrib import admin
from import_export.admin import ImportExportModelAdmin

from ecommerce.models import Marca, Produto, Filial, Cliente


@admin.register(Filial)
class FilialResource(ImportExportModelAdmin):
    pass


@admin.register(Marca)
class MarcaResource(ImportExportModelAdmin):
    pass


@admin.register(Produto)
class ProdutoResource(ImportExportModelAdmin):
    pass


@admin.register(Cliente)
class ClienteResource(ImportExportModelAdmin):
    pass
