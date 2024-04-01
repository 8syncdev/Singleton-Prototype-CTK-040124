class LoggerManager(object):
    _instance = None
    _data_log = {}

    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super().__new__(cls, *args, **kwargs)
        return cls._instance

    def add_log(self, key, value):
        self._data_log[key] = value


class TextLogger(LoggerManager):
    pass


class ImageLogger(LoggerManager):
    pass

class VideoLogger(LoggerManager):
    pass