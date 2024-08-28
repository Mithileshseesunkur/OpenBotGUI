from input_frame import my_input_frame
import customtkinter as CTK
# ./run_app.sh

# class my_input_frame(CTK.CTkFrame):

#     input_length:int
#     entries:list=[]
#     def __init__(self, master, **kwargs):
#         super().__init__(master, **kwargs)

#         # add widgets onto the frame
#         self.inputs = ["input_1", "input_2", "input_3", "input_4"]
#         self.input_length=len(self.inputs)

        
        

#         for label_no in range(len(self.inputs)):
#             self.label = CTK.CTkLabel(self, text=self.inputs[label_no])
#             self.label.grid(row=label_no, column=0, pady=20, padx=20)

#             self.entry = CTK.CTkEntry(self)
#             self.entry.grid(row=label_no, column=1, pady=20, padx=20)
    
#             self.entries.append(self.entry)
    







class App(CTK.CTk):
    def __init__(self):
        super().__init__()

        self.title("_OpenBot_")
        self.geometry("500x800")

        self.gui_inputs_frame = my_input_frame(master=self)
        self.gui_inputs_frame.grid(row=0, column=0, padx=20, pady=20, sticky="nsew")

       





app = App()
app.mainloop()
