import customtkinter as ctk
from app.core.singleton.action_logger import LoggerManager
from app.core.prototype.document import TextDocument, ImageDocument, VideoDocument
from PIL import Image, ImageTk


class StaticUI(ctk.CTkFrame):
    def __init__(self, parent, **kwargs):
        super().__init__(parent, **kwargs)
        self.pack(fill="both", expand=True)
        self.log_manager = LoggerManager()

        self.style_font = {
            'header': ('Helvetica', 24, 'bold'),
            'title': ('Helvetica', 14, 'bold'),
            'subtitle': ('Helvetica', 14, 'bold'),
            'normal': ('Helvetica', 14),
        }

        self.init_ui()

    def init_ui(self):
        self.left_frame = ctk.CTkFrame(self, width=500)
        self.left_frame.pack(side="left", fill="y", padx=3, pady=3)


        self.right_frame = ctk.CTkFrame(self)
        self.right_frame.pack(side="right", fill="both", expand=True, padx=(3, 0), pady=3)



    def implement_left_frame(self):
        if hasattr(self, "left_frame"):
            self.left_frame.destroy()

        self.left_frame = ctk.CTkFrame(self, width=500)
        self.left_frame.pack(side="left", fill="y", padx=3, pady=3)
        for key in self.log_manager._data_log.keys():
            value = self.log_manager._data_log[key]
            path = value.path[:value.path.__len__() // 3] + "..." + value.path[-value.path.__len__() // 3:] if value.path else None

            if isinstance(value, TextDocument):
                label_log = ctk.CTkLabel(self.left_frame, text=f"Text Document: {value.title} by {value.author}, path {path}", font=self.style_font['normal'])
                label_log.pack(fill="x")
                label_log.bind("<Button-1>", lambda e, value=value: self.show_detail(value))

            elif isinstance(value, ImageDocument):
                label_log = ctk.CTkLabel(self.left_frame, text=f"Image Document: {value.title} by {value.author}, size {value.size}, path {path}", font=self.style_font['normal'])
                label_log.pack(fill="x")
                label_log.bind("<Button-1>", lambda e, value=value: self.show_detail(value))

            elif isinstance(value, VideoDocument):
                label_log = ctk.CTkLabel(self.left_frame, text=f"Video Document: {value.title} by {value.author}, quality {value.quality}, path {path}", font=self.style_font['normal'])
                label_log.pack(fill="x")
                label_log.bind("<Button-1>", lambda e, value=value: self.show_detail(value))

    def show_detail(self, value):
        if hasattr(self, "show_detail_ui"):
            self.show_detail_ui.destroy()

        self.show_detail_ui = ctk.CTkFrame(self.right_frame)
        self.show_detail_ui.pack(fill="both", expand=True, padx=5, pady=5)

        if isinstance(value, TextDocument):
            with open(value.path, "r") as f:
                content = f.read()
            label_content = ctk.CTkLabel(self.show_detail_ui, text=content, font=self.style_font['normal'])
            label_content.pack(fill="both", expand=True)

        elif isinstance(value, ImageDocument):
            img = Image.open(value.path)
            img = img.resize((300, 300))
            img = ImageTk.PhotoImage(img)
            label_img = ctk.CTkLabel(self.show_detail_ui, image=img, text="")
            label_img.image = img
            label_img.pack(fill="both", expand=True)

        elif isinstance(value, VideoDocument):
            pass
