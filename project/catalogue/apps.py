from django.apps import AppConfig


class CatalogueConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'catalogue'

    def ready(self):
        # Необходимый импорт для работы signals
        import catalogue.signals

