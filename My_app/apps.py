from django.apps import AppConfig


class MyAppConfig(AppConfig):  # It defines the scope of the app and some initials required when loaded.
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'My_app'
