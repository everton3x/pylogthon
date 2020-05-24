""" Mensageiro padrão.
"""


class Std:
    def __init__(self, environment, name='unamed_messenger'):
        self._name = name
        self._environment = environment

    def get_name(self):
        return self._name

    def _send(self, level, message, context={}):
        pass

    def emergency(self, message, context={}):
        pass

    def alert(self, message, context={}):
        pass

    def critical(self, message, context={}):
        pass

    def error(self, message, context={}):
        pass

    def warning(self, message, context={}):
        pass

    def notice(self, message, context={}):
        pass

    def info(self, message, context={}):
        pass

    def debug(self, message, context={}):
        pass

    def progress(self, progress, message='', context={}):
        pass
