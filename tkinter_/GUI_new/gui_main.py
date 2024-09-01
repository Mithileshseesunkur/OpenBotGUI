from input_frame import my_input_frame
from notifications import my_notifications_frame
from transmitting import my_transmitting_frame
from receiving import my_receiving_frame

import customtkinter as CTK

class App(CTK.CTk):
    def __init__(self):
        super().__init__()


        self.title("_OpenBot_")
        self.geometry("1000x800")

        #inputs frame
        self.gui_inputs_frame = my_input_frame(master=self)
        self.gui_inputs_frame.grid(row=0, column=0, padx=20, pady=20, sticky="nsew")

        
        #notif  frame
        # Get the notif value from the my_input_frame instance
        #notif = self.gui_inputs_frame.send_values()

        #notif  frame
        self.gui_notif_frame = my_notifications_frame(master=self)
        self.gui_notif_frame.grid(row=1, column=0, padx=20, pady=0, sticky="nsew")

        # Bind the "Send inputs" button press event to the update_notif method
        self.gui_inputs_frame.send_button.configure(command=self.update_notif)

        #transmitting frame
        self.gui_transmitting_frame=my_transmitting_frame(master=self,width="200")
        self.gui_transmitting_frame.grid(row=0, column=1, sticky="nsew",pady=(20,20),rowspan=1)

        #receiving frame
        self.gui_receiving_frame=my_receiving_frame(master=self,width="200")
        self.gui_receiving_frame.grid(row=0, column=2, sticky="nsew",pady=(20,20),rowspan=1)

    #update notif framepip
    def update_notif(self):

    #update notif
        notif = self.gui_inputs_frame.send_values()

        # Destroy old widgets and create new ones with the new notif value
        children = self.gui_notif_frame.winfo_children()
        for widget in children[1:]:
            widget.destroy()
        self.gui_notif_frame = my_notifications_frame(master=self, notif=notif)
        self.gui_notif_frame.grid(row=1, column=0, padx=20, pady=0, sticky="nsew")
        
    #update transmissionmsg = self.gui_inputs_frame.send_recvmsg = self.gui_inputs_frame.send_recv()
        self.trans.msg=self.msg[1]

        # Destroy old widgets and create new ones with the new notif value
        children = self.gui_transmitting_frame.winfo_children()
        for widget in children[1:]:
            widget.destroy()
        self.gui_notif_frame = my_transmitting_frame(master=self, msg=msg)
        self.gui_notif_frame.grid(row=1, column=0, padx=20, pady=0, sticky="nsew")()
        self.trans.msg=self.msg[1]

        # Destroy old widgets and create new ones with the new notif value
        children = self.gui_transmitting_frame.winfo_children()
        for widget in children[1:]:
            widget.destroy()
        self.gui_notif_frame = my_transmitting_frame(master=self, msg=msg)
        self.gui_notif_frame.grid(row=1, column=0, padx=20, pady=0, sticky="nsew")
        self.msg = self.gui_inputs_frame.send_recv()
        trans_msg=self.msg[1]

        # Destroy old widgets and create new ones with the new notif value
        children = self.gui_transmitting_frame.winfo_children()
        for widget in children[1:]:
            widget.destroy()
        self.gui_notif_frame = my_transmitting_frame(master=self, trans_msg=trans_msg)
        self.gui_notif_frame.grid(row=1, column=0, padx=20, pady=0, sticky="nsew")

    def update_transmitting(self):
        msg = self.gui_inputs_frame.send_recv()
        self.trans.msg=self.msg[1]

        # Destroy old widgets and create new ones with the new notif value
        children = self.gui_transmitting_frame.winfo_children()
        for widget in children[1:]:
            widget.destroy()
        self.gui_notif_frame = my_transmitting_frame(master=self, msg=msg)
        self.gui_notif_frame.grid(row=1, column=0, padx=20, pady=0, sticky="nsew")

    def update_receiving(self):
        pass





app = App()
app.mainloop()
