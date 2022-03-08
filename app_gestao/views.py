from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from rest_framework import permissions
from app_gestao.serializers import *

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]

class GroupViewSet(viewsets.ModelViewSet):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    permission_classes = [permissions.IsAuthenticated]

class CategoriasViewSet(viewsets.ModelViewSet):
    queryset = Categorias.objects.all()
    serializer_class = CategoriasSerializer
    permission_classes = [permissions.IsAuthenticated]

class GastosViewSet(viewsets.ModelViewSet):
    queryset = Gastos.objects.all()
    serializer_class = GastosSerializer
    permission_classes = [permissions.IsAuthenticated]

class BancosViewSet(viewsets.ModelViewSet):
    queryset = Bancos.objects.all()
    serializer_class = BancosSerializer
    permission_classes = [permissions.IsAuthenticated]

class UserBancosViewSet(viewsets.ModelViewSet):
    queryset = User.objects.prefetch_related('bancos')
    print(str(queryset.query))
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]
    def get_object(self):
        queryset = self.queryset()
        return get_object_or_404(queryset)
        

