from django.contrib import admin
from .models import Service

# Registre o modelo 'Service' para que ele apareça no painel de administração
admin.site.register(Service)