from django.apps import AppConfig


class MyAppConfig(AppConfig):
    """Class to registered signals"""

    name = 'myapp'

    def ready(self):
        import myapp.signals
