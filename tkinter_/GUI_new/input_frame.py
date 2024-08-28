import customtkinter as CTK

class my_input_frame(CTK.CTkFrame):
    input_length: int
    entries: list = []

    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)

        # add widgets onto the frame
        self.inputs = ["input_1", "input_2", "input_3", "input_4"]
        self.input_length = len(self.inputs)

        for label_no in range(len(self.inputs)):
            self.label = CTK.CTkLabel(self, text=self.inputs[label_no])
            self.label.grid(row=label_no, column=0, pady=20, padx=20)

            self.entry = CTK.CTkEntry(self)
            self.entry.grid(row=label_no, column=1, pady=20, padx=20)

            self.entries.append(self.entry)

        def print_values():
            
            for entry_no in range(input_frame.input_length):
                value = input_frame.entries[entry_no].get()
                print(f"input_{entry_no + 1}: {value}")

        self.send_button = CTK.CTkButton(self, text="Send inputs", command=print_inputs)
        self.send_button.grid(row=label_no+1, column=0, pady=20, padx=20)