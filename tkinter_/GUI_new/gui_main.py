#from input_frame import my_input_frame
import customtkinter as CTK

class my_input_frame(CTK.CTkFrame):

    input_length:int
    entries:list=[]
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)

        # add widgets onto the frame
        self.inputs = ["input_1", "input_2", "input_3", "input_4"]
        self.input_length=len(self.inputs)

        
        

        for label_no in range(len(self.inputs)):
            self.label = CTK.CTkLabel(self, text=self.inputs[label_no])
            self.label.grid(row=label_no, column=0, pady=20, padx=20)

            self.entry = CTK.CTkEntry(self)
            self.entry.grid(row=label_no, column=1, pady=20, padx=20)
    
            self.entries.append(self.entry)
    

class my_send_button_frame(CTK.CTkFrame):
    
    
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)

        
        #self.inputs=

        #self.input_frame = my_input_frame

        def print_inputs():

            for entry_no in range(0,my_input_frame.input_length):
                value=my_input_frame.entries.get()
                print("input_" + str(entry_no)+f": {value}")
                

        self.send_button = CTK.CTkButton(self, text="Send inputs", command=print_inputs)
        self.send_button.grid(row=0, column=0, pady=20, padx=20)





class App(CTK.CTk):
    def __init__(self):
        super().__init__()

        self.title("_OpenBot_")
        self.geometry("500x800")

        self.gui_inputs_frame = my_input_frame(master=self)
        self.gui_inputs_frame.grid(row=0, column=0, padx=20, pady=20, sticky="nsew")

        self.gui_send_button_frame = my_send_button_frame(master=self)
        self.gui_send_button_frame.grid(row=1, column=0, padx=20, pady=20, sticky="nsew")





app = App()
app.mainloop()
