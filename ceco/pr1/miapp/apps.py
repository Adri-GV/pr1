from django.apps import AppConfig


class MiappConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'miapp'
    # Cambiar nombre en /admin
    verbose_name='Zapatos Bernini'