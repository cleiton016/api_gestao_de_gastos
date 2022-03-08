from django.contrib.auth.models import User, Group
from rest_framework import serializers
from app_gestao.models import *


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'bancos']

class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ['url', 'name']
#-------------------------------------------------------------------#
class CategoriasSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Categorias
        fields = ['url', 'nome', 'slug', 'criado_em']

class GastosSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Gastos
        fields = ['url' ,'usuario_id', 'categoria_id', 'data_referente', 'criado_em']
class BancosSerializer(serializers.ModelSerializer):
    class Meta:
        model = Bancos
        fields = '__all__'