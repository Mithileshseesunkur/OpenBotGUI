import customtkinter as CTK
from input_frame import my_input_frame

class my_notifications_frame(CTK.CTkFrame):
    
    height="400"
    width="800"
    #notif= my_input_frame.notif

    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)

        self.notif = my_input_frame.get_notif()

        for label in self.notif:

            self.label = CTK.CTkLabel(self, text=self.notif[label])
            self.label.grid(row=label, column=0, pady=20, padx=20)



# # Create an instance of the my_input_frame class
# input_frame_instance = my_input_frame(aiter)

# # Create an instance of the my_notifications_frame class and pass the input_frame_instance to it
# notifications_frame_instance = my_notifications_frame(aiter, input_frame_instance)  