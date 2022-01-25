from django.apps import AppConfig


class UsersConfig(AppConfig):
    name = 'users'

    def ready(self): #Django requires an import of signals into respective apps "apps.py" file.
        #the function is called "ready" because we must overwrite the values for the default django "ready" function
        import users.signals #here we import our specified signals!