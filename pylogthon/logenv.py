'''
Este módulo fornece um gerenciador para o ambiente de log.
'''
class LogEnv:
    def __init__(self):
        self._level_assign = {}
        self._level_active = {
            'emergency': True,
            'alert': True,
            'critical': True,
            'error': True,
            'warning': True,
            'notice': True,
            'info': True,
            'debug': False,
            'progress': True
        }

    def _assign_loggerToLevel(self, level, **loggers):
        pass

    def assign_to_emergency(self, **loggers):
        pass

    def assign_to_emergency(self, **loggers):
        pass

    def assign_to_alert(self, **loggers):
        pass

    def assign_to_critical(self, **loggers):
        pass

    def assign_to_error(self, **loggers):
        pass

    def assign_to_warning(self, **loggers):
        pass

    def assign_to_notice(self, **loggers):
        pass

    def assign_to_info(self, **loggers):
        pass

    def assign_to_debug(self, **loggers):
        pass

    def assign_to_progress(self, **loggers):
        pass

    def get_messenger(self, name='unamed_messenger'):
        pass

    def _is_mode(self):
        pass

    def is_emergency(self):
        pass

    def is_emergency(self):
        pass

    def is_alert(self):
        pass

    def is_critical(self):
        pass

    def is_error(self):
        pass

    def is_warning(self):
        pass

    def is_notice(self):
        pass

    def is_info(self):
        pass

    def is_debug(self):
        pass

    def is_progress(self):
        pass

    def _get_logger_assigned_to(self, level):
        pass

    def get_logger_to_emergency(self):
        pass

    def get_logger_to_alert(self):
        pass

    def get_logger_to_critical(self):
        pass

    def get_logger_to_error(self):
        pass

    def get_logger_to_warning(self):
        pass

    def get_logger_to_notice(self):
        pass

    def get_logger_to_info(self):
        pass

    def get_logger_to_debug(self):
        pass

    def get_logger_to_progress(self):
        pass

    def _toggle_level_active(self, toggle):
        pass

    def toggle_emergency(self):
        pass

    def toggle_emergency(self):
        pass

    def toggle_alert(self):
        pass

    def toggle_critical(self):
        pass

    def toggle_error(self):
        pass

    def toggle_warning(self):
        pass

    def toggle_notice(self):
        pass

    def toggle_info(self):
        pass

    def toggle_debug(self):
        pass

    def toggle_progress(self):
        pass



