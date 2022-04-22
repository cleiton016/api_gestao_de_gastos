from django.contrib import admin
from django.urls import include, path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from rest_framework import routers
from app_gestao import views

router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet)
router.register(r'groups', views.GroupViewSet)
router.register(r'permission', views.PermissionSiewSet)
#------------------------------------------------------#
router.register(r'usuario', views.UsuarioViewSet)
router.register(r'categorias', views.CategoriaViewSet)
router.register(r'gastos', views.GastoViewSet)
router.register(r'bancos', views.BancoViewSet)
router.register(r'lancamento', views.LancamentoViewSer, basename='lancamento')

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path('', include(router.urls)),
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenObtainPairView.as_view(), name='token_refresh')
]