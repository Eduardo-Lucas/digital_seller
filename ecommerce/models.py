from django.db import models


class Versao(models.Model):
    pass


class Marca(models.Model):
    cd_marca = models.PositiveIntegerField(default=1, unique=True)
    nm_marca = models.CharField(max_length=64, unique=True)
    
    class Meta:
        ordering = ['nm_marca']
        verbose_name = "Marca"
        verbose_name_plural = "Marcas"

    def __str__(self):
        return self.nm_marca
