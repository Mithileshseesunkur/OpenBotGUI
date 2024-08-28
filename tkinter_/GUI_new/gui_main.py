from input_frame import my_input_frame

import customtkinter as CTK

class App(CTK.CTk):
    def __init__(self):
        super().__init__()

        self.title("_OpenBot_")
        self.geometry("500x800")

        #inputs frame
        self.gui_inputs_frame = my_input_frame(master=self)
        self.gui_inputs_frame.grid(row=0, column=0, padx=20, pady=20, sticky="nsew")

       





app = App()
app.mainloop()
