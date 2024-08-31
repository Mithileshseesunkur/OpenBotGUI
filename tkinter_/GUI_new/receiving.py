from typing import Any, Tuple
import customtkinter as CTK


class my_receiving_frame(CTK.CTkScrollableFrame):
    # def __init__(self, master: Any, width: int = 200, height: int = 200, corner_radius: int | str | None = None, border_width: int | str | None = None, bg_color: str | Tuple[str, str] = "transparent", fg_color: str | Tuple[str, str] | None = None, border_color: str | Tuple[str, str] | None = None, background_corner_colors: Tuple[str | Tuple[str, str]] | None = None, overwrite_preferred_drawing_method: str | None = None, **kwargs):
    #     super().__init__(master, width, height, corner_radius, border_width, bg_color, fg_color, border_color, background_corner_colors, overwrite_preferred_drawing_method, **kwargs)
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)

        self.label=CTK.CTkLabel(self,text="Receiving",text_color="#53c03f")
        self.label.grid(row=0,column=0, padx=20, pady=(10,10),sticky="w")


