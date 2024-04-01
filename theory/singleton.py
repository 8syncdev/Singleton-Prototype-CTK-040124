class LoggerManager(object):
    _instance = None
    _data_log = {}

    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super().__new__(cls, *args, **kwargs)
        return cls._instance

    def add_log(self, key, value):
        self._data_log[key] = value


class DocumentLogger(LoggerManager):
    pass


class ImageLogger(LoggerManager):
    pass

logger_manager = LoggerManager()
logger_manager.add_log("Log1", "This is a log message")

doc_logger1 = DocumentLogger()
doc_logger1.add_log("Document1", "This is a text document")

doc_logger2 = DocumentLogger()
doc_logger2.add_log("Document2", "This is another text document")

image_logger1 = ImageLogger()
image_logger1.add_log("Image1", "This is an image")

image_logger2 = ImageLogger()
image_logger2.add_log("Image2", "This is another image")


# Kiểm tra vùng nhớ của các đối tượng
print(id(doc_logger1), id(doc_logger2))
print(id(image_logger1), id(image_logger2))

