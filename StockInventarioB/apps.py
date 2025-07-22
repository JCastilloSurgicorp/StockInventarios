from django.apps import AppConfig


class StockinventariobConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'StockInventarioB'

    def ready(self):
        # Importa y registra las señales
        import StockInventarioB.signals