

class router(object):

    def db_for_read(self, model, **hints):
        if model._meta.app_label == 'core':
            return 'core'
        return None

    def db_for_write(self, model, **hints):
        if model._meta.app_label == 'core':
            return 'core'
        return None

    def allow_syncdb(self, db, model):
        if db == 'default':
            return model._meta.app_label == 'core'
        elif model._meta.app_label == 'core':
            return False
        return None
