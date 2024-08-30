from input_frame import my_input_frame
from notifications import my_notifications_frame

import customtkinter as CTK

class App(CTK.CTk):
    def __init__(self):
        super().__init__()

        self.title("_OpenBot_")
        self.geometry("500x800")

        #inputs frame
        self.gui_inputs_frame = my_input_frame(master=self)
        self.gui_inputs_frame.grid(row=0, column=0, padx=20, pady=20, sticky="nsew")

        
        #notif  frame
        # Get the notif value from the my_input_frame instance
        #notif = self.gui_inputs_frame.send_values()

        if hasattr(self, 'gui_notif_frame'):
            self.gui_notif_frame.destroy()
        else:
            self.gui_notif_frame = my_notifications_frame(master=self)

            #self.gui_notif_frame = my_notifications_frame(master=self,notif=notif)
            self.gui_notif_frame.grid(row=1, column=0, padx=20, pady=0, sticky="nsew")

       





app = App()
app.mainloop()
