import copy

class DocumentPrototype:
    def clone(self):
        return copy.deepcopy(self)

    def __str__(self):
        raise NotImplementedError("Subclasses should override this method")


class TextDocument(DocumentPrototype):
    _type = "text-document"
    def __init__(self, title, author, path):
        self.title = title
        self.author = author
        self.path = path


    def __str__(self):
        return f"Text Document: {self.title} by {self.author}, {self.num_pages} pages"
    
    @staticmethod
    def all_attr_names():
        return (
            "title",
            "author",
            "path"
        )
    


class ImageDocument(DocumentPrototype):
    _type = "image-document"
    def __init__(self, title, author, size, path):
        self.title = title
        self.author = author
        self.size = size
        self.path = path

    def __str__(self):
        return f"Image Document: {self.title} by {self.author}, size {self.size}"
    
    @staticmethod
    def all_attr_names():
        return (
            "title",
            "author",
            "size",
            "path"
        )


class VideoDocument(DocumentPrototype):
    _type = "video-document"
    def __init__(self, title, author, quality, path):
        self.title = title
        self.author = author
        self.quality = quality
        self.path = path

    def __str__(self):
        return f"Video Document: {self.title} by {self.author}, duration {self.duration} seconds"
    
    @staticmethod
    def all_attr_names():
        return (
            "title",
            "author",
            "quality",
            "path"
        )