import copy

class DocumentPrototype:
    def clone(self):
        return copy.deepcopy(self)

    def __str__(self):
        raise NotImplementedError("Subclasses should override this method")


class TextDocument(DocumentPrototype):
    def __init__(self, title, author, num_pages):
        self.title = title
        self.author = author
        self.num_pages = num_pages

    def __str__(self):
        return f"Text Document: {self.title} by {self.author}, {self.num_pages} pages"


class ImageDocument(DocumentPrototype):
    def __init__(self, title, author, size):
        self.title = title
        self.author = author
        self.size = size

    def __str__(self):
        return f"Image Document: {self.title} by {self.author}, size {self.size}"


class VideoDocument(DocumentPrototype):
    def __init__(self, title, author, duration):
        self.title = title
        self.author = author
        self.duration = duration

    def __str__(self):
        return f"Video Document: {self.title} by {self.author}, duration {self.duration} seconds"


# Sử dụng Prototype Design Pattern trong ứng dụng quản lý tài liệu
text_doc_template = TextDocument("Introduction to Python", "John Doe", 100)
image_doc_template = ImageDocument("Nature Photography", "Jane Smith", "5MB")
video_doc_template = VideoDocument("Python Basics", "Alice Johnson", 120)

# Tạo bản sao mới từ các tài liệu mẫu
text_doc_copy = text_doc_template.clone()
image_doc_copy = image_doc_template.clone()
video_doc_copy = video_doc_template.clone()

# Hiển thị thông tin của các bản sao
print(text_doc_copy)
print(image_doc_copy)
print(video_doc_copy)

# Kiểm tra vùng nhớ của các đối tượng
print(id(text_doc_template), id(text_doc_copy))
print(id(image_doc_template), id(image_doc_copy))
print(id(video_doc_template), id(video_doc_copy))


