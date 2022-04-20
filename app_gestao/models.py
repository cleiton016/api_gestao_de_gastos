from django.db import models
from django.contrib.auth.models import User
from django.utils.text import slugify
from .choices import *
from random import random
# Create your models here.

class Usuario(models.Model):
    usuario = models.OneToOneField(User, on_delete=models.CASCADE)
    nome = models.CharField(max_length=128)
    email = models.EmailField()
    foto = models.ImageField(null=True, blank=True)

    criado_em = models.DateTimeField(auto_now_add=True)
    ultima_alteracao = models.DateTimeField(auto_now=True)
    class Meta:
        verbose_name = "Usuário"
        verbose_name_plural = "Usuários"
    def __str__(self):
        return self.nome

class Banco(models.Model):
    usuario_fk = models.ForeignKey(Usuario, on_delete=models.CASCADE, verbose_name="Usuário")
    nome = models.CharField(max_length=24)
    saldo = models.DecimalField(max_digits=7, decimal_places=2, blank=True, null=True)
    credito_limite = models.DecimalField(max_digits=7, decimal_places=2, blank=True, null=True)
    credito_disponivel = models.DecimalField(max_digits=7, decimal_places=2, blank=True, null=True)
    fechamento_fatura = models.CharField("Fechamento da fatura",max_length=2)
    vencimento_fatura = models.CharField("Vencimento da fatura",max_length=2) 

    criado_em = models.DateTimeField(auto_now_add=True)
    ultima_alteracao = models.DateTimeField(auto_now=True)
    class Meta:
        verbose_name = "Banco"
        verbose_name_plural = "Bancos"
    def __str__(self):
        return self.nome

class Categoria(models.Model):
    def random_hex_color(end = 0xffffff):
        return '#%06X' % round(random() * end)

    nome = models.CharField(max_length=24)
    slug = models.SlugField(max_length=28, blank=True, null=True)
    cor = models.CharField(max_length=16, default=random_hex_color())

    criado_em = models.DateTimeField(auto_now_add=True)
    ultima_alteracao = models.DateTimeField(auto_now=True)
    class Meta:
        verbose_name = "Categoria"
        verbose_name_plural = "Categorias"

    def save(self, force_insert=False, force_update=False, using=None,
             update_fields=None):
        """Sobrescrita do método `save()` para que o slug da categoria seja gerado a partir do nome"""
        self.slug = slugify(self.nome)
        super().save(force_insert, force_update, using, update_fields)

    def __str__(self):
        return self.nome

class Lancamento(models.Model):
    usuario_fk = models.ForeignKey(Usuario, on_delete=models.CASCADE, verbose_name="Usuário")
    banco_fk = models.ForeignKey(Banco, on_delete=models.CASCADE, verbose_name="Banco")
    mes = models.CharField(max_length=2, choices=MES_LANCAMENTO.choices, verbose_name="Mês")
    ano = models.CharField(max_length=4)

    criado_em = models.DateTimeField(auto_now_add=True)
    ultima_alteracao = models.DateTimeField(auto_now=True)
    class Meta:
        verbose_name = "Lançamento"
        verbose_name_plural = "Lançamentos"
    def __str__(self):
        return "Lançamento: {ano}/{mes}".format(mes=self.mes, ano=self.ano)

class Gasto(models.Model):
    nome = models.CharField(max_length=24)
    valor = models.DecimalField(max_digits=7, decimal_places=2)
    data_referente = models.DateField()
    categoria_fk = models.ForeignKey(Categoria, on_delete=models.CASCADE)
    lancamento_fk = models.ForeignKey(Lancamento, on_delete=models.CASCADE)

    criado_em = models.DateTimeField(auto_now_add=True)
    ultima_alteracao = models.DateTimeField(auto_now=True)
    class Meta:
        verbose_name = "Gasto"
        verbose_name_plural = "Gastos"
    def __str__(self):
        return "{nome} (R$: {valor})".format(nome=self.nome, valor=self.valor)