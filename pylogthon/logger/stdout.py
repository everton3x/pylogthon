'''
Logger para a saída padrão, geralmente a tela do console ou terminal.
'''


class Stdout:
    def __init__(self, name='unamed_logger', **templates):
        self._name = name

    def get_name(self):
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
