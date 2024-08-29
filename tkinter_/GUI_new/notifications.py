import customtkinter as CTK
from input_frame import my_input_frame


class my_notifications_frame(CTK.CTkFrame):
    
    height="400"
    width="800"

    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)

        self.gui_inputs_frame = my_input_frame(master=self)

        if 

        self.notif=self.gui_inputs_frame.send_values()
        

        for i, value in enumerate(self.notif):
            label = CTK.CTkLabel(self, text=str(value))
            label.grid(row=i, column=0, padx=20, pady=20)



# # Create an instance of the my_input_frame class
# input_frame_instance = my_input_frame(aiter)

# # Create an instance of the my_notifications_frame class and pass the input_frame_instance to it
# notifications_frame_instance = my_notifications_frame(aiter, input_frame_instance)  