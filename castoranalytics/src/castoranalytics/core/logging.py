import datetime


class LogManager:
    def __init__(self):
        self._name = 'castormobile'

    def _log(self, level, message):
        timestamp = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        print(f'[{timestamp}] {level} {self._name}: {message}')

    def info(self, message):
        self._log('INFO', message)

    def warning(self, message):
        self._log('WARNING', message)

    def error(self, message):
        self._log('ERROR', message)