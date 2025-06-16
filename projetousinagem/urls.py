from django.contrib import admin
from django.urls import path
from appusinagem import views
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('servicos/', views.servicos, name='servicos'),
    path('lista-servicos/', views.listaservicos, name='lista-servicos'),
    path('novo-servico/', views.novoservico, name='novo-servico'),
    path('agenda/', views.agenda, name='agenda'),
    path('finalizar-servico/<int:service_id>/', views.finalizar_servico, name='finalizar-servico'),
    path('reativar-servico/<int:service_id>/', views.reativar_servico, name='reativar-servico'),
    path('servicos-finalizados/', views.listaservicos, name='servicos-finalizados'),
    path('excluir-servico/<int:service_id>/', views.excluir_servico, name='excluir-servico'),
    path('editar-servico/<int:service_id>/', views.editar_servico, name='editar-servico'),
     path('clientes/', views.clientes, name='clientes'),
    path('novo-cliente/', views.novo_cliente, name='novo-cliente'),
    path('editar-cliente/<int:cliente_id>/', views.editar_cliente, name='editar_cliente'),
    path('excluir-cliente/<int:cliente_id>/', views.excluir_cliente, name='excluir_cliente'),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
