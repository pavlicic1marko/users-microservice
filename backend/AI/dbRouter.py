class App1DBRouter(object):
    """
A router to control db operations
"""


route_app_labels = {'AI'}
db_name = 'db_app1'
default_db = "default"


def db_for_read(self, model, **hints):
    """
    Attempts to read auth and contenttypes models go to self.db_name.
    """
    if model._meta.app_label in self.route_app_labels:
        return self.db_name
    return self.db_name


def db_for_write(self, model, **hints):
    """
    Attempts to write auth and contenttypes models go to self.db_name.
    """
    if model._meta.app_label in self.route_app_labels:
        return self.db_name
    return self.db_name




def allow_migrate(self, db, app_label, model_name=None, **hints):
    """
    Make sure the auth and contenttypes apps only appear in the
    self.db_name database.
    """
    if app_label in self.route_app_labels:
        return db == self.db_name
    return self.db_name