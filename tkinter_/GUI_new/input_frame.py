import customtkinter as CTK
import can


class my_input_frame(CTK.CTkFrame):
    input_length: int
    entries=[]
    notif:list
    
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)

        # add widgets onto the frame
        self.inputs = ["input_1", "input_2", "input_3", "input_4"]
        self.input_length = len(self.inputs)

        #creatinf labels and entries
        for label_no in range(0,len(self.inputs)):
            self.label = CTK.CTkLabel(self, text=self.inputs[label_no])
            self.label.grid(row=label_no, column=0, pady=(10,10), padx=(10,10))

            self.entry = CTK.CTkEntry(self)
            self.entry.grid(row=label_no, column=1, pady=(10,10), padx=(10,10))

            self.entries.append(self.entry)
        
        # Update the frame to ensure it's drawn
        self.update_idletasks()

        # Get the frame's size
        self.width = self.winfo_width()
        self.height = self.winfo_height()
        
            
        # send all button
        self.send_button = CTK.CTkButton(self, text="Send inputs", command=None)
        self.send_button.grid(row=label_no+1, column=1, pady=20, padx=20,sticky="w")
    
    #functions must be outside of __init__ 
    #send off values at once
    def send_values(self):

        self.value_get=[]
       
        try:
            for entry_no in range(0,self.input_length):
                
                self.value=self.entries[entry_no].get() #get values from entries by order
                if self.value=="": # nothing=0
                    self.value=0
                self.value_get.append(self.value) #appendd entries in value_get
                print(f"input_{entry_no + 1}: {self.value_get[entry_no]}")
                #put send function here

            print(self.value_get)
            self.notif=[float(x) for x in self.value_get]
            print(self.notif)
            
            return self.notif    
        
        except AttributeError:
            pass

        except ValueError:

            self.notif="Incorrect type of input"
            print(self.notif)                    
            return self.notif

        self.send_recv()

    def send_recv(self):
        
        self.bus1 = can.interface.Bus(channel='test1', interface='virtual')
        self.bus2 = can.interface.Bus(channel='test1', interface='virtual')

        self.msg1 = can.Message(arbitration_id=0xabcde, data=[1,2,3])
        self.bus1.send(self.msg1)
        self.recv1 = self.bus2.recv()
        self.send_recv_msg=[self.msg1, self.recv1]

        return self.send_recv_msg

        

        