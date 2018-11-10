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


class Variacao(models.Model):
    cd_variacao = models.PositiveIntegerField(default=1)
    dc_cor = models.PositiveIntegerField(default=1)
    dc_numero = models.PositiveIntegerField(default=1)
    dc_voltagem = models.PositiveIntegerField(default=1)

    
class Produto(models.Model):
    cd_produto = models.PositiveIntegerField(default=1, unique=True)
    nm_produto = models.CharField(max_length=255, unique=True)
    dc_modelo = models.CharField(max_length=64)
    cd_barras = models.CharField(max_length=15)
    cd_altura = models.DecimalField(max_digits=15, decimal_places=8)
    nr_comprimento = models.DecimalField(max_digits=15, decimal_places=8)
    nr_largura = models.DecimalField(max_digits=15, decimal_places=8)
    nr_peso = models.DecimalField(max_digits=15, decimal_places=8)
    dt_cadastro = models.DateField(auto_now_add=True)
    fl_situacao = models.PositiveIntegerField(default=1)
    marca = models.ForeignKey(Marca, on_delete=models.CASCADE)
    

class VariacaoProduto(models.Model):
    variacao = models.ForeignKey(Variacao, on_delete=models.CASCADE)
    produto = models.ForeignKey(Produto, on_delete=models.CASCADE)