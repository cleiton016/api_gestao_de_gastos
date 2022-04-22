from django.contrib.auth.models import User, Group, Permission
from rest_framework import serializers
from app_gestao.models import *
from .choices import MES_LANCAMENTO

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'groups']

class GroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = Group
        fields = ['id', 'name']

class PermissionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Permission
        fields = '__all__'

#---------------------------------------------------------#
class UsuarioSerializer(serializers.ModelSerializer):
    usuario_id = serializers.PrimaryKeyRelatedField(queryset=User.objects.all(), required=True, write_only=True, label="Usuário")
    usuario = UserSerializer(read_only=True)
    class Meta:
        model = Usuario
        fields = '__all__'

    read_only_fields = ['criado_em', 'ultima_alteracao']

    def create(self, validated_data):
        validated_data['usuario'] = validated_data.pop('usuario_id')
        return super().create(validated_data)


class CategoriaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Categoria
        fields = ['id', 'nome', 'slug', 'cor', 'criado_em', 'ultima_alteracao']

    read_only_fields = ['slug','criado_em', 'ultima_alteracao']

class GastoSerializer(serializers.ModelSerializer):
    class CategoriaSerializer(serializers.ModelSerializer):
        class Meta:
            model = Categoria
            fields = ['id', 'nome', 'slug', 'cor']
    class LancamentoSerializer(serializers.ModelSerializer):
        class Meta:
            model = Lancamento
            fields = ['id', 'ano', 'mes']
    
    categoria = serializers.PrimaryKeyRelatedField(queryset=Categoria.objects.all(), required=True, write_only=True)
    lancamento = serializers.PrimaryKeyRelatedField(queryset=Lancamento.objects.all(), required=True, write_only=True)

    categoria_fk = CategoriaSerializer(read_only=True)
    lancamento_fk = LancamentoSerializer(read_only=True)
    class Meta:
        model = Gasto
        fields = ['id', 'nome', 'valor', 'data_referente',
                'categoria','lancamento', 'categoria_fk',
                'lancamento_fk', 'criado_em', 'ultima_alteracao']

    read_only_fields = ['criado_em', 'ultima_alteracao']

    def create(self, validated_data):
        validated_data['categoria_fk'] = validated_data.pop('categoria')
        validated_data['lancamento_fk'] = validated_data.pop('lancamento')
        return super().create(validated_data)

class BancoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Banco
        fields = '__all__'
    read_only_fields = ['criado_em', 'ultima_alteracao']

class LancamentoSerializer(serializers.ModelSerializer):
    class ChoiceField(serializers.ChoiceField):
        def to_representation(self, obj):
            if obj == '' and self.allow_blank:
                return obj
            return self._choices[obj]
        def to_internal_value(self, data):
            # To support inserts with the value
            if data == '' and self.allow_blank:
                return ''

            for key, val in self._choices.items():
                if val == data:
                    return key
            self.fail('invalid_choice', input=data)

    mes = ChoiceField(choices=MES_LANCAMENTO.choices)
    class Meta:
        model = Lancamento
        fields = ['id', 'mes', 'ano', 'criado_em', 'ultima_alteracao', 'usuario_fk', 'banco_fk']
    read_only_fields = ['criado_em', 'ultima_alteracao']

