""" Este módulo fornece um gerenciador para o ambiente de log.
"""

class LogEnv:
    def __init__(self):
        self._level_assign = {
            'emergency': [],
            'alert': [],
            'critical': [],
            'error': [],
            'warning': [],
            'notice': [],
            'info': [],
            'debug': [],
            'progress': []
        }
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

    def _assign_logger_to_level(self, level, logger):
        if logger in self._level_assign[level]:
            raise Exception(
                'Logger {logger_name} is already registered for the {level} level'.format(logger_name=logger.get_name(),
                                                                                          level=level))
        else:
            self._level_assign[level].append(logger)

    def assign_to_emergency(self, logger):
        self._assign_logger_to_level('emergency', logger)

    def assign_to_alert(self, logger):
        self._assign_logger_to_level('alert', logger)

    def assign_to_critical(self, logger):
        self._assign_logger_to_level('critical', logger)

    def assign_to_error(self, logger):
        self._assign_logger_to_level('error', logger)

    def assign_to_warning(self, logger):
        self._assign_logger_to_level('warning', logger)

    def assign_to_notice(self, logger):
        self._assign_logger_to_level('notice', logger)

    def assign_to_info(self, logger):
        self._assign_logger_to_level('info', logger)

    def assign_to_debug(self, logger):
        self._assign_logger_to_level('debug', logger)

    def assign_to_progress(self, logger):
        self._assign_logger_to_level('progress', logger)

    def _is_mode(self, level):
        return self._level_active[level]

    def is_emergency(self):
        return self._level_active['emergency']

    def is_alert(self):
        return self._level_active['alert']

    def is_critical(self):
        return self._level_active['critical']

    def is_error(self):
        return self._level_active['error']

    def is_warning(self):
        return self._level_active['warning']

    def is_notice(self):
        return self._level_active['notice']

    def is_info(self):
        return self._level_active['info']

    def is_debug(self):
        return self._level_active['debug']

    def is_progress(self):
        return self._level_active['progress']

    def _get_logger_assigned_to(self, level):
        return self._level_assign[level]

    def get_logger_to_emergency(self):
        return self._level_assign['emergency']

    def get_logger_to_alert(self):
        return self._level_assign['alert']

    def get_logger_to_critical(self):
        return self._level_assign['critical']

    def get_logger_to_error(self):
        return self._level_assign['error']

    def get_logger_to_warning(self):
        return self._level_assign['warning']

    def get_logger_to_notice(self):
        return self._level_assign['notice']

    def get_logger_to_info(self):
        return self._level_assign['info']

    def get_logger_to_debug(self):
        return self._level_assign['debug']

    def get_logger_to_progress(self):
        return self._level_assign['progress']

    def _toggle_level_active(self, level, toggle):
        self._level_active[level] = toggle

    def toggle_emergency(self, toggle):
        self._toggle_level_active('emergency', toggle)

    def toggle_alert(self, toggle):
        self._toggle_level_active('alert', toggle)

    def toggle_critical(self, toggle):
        self._toggle_level_active('critical', toggle)

    def toggle_error(self, toggle):
        self._toggle_level_active('error', toggle)

    def toggle_warning(self, toggle):
        self._toggle_level_active('warning', toggle)

    def toggle_notice(self, toggle):
        self._toggle_level_active('notice', toggle)

    def toggle_info(self, toggle):
        self._toggle_level_active('info', toggle)

    def toggle_debug(self, toggle):
        self._toggle_level_active('debug', toggle)

    def toggle_progress(self, toggle):
        self._toggle_level_active('progress', toggle)
