import customtkinter as CTK

class my_input_frame(CTK.CTkFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)

        # add widgets onto the frame
        inputs = ["input_1", "input_2", "input_3", "input_4"]

        for i in range(len(inputs)):
            self.label = CTK.CTkLabel(self, text=inputs[i])
            self.label.grid(row=i, column=0, pady=20, padx=20)
