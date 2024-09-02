import customtkinter as CTK

class my_units_input_frame(CTK.CTkFrame):
    input_length: int
    entries=[]
    notif:list
    
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)

        # add widgets onto the frame
        #
        self.inputs = ["position", "input_2", "input_3", "input_4"]
        self.input_length = len(self.inputs)

        #creatinf labels and entries
        for self.label_no in range(0,len(self.inputs)):
            self.label = CTK.CTkLabel(self, text=self.inputs[self.label_no])
            self.label.grid(row=self.label_no, column=0, pady=(10,10), padx=(10,10))

            self.entry = CTK.CTkEntry(self)
            self.entry.grid(row=self.label_no, column=1, pady=(10,10), padx=(10,10))

            self.entries.append(self.entry)
        
        self.add_units_button=CTK.CTkButton(self,text="Add")
        self.add_units_button.grid(row=self.label_no+1,column=1,pady=(10,10),command=self.add)


    def add(self):

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

        