from django.urls import include, path
from rest_framework import routers
from app_gestao import views

router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet)
router.register(r'groups', views.GroupViewSet)
router.register(r'categorias', views.CategoriasViewSet)
router.register(r'gastos', views.GastosViewSet)
router.register(r'bancos', views.BancosViewSet)
router.register(r'user_bancos', views.UserBancosViewSet)



# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]