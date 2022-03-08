from djmoney.models.fields import MoneyField
from django.db import models
from django.contrib.auth.models import User 
# Create your models here.

class Bancos(models.Model):
    usuario_id = models.ForeignKey(User, related_name='bancos', on_delete=models.CASCADE)
    nome = models.CharField(max_length=24)
    saldo = models.DecimalField(max_digits=7, decimal_places=2, blank=True, null=True)
    credito_limite = models.DecimalField(max_digits=7, decimal_places=2, blank=True, null=True)
    credito_disponivel = models.DecimalField(max_digits=7, decimal_places=2, blank=True, null=True)
    fechamento_fatura = models.DateField()
    vencimento_fatura = models.DateField() 

    criado_em = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.nome

class Categorias(models.Model):
    nome = models.CharField(max_length=24)
    slug = models.SlugField(max_length=28)
    cor = models.CharField(max_length=16)

    criado_em = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.nome

class Gastos(models.Model):
    nome = models.CharField(max_length=24)
    data_referente = models.DateField()
        
    usuario_id = models.ForeignKey(User, on_delete=models.CASCADE)
    categoria_id = models.ForeignKey(Categorias, on_delete=models.CASCADE)

    criado_em = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.categoria+'_'+self.criado_em

class Faturas(models.Model):
    banco_id = models.ForeignKey(Bancos, on_delete=models.CASCADE)

    limite_usado = models.DecimalField(max_digits=7, decimal_places=2)
    mes_referente = models.DateField()
    fechada = models.BooleanField(default=False)

    criado_em = models.DateTimeField(auto_now_add=True)

class GastoValor(models.Model):
    fatura_id = models.ForeignKey(Faturas, on_delete=models.CASCADE)
    gasto_id = models.ForeignKey(Gastos, on_delete=models.CASCADE)
    valor = models.DecimalField(max_digits=7, decimal_places=2)    

    