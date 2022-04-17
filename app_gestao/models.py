from django.db import models
from django.contrib.auth.models import User 
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
    usuario_fk = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    nome = models.CharField(max_length=24)
    saldo = models.DecimalField(max_digits=7, decimal_places=2, blank=True, null=True)
    credito_limite = models.DecimalField(max_digits=7, decimal_places=2, blank=True, null=True)
    credito_disponivel = models.DecimalField(max_digits=7, decimal_places=2, blank=True, null=True)
    fechamento_fatura = models.IntegerField(max_length=2)
    vencimento_fatura = models.IntegerField(max_length=2) 

    criado_em = models.DateTimeField(auto_now_add=True)
    ultima_alteracao = models.DateTimeField(auto_now=True)
    class Meta:
        verbose_name = "Banco"
        verbose_name_plural = "Bancos"
    def __str__(self):
        return self.nome

class Categoria(models.Model):
    nome = models.CharField(max_length=24)
    slug = models.SlugField(max_length=28)
    cor = models.CharField(max_length=16)

    criado_em = models.DateTimeField(auto_now_add=True)
    ultima_alteracao = models.DateTimeField(auto_now=True)
    class Meta:
        verbose_name = "Categoria"
        verbose_name_plural = "Categorias"
    def __str__(self):
        return self.nome

class Gasto(models.Model):
    nome = models.CharField(max_length=24)
    valor = models.DecimalField(max_digits=7, decimal_places=2)
    data_referente = models.DateField()
    categoria_fk = models.ForeignKey(Categoria, on_delete=models.CASCADE)

    criado_em = models.DateTimeField(auto_now_add=True)
    ultima_alteracao = models.DateTimeField(auto_now=True)
    class Meta:
        verbose_name = "Gasto"
        verbose_name_plural = "Gastos"
    def __str__(self):
        return "{nome} (R$: {valor})".format(nome=self.nome, valor=self.valor)

class Lancamento(models.Model):
    usuario_fk = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    banco_fk = models.ForeignKey(Banco, on_delete=models.CASCADE)
    gasto_fk = models.OneToOneField(Gasto, on_delete=models.CASCADE)

    criado_em = models.DateTimeField(auto_now_add=True)
    ultima_alteracao = models.DateTimeField(auto_now=True)
    class Meta:
        verbose_name = "Lançamento"
        verbose_name_plural = "Lançamentos"
    def __str__(self):
        return "Lançamento: {}".format(self.gasto_fk)