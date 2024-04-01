import customtkinter as ctk
from app.core.singleton.action_logger import LoggerManager
from app.core.prototype.document import TextDocument, ImageDocument, VideoDocument

class ShowLogUI:
    def __init__(self, parent):
        self.parent = parent
        self.logger_manager = LoggerManager()
        self.style_font = {
            'header': ('Helvetica', 24, 'bold'),
            'title': ('Helvetica', 14, 'bold'),
            'subtitle': ('Helvetica', 14, 'bold'),
            'normal': ('Helvetica', 14),
        }
        self.init_ui()

    def init_ui(self):
        self.ctn_frame = ctk.CTkFrame(self.parent)
        self.ctn_frame.pack(fill="both", expand=True, padx=5, pady=5)
        for key in self.logger_manager._data_log.keys():
            value = self.logger_manager._data_log[key]
            path = value.path[:value.path.__len__() // 3] + "..." + value.path[-value.path.__len__() // 3:] if value.path else None

            if isinstance(value, TextDocument):
                label_log = ctk.CTkLabel(self.ctn_frame, text=f"Text Document: {value.title} by {value.author}, path {path}", font=self.style_font['normal'])
                label_log.pack(fill="x")

            elif isinstance(value, ImageDocument):
                label_log = ctk.CTkLabel(self.ctn_frame, text=f"Image Document: {value.title} by {value.author}, size {value.size}, path {path}", font=self.style_font['normal'])
                label_log.pack(fill="x")

            elif isinstance(value, VideoDocument):
                label_log = ctk.CTkLabel(self.ctn_frame, text=f"Video Document: {value.title} by {value.author}, quality {value.quality}, path {path}", font=self.style_font['normal'])
                label_log.pack(fill="x")