# This class will takes care of DB Routing for master and user routing


class Database_Router(object):

    def db_for_read(self, model, **hints):
        # Point all operations on core  models to 'default'
        if model._meta.app_label == 'core':
            return 'default'
        return 'user'

    def db_for_write(self, model, **hints):
        # Point all operations on core models to 'default'
        if model._meta.app_label == 'core':
            return 'default'
        return 'user'

    def allow_syncdb(self, db, model):
        # Make sure the core app only appears in the 'default' database.
        if db == 'default':
            return model._meta.app_label == 'core'
        elif model._meta.app_label == 'core':
            return False
        return None
