from django.db import models


class Versao(models.Model):
    pass


class Filial(models.Model):
    nome = models.CharField(max_length=60,)
    
    class Meta:
        ordering = ['nome']
        verbose_name = "Filial"
        verbose_name_plural = "Filiais"
        
    def __str__(self):
        return self.nome


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
    filial = models.ForeignKey(Filial, on_delete=models.CASCADE)
    cd_produto = models.PositiveIntegerField(default=1, unique=True)
    nm_produto = models.CharField(max_length=255, unique=True)
    dc_modelo = models.CharField(max_length=64)
    cd_barras = models.CharField(max_length=15)
    cd_altura = models.DecimalField(max_digits=15, decimal_places=8)
    nr_comprimento = models.DecimalField(max_digits=15, decimal_places=8)
    nr_largura = models.DecimalField(max_digits=15, decimal_places=8)
    nr_peso = models.DecimalField(max_digits=15, decimal_places=8)
    dt_cadastro = models.DateField(auto_now_add=True, )
    hr_cadastro = models.TimeField(auto_now_add=True, )
    dt_alteracao = models.DateField(auto_now=True, blank=True)
    hr_alteracao = models.TimeField(auto_now=True, blank=True)
    dt_preco = models.DateField(auto_now=True, blank=True)
    hr_preco = models.TimeField(auto_now=True, blank=True)
    fl_situacao = models.PositiveIntegerField(default=1)
    marca = models.ForeignKey(Marca, on_delete=models.CASCADE)
    qt_estoque = models.DecimalField(max_digits=15, decimal_places=4)
    vl_preco = models.DecimalField(max_digits=15, decimal_places=4)

    def __str__(self):
        return self.nm_produto
    

class VariacaoProduto(models.Model):
    variacao = models.ForeignKey(Variacao, on_delete=models.CASCADE)
    produto = models.ForeignKey(Produto, on_delete=models.CASCADE)


class Cliente(models.Model):
    # choices
    TIPO_PESSOA = ((0, 'Pessoa Física'),
                   (1, 'Pessoa Jurídica'))
    CONTRIBUINTE_ICMS = ((0, 'Isento'),
                         (1, 'Não Contribuinte'),
                         (2, 'Contribuinte'))
    
    cd_cliente_eco = models.PositiveIntegerField(help_text='Código do cliente no e-commerce')
    cd_cliente_erp = models.PositiveIntegerField(help_text='Código do cliente no ERP')
    nr_cpf = models.CharField(max_length=11, null=True, blank=True, help_text='CPF')
    nr_cnpj = models.CharField(max_length=14, null=True, blank=True, help_text='CNPJ')
    nm_cliente = models.CharField(max_length=128, help_text='Nome/Fantasia do cliente')
    dt_nascimento = models.DateField(null=True, blank=True, help_text='Data de nascimento')
    tp_pessoa = models.PositiveSmallIntegerField(choices=TIPO_PESSOA, default=0,
                                                 help_text='Tipo de pessoa física (0), jurídica(1)')
    fl_contribuinte_icms = models.PositiveSmallIntegerField(choices=CONTRIBUINTE_ICMS, default=0,
                                                            help_text='Contribuinte ICMS: '
                                                                      'isento (0) não contribuinte (1) contribuinte (2)')
    nr_rg = models.CharField(max_length=15,  null=True, blank=True, help_text='Registro geral')
    dc_orgao = models.CharField(max_length=8, null=True, blank=True, help_text='Órgão emissor')
    dt_cadastro = models.DateField(auto_now_add=True, help_text='Data de cadastro do cliente no e-commerce')
    nr_fone_residencia = models.PositiveIntegerField(null=True, blank=True, help_text='Telefone residencial')
    nr_fone_celular = models.PositiveIntegerField(null=True, blank=True, help_text='Telefone celular')
    nm_razao_social = models.CharField(max_length=128,  null=True, blank=True,
                                       help_text='Razão social para pessoa jurídica')
    nr_inscricao_estadual = models.CharField(max_length=32,  null=True, blank=True,
                                             help_text='Inscrição estadual para pessoa jurídica')
    
    def __str__(self):
        if self.tp_pessoa == 0:
            return self.nm_cliente
        else:
            return self.nm_razao_social


class Endereco(models.Model):
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    cd_endereco_erp = models.PositiveIntegerField(help_text='Código do endereço no ERP')
    nr_cep = models.CharField(max_length=11, help_text='Número do CEP')
    dc_endereco = models.CharField(max_length=128, help_text='Descrição do endereço')
    dc_numero = models.CharField(max_length=9, help_text='Número do endereço')
    dc_complemento = models.CharField(max_length=128, help_text='Complemento')
    dc_bairro = models.CharField(max_length=128, help_text='Bairro')
    nm_cidade = models.CharField(max_length=128, help_text='Cidade')
    sg_uf = models.CharField(max_length=2, help_text='UF do estado')
    

class Pedido(models.Model):
    TP_ENTREGA = (
        (0, 'Retira'),
        (1, 'Entrega')
    )
    filial = models.ForeignKey(Filial, on_delete=models.CASCADE, help_text='Código da filial do pedido')
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE, help_text='Código do cliente no ERP')
    nr_pedido_eco = models.PositiveIntegerField(help_text='Número do pedido no e-commerce')
    nr_pedido_erp = models.PositiveIntegerField(help_text='Número do pedido no ERP')
    dt_pedido = models.DateField(auto_now_add=True, help_text='Data do pedido')
    hr_pedido = models.TimeField(auto_now_add=True, help_text='Hora do pedido')
    cd_vendedor = models.PositiveIntegerField(help_text='Código do vendedor no ERP')
    dc_observacao = models.TextField(max_length=230, help_text='Observação do cliente no pedido')
    tp_entrega = models.PositiveIntegerField(choices=TP_ENTREGA, default=1, help_text='Retira (0), Entrega (1)')
    vl_entrega = models.DecimalField(max_digits=15, decimal_places=4, help_text='Valor da entrega')
    
    class Meta:
        ordering = ['-dt_pedido', 'nr_pedido_eco', 'nr_pedido_erp']
        verbose_name = "Pedido"
        verbose_name_plural = "Pedidos"
        
    def __str__(self):
        return str(self.filial) + ' ' + str(self.nr_pedido_eco) + ' ' + str(self.nr_pedido_eco) + \
               ' ' + str(self.dt_pedido)
    

class PedidoItem (models.Model):
    pedido = models.ForeignKey(Pedido, related_name='items', on_delete=models.CASCADE)
    produto = models.ForeignKey(Produto, on_delete=models.CASCADE)
    qt_comprada = models.DecimalField(max_digits=15, decimal_places=4, default=1,
                                      help_text='Quantidade comprada (Produto)')
    vl_venda = models.DecimalField(max_digits=15, decimal_places=4, help_text='Valor de venda (Produto)')
    
    def __str__(self):
        return str(self.produto) + ' ' + str(self.qt_comprada) + ' ' + str(self.vl_venda)


class Parcela(models.Model):
    TP_PAGAMENTO = (
        (0, 'Cartão'),
        (1, 'Boleto'),
        (2, 'Outros (Parcela)')
    )
    pedido = models.ForeignKey(Pedido, related_name='parcelas', on_delete=models.CASCADE)
    tp_pagamento = models.PositiveIntegerField(choices=TP_PAGAMENTO, default=2, help_text='Cartão (0), Boleto (1), '
                                                                                          'Outros (2) (Parcela)')
    vl_transacao = models.DecimalField(max_digits=15, decimal_places=4, help_text='Valor total das parcelas (Parcela)')
    vl_parcela = models.DecimalField(max_digits=15, decimal_places=4, help_text='Valor da parcela (Parcela)')
    qt_parcelas = models.PositiveIntegerField(help_text='Quantidade de parcelas (Parcela)')
    cd_nsu = models.CharField(max_length=16, null=True, blank=True, help_text='NSU quando usado cartão (Parcela)')
    dt_transacao = models.DateField(auto_now_add=True)
    cd_autorizacao = models.CharField(max_length=16, null=True, blank=True, help_text='Código da autorização quando '
                                                                                      'usado cartão (Parcela)')
    nm_bandeira = models.CharField(max_length=16, null=True, blank=True, help_text='Nome da bandeira quando '
                                                                                   'usado cartão (Parcela)')
    nm_adquirente = models.CharField(max_length=16, null=True, blank=True, help_text='Nome da adquirente quando usado '
                                                                                     'cartão (Parcela)')
    nr_pedido_gateway = models.CharField(max_length=64, null=True, blank=True, help_text='Número do pedido no gateway '
                                                                                         'de pagamento (Parcela)')
    
    def __str__(self):
        return str(self.tp_pagamento) + ' ' + str(self.id) + ' ' + str(self.vl_transacao) + ' ' + \
               str(self.vl_parcela) + ' ' + str(self.qt_parcelas) + ' ' + str(self.cd_nsu) + ' ' + \
               str(self.dt_transacao) + ' ' + self.cd_autorizacao + ' ' + self.nm_bandeira + ' ' + \
               self.nm_adquirente + ' ' + self.nr_pedido_gateway
