import customtkinter as ctk
from PIL import Image, ImageTk
import os 
from app.ui.shared.MenuDev import MenuDev
from app.assets.key import get_icon
from app.custom.SlideControl import SlideControl
from app.ui.main_ui.tab_home.dip_ui import DipUI
from app.ui.main_ui.tab_static.static_ui import StaticUI

class MainUI:
    def __init__(self):
        self.root = ctk.CTk() # tạo ra cửa sổ chính
        self.root.title("Main UI")
        self.root.geometry("1400x700")


        self.style_primary = {
            "fg_color": "#131313",
            "hover_color": "#1d1d1d",
        }

        # Khởi tạo ra ui
        self.init_ui()

        # Chạy chương trình
        self.root.mainloop()

    def init_ui(self):
        # Header
        self.header = ctk.CTkFrame(self.root, height=50)
        self.header.pack(fill="x")

        self.header_right_frame = ctk.CTkFrame(self.header)
        self.header_right_frame.pack(side="right", padx=(0, 5), pady=5)

        MenuDev(self.header_right_frame, ImageTk.PhotoImage(get_icon('user')), _global=self.root, values=["Profile", "Switch account", "Log out"])

        MenuDev(self.header_right_frame, ImageTk.PhotoImage(get_icon('sun')), _global=self.root, values=["System", "Dark", "Light"])


        # Body

        self.body = ctk.CTkFrame(self.root)
        self.body.pack(fill="both", expand=True)


        # Sidebar
        self.sidebar = ctk.CTkFrame(self.body, width=200)
        self.sidebar.pack(side="left", fill="y")

        self.btn_open_sidebar = ctk.CTkButton(self.sidebar, text="", command=lambda: self.slide_control.animate(), image=ImageTk.PhotoImage(get_icon('sidebar')), **self.style_primary)
        self.btn_open_sidebar.pack(fill="x", pady=10)

        self.slide_control = SlideControl(self.sidebar, -1, 0)
        self.slide_control.animate()

        # Create content in slide control
        self.btn_home = ctk.CTkButton(self.slide_control, text="", **self.style_primary, image=ImageTk.PhotoImage(get_icon('home')), command=lambda: self.tab_parent.set("Home"))
        self.btn_home.pack(fill="x", pady=3)

        self.btn_static = ctk.CTkButton(self.slide_control, text="", **self.style_primary, image=ImageTk.PhotoImage(get_icon('codesandbox')), command=lambda: self.set_tab("Static"))
        self.btn_static.pack(fill="x", pady=3)

        # Tab
        self.tab_parent = ctk.CTkTabview(self.body)
        self.tab_parent.pack(fill="both", expand=True, padx=10)
        # DIP UI
        self.tab_home = self.tab_parent.add("Home")
        self.dip_ui = DipUI(self.tab_home)
        # -------------------------------------
        self.tab_static = self.tab_parent.add("Static")
        self.static_ui = StaticUI(self.tab_static)

    def set_tab(self, tab_name):
        self.tab_parent.set(tab_name)
        if tab_name == 'Static':
            self.static_ui.implement_left_frame()



        #-------------------------------------

