import customtkinter as ctk


class MenuDev(ctk.CTkFrame):
    open_status = False

    def __init__(self, parent, image, _global, values,**kwargs):
        self._global = _global
        self.values = values
        super().__init__(parent, **kwargs)
        self.pack(side="right")


        self.button_avatar = ctk.CTkButton(self, 
                                           text="",
                                           width=30, 
                                           image=image,
                                           fg_color="#131313",
                                           hover_color="#1d1d1d",
                                           command=self.show_menu
                                           )
        
        self.button_avatar.pack(side="right", padx=5, pady=5)

    def show_menu(self):
        if self.open_status:
            self.open_status = False
            if hasattr(self, "menu_frame"):
                self.menu_frame.destroy()
        else:
            if hasattr(self, "menu_frame"):
                self.menu_frame.destroy()
            self.open_status = True
            self.menu_frame = ctk.CTkFrame(self._global)
            self.menu_frame.place(x=1250, y=50)

            for value in self.values:
                button_option= ctk.CTkButton(self.menu_frame, text=value, fg_color="#131313", hover_color="#1d1d1d")
                button_option.pack(fill="x", pady=5, padx=5)




     