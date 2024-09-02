import customtkinter as CTK
from units_tab_input import my_units_input_frame

class my_tabs(CTK.CTkTabview):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)

        # create tabs
        self.add("Units")
        self.add("Shape")

        # add widgets or frames on the tabs
        self.gui_input_frame = my_units_input_frame(master=self.tab("Units"))
        self.gui_input_frame.grid(row=0, column=0, padx=20, pady=10)

        #self.gui_input_frame = my_units_input_frame(master=self.tab("Shape"))
        #self.gui_input_frame.grid(row=0, column=0, padx=20, pady=10)