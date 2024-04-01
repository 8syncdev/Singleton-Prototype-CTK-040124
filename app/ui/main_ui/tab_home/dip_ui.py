import customtkinter as ctk
from tkinter.filedialog import askopenfilename
from PIL import Image, ImageTk
from app.assets.key import get_icon
from app.core.prototype.document import *
from app.core.singleton.action_logger import *
from app.ui.main_ui.tab_home.show_log_ui import ShowLogUI



class DipUI:
    def __init__(self, parent, **kwargs):
        self.parent = parent

        self.style_font = {
            'header': ('Helvetica', 24, 'bold'),
            'title': ('Helvetica', 14, 'bold'),
            'subtitle': ('Helvetica', 14, 'bold'),
            'normal': ('Helvetica', 14),
        }


        # Singleton
        self.logger_manager = LoggerManager()
        self.text_logger = TextLogger()

        self.frame_left = ctk.CTkFrame(self.parent, width=500)
        self.frame_left.pack(side="left", fill="y", padx=3, pady=3)

        self.frame_right = ctk.CTkFrame(self.parent)
        self.frame_right.pack(fill="both", expand=True, padx=(3, 0), pady=3)

        self.srollframe_show_log = ctk.CTkScrollableFrame(self.frame_right)
        self.srollframe_show_log.pack(fill="both", expand=True, padx=5, pady=5)

        self.style_primary = {
            'fg_color': '#131313',
            'hover_color': '#1d1d1d',
        }

        self.selected_file = None

        self.init_ui()


    def init_ui(self):
        # Left frame

        self.section_add_document = ctk.CTkFrame(self.frame_left, width=500)
        self.section_add_document.pack(fill="x", padx=5, pady=3)


        self.label_name_section = ctk.CTkLabel(self.section_add_document, text="Thêm tài liệu", font=self.style_font['header'], width=500)
        self.label_name_section.pack(fill="x", pady=5)

        self.innerleft_frame = ctk.CTkFrame(self.section_add_document)
        self.innerleft_frame.pack(fill="x", padx=5, pady=5)

        self.option_values = {
            TextDocument._type: "Upload text document",
            ImageDocument._type: "Upload image document",
            VideoDocument._type: "Upload video document",
        }
        self.menu_options = ctk.CTkOptionMenu(self.innerleft_frame, values=[v for k, v in self.option_values.items()], font=self.style_font['normal'], command=lambda *args: self.init_form_upload_ui())
        self.menu_options.pack(fill="x", pady=5)
        
        self.init_form_upload_ui()



        self.btn_submit = ctk.CTkButton(self.section_add_document, text="Submit", **self.style_primary, command=self.add_log, image=ImageTk.PhotoImage(get_icon('send')))
        self.btn_submit.pack(fill="x", pady=5)


    def add_log(self):
        if self.menu_options.get() == self.option_values[TextDocument._type]:
            title = self.state_widgets["title"].get()
            author = self.state_widgets["author"].get()
            path = self.selected_file
            document = TextDocument(title, author, path)
            self.text_logger.add_log('log_0' if len(self.logger_manager._data_log) == 0 else f'log_{len(self.logger_manager._data_log)}', document.clone())

        elif self.menu_options.get() == self.option_values[ImageDocument._type]:
            title = self.state_widgets["title"].get()
            author = self.state_widgets["author"].get()
            size = self.state_widgets["size"].get()
            path = self.selected_file
            document = ImageDocument(title, author, size, path)
            self.text_logger.add_log('log_0' if len(self.logger_manager._data_log) == 0 else f'log_{len(self.logger_manager._data_log)}', document.clone())

        elif self.menu_options.get() == self.option_values[VideoDocument._type]:
            title = self.state_widgets["title"].get()
            author = self.state_widgets["author"].get()
            quality = self.state_widgets["quality"].get()
            path = self.selected_file
            document = VideoDocument(title, author, quality, path)
            self.text_logger.add_log('log_0' if len(self.logger_manager._data_log) == 0 else f'log_{len(self.logger_manager._data_log)}', document.clone())
        
        print(self.logger_manager._data_log)
        if hasattr(self, "ctn_show_log"):
            self.ctn_show_log.destroy()
        self.ctn_show_log = ctk.CTkFrame(self.srollframe_show_log)
        self.ctn_show_log.pack(fill="both", pady=5)
        self.show_log_ui = ShowLogUI(self.ctn_show_log)

        self.selected_file = None

    def open_file(self, file_type):
        file_name = askopenfilename(filetypes=file_type, title="Choose a file")
        print(file_name)
        self.selected_file = file_name
        return file_name


    def init_form_upload_ui(self):
        if hasattr(self, "innerleft_section_add_document"):
            self.innerleft_section_add_document.destroy()
        self.state_widgets = {}
        self.selected_file = None
        if self.menu_options.get() == self.option_values[TextDocument._type]:
            self.innerleft_section_add_document = ctk.CTkFrame(self.innerleft_frame)
            self.innerleft_section_add_document.pack(fill="x", padx=5, pady=5)

            for attr_name in TextDocument.all_attr_names():
                if attr_name == "path":
                    self.state_widgets[attr_name] = ctk.CTkButton(self.innerleft_section_add_document, text="Upload file", **self.style_primary, command=lambda: self.open_file([("Text files", "*.txt")]), image=ImageTk.PhotoImage(get_icon('upload')))
                    self.state_widgets[attr_name].pack(fill="x", pady=5)

                    continue
                self.state_widgets[attr_name] = ctk.CTkLabel(self.innerleft_section_add_document, text=attr_name, font=self.style_font['title'])
                self.state_widgets[attr_name].pack(fill="x", pady=5)

                self.state_widgets[attr_name] = ctk.CTkEntry(self.innerleft_section_add_document, font=self.style_font['normal'])
                self.state_widgets[attr_name].pack(fill="x", pady=5)

        elif self.menu_options.get() == self.option_values[ImageDocument._type]:
            self.innerleft_section_add_document = ctk.CTkFrame(self.innerleft_frame)
            self.innerleft_section_add_document.pack(fill="x", padx=5, pady=5)

            for attr_name in ImageDocument.all_attr_names():
                if attr_name == "path":
                    self.state_widgets[attr_name] = ctk.CTkButton(self.innerleft_section_add_document, text="Upload file", **self.style_primary, command=lambda: self.open_file([("Image files", "*.jpg *.png")]), image=ImageTk.PhotoImage(get_icon('upload')))
                    self.state_widgets[attr_name].pack(fill="x", pady=5)
                    continue
                self.state_widgets[attr_name] = ctk.CTkLabel(self.innerleft_section_add_document, text=attr_name, font=self.style_font['title'])
                self.state_widgets[attr_name].pack(fill="x", pady=5)

                self.state_widgets[attr_name] = ctk.CTkEntry(self.innerleft_section_add_document, font=self.style_font['normal'])
                self.state_widgets[attr_name].pack(fill="x", pady=5)


        elif self.menu_options.get() == self.option_values[VideoDocument._type]:
            self.innerleft_section_add_document = ctk.CTkFrame(self.innerleft_frame)
            self.innerleft_section_add_document.pack(fill="x", padx=5, pady=5)

            for attr_name in VideoDocument.all_attr_names():
                if attr_name == "path":
                    self.state_widgets[attr_name] = ctk.CTkButton(self.innerleft_section_add_document, text="Upload file", **self.style_primary, command=lambda: self.open_file([("Video files", "*.mp4")]), image=ImageTk.PhotoImage(get_icon('upload')))
                    self.state_widgets[attr_name].pack(fill="x", pady=5)
                    continue
                self.state_widgets[attr_name] = ctk.CTkLabel(self.innerleft_section_add_document, text=attr_name, font=self.style_font['title'])
                self.state_widgets[attr_name].pack(fill="x", pady=5)

                self.state_widgets[attr_name] = ctk.CTkEntry(self.innerleft_section_add_document, font=self.style_font['normal'])
                self.state_widgets[attr_name].pack(fill="x", pady=5)




