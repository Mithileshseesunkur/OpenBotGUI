import customtkinter as CTK
from input_frame import my_input_frame

class my_notifications_frame(CTK.CTkFrame):
    
    height="400"
    width="800"
    notif_entries

    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)

        for label in my_input_frame.entries:

            self.label = CTK.CTkLabel(self, text=self.entries[label])
            self.label.grid(row=label, column=0, pady=20, padx=20)



        