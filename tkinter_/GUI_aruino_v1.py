import tkinter
import tkinter as tk
import customtkinter
import numpy as np
import time
from pySerialTransfer import pySerialTransfer as txfer

# set the theme and color options

customtkinter.set_appearance_mode("dark")  # system(default), light, dark
customtkinter.set_default_color_theme("blue")

# MAIN#############################
root = customtkinter.CTk()

# title of window
root.title("Testing input")

# change according to inputs
inputs = np.array(["yellow", "blue", "red", "white"])
print(inputs)

# get inputs from entry fields
to_send = []

# what is sending
sending_list = []

# errors stored here
error_message_matrix = []

conn_avail = None


# button functions down>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

# connect function


# function to refresh frame
def clear_widgets_err_frame():
    children = frame_error.winfo_children()
    for widget in children[1:]:
        widget.destroy()


# connect and open connection
def connect():
    global link
    global conn_avail

    try:
        clear_widgets_err_frame()
    except tk.TclError:
        pass

    try:
        link = txfer.SerialTransfer('COM2')
        print("link available")
        progressbar.configure(progress_color='#5cffb6')
        progressbar.start()

        conn_avail = True


    except txfer.InvalidSerialPort:
        conn_avail = False
        print("NO LINK")

    if conn_avail:

        print("LINK!")
        link.open()
        connection_text = "Connected..."
        connection_label = customtkinter.CTkLabel(frame_error,
                                                  text=connection_text)
        connection_label.grid(row=1, column=0, sticky='W', padx=10, pady=5)
        update_send_all_button_state('normal')
        return link

    else:
        connection_error_text = "Maybe Arduino is off or USB not connected"
        connection_error_label = customtkinter.CTkLabel(frame_error,
                                                        text=connection_error_text)
        connection_error_label.grid(row=1, column=0, sticky='W', padx=10, pady=5)
        update_send_all_button_state('disabled')




def update_send_all_button_state(state):
    button_send_all.configure(state=state)


def send_all():
    clear_widgets_err_frame()

    print("---"
          "inside send_all in if conn_available"
          "---")

    send_all_error_msg = ""
    error_count = 0
    send_size = 0
    print("printing value size")

    for j, entry_field in enumerate(to_send):
        try:
            value = float(entry_field.get())

            value_size = link.tx_obj(value, send_size) - send_size
            print(value_size)
            send_size += value_size

            print(inputs[j] + ':', value)

        except ValueError:
            value = 0
            value_size = link.tx_obj(value, send_size) - send_size
            print(value_size)
            send_size += value_size

            print(inputs[j] + ':', value)
            send_all_error_msg = "Invalid format in " + inputs[j]
            error_count += 1
            send_all_input_error_label = customtkinter.CTkLabel(frame_error)
            send_all_input_error_label.configure(text=send_all_error_msg)
            send_all_input_error_label.grid(row=error_count, column=0, sticky="w",
                                            padx=10, pady=5)

    link.send(send_size)
    print(send_size)


def clear_all():  # clear all fields

    for entry_field in to_send:
        entry_field.delete(0, tk.END)
    # Clear error message label
    clear_widgets_err_frame()


# button functions up>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

# connect frame ########################################################
frame_connect = customtkinter.CTkFrame(root, border_width=1)
frame_connect.grid(row=0, column=0, padx=10,
                   pady=5, sticky="nsew")

connect_button = customtkinter.CTkButton(frame_connect, width=75,
                                         height=25,
                                         text="Connect",
                                         command=connect)
connect_button.grid(row=0, column=0, sticky="W",
                    padx=10,
                    pady=10)

# progress bar

progressbar = customtkinter.CTkProgressBar(frame_connect, orientation='horizonntal',
                                           indeterminate_speed=.5,
                                           determinate_speed=0.5,
                                           mode="indeterminate",
                                           progress_color='#6e6e6e',
                                           width=150)
progressbar.grid(row=0, column=1, padx=10, pady=10)
progressbar.set(0)
######################################################################

# Inputs Frame ########################################################
frame_inputs = customtkinter.CTkFrame(root, border_width=1)
frame_inputs.grid(row=1,
                  column=0,
                  padx=10,
                  pady=5,
                  sticky="nsew")  # Packing the frame within the root window

# for loop to create GUI
row_no = 0
for i in inputs:
    # labels
    label = customtkinter.CTkLabel(frame_inputs, text=i + ":")
    label.grid(row=row_no, column=0, sticky="E", padx=10, pady=5)

    # input fields
    entry_field = customtkinter.CTkEntry(frame_inputs)
    entry_field.grid(row=row_no, column=1, sticky="W", padx=10, pady=5)

    # button for each field
    '''button = customtkinter.CTkButton(frame_inputs, text="Send " + i, command=lambda index=row_no: send_input(index))
    button.grid(row=row_no, column=2, sticky="W", padx=10, pady=5)
    '''
    to_send.append(entry_field)
    row_no += 1
# end of for loop to create GUI
print(to_send)

# send all inputs button
button_send_all = customtkinter.CTkButton(frame_inputs, width=120,
                                          height=25, text="Send all",
                                          command=send_all, state='disabled')
button_send_all.grid(row=row_no, column=1, rowspan=2, padx=10, pady=5)

# clear all button

button_clear_all = customtkinter.CTkButton(frame_inputs, width=75, height=25,
                                           text="Clear all", command=clear_all)
button_clear_all.grid(row=row_no + 1, column=0, rowspan=2, sticky="E", padx=10, pady=5)
# print("yes")
########################################################################################
# frame error messages##################################################################

frame_error = customtkinter.CTkFrame(root, border_width=1)
frame_error.grid(row=2, column=0, padx=10, pady=10, sticky="nsew")

# frame_error title
label_error = customtkinter.CTkLabel(frame_error, text_color='#ebcf00', text="Notifications:")
label_error.grid(row=0, column=0, sticky="W", padx=10, pady=5)

# send_input error label
input_error_message = customtkinter.CTkLabel(frame_error)

# send all error message label
send_all_input_error_message = customtkinter.CTkLabel(frame_error)
#######################################################################################

root.mainloop()

# close com
try:
    link = connect()
    link.close()
    print("LINK closed")
except (txfer.InvalidSerialPort, tk.TclError, NameError):
    pass

#######to
# consider############
'''def send_input(index):  # send inputs selected

    # refresh frame_error everytime this func is called
    children = frame_error.winfo_children()
    for widget in children[1:]:
        widget.destroy()
    input_error_message = customtkinter.CTkLabel(frame_error)

    # initialise error msg
    error_msg = ""

    # try except errors
    try:
        input_error_message.configure(text="")
        value = float(to_send[index].get())
        print(inputs[index] + ":", value)
        # Here commands to send the value to Arduino
        value_bytes = struct.pack('f', value)
        # value_bytes= value.to_bytes(2, byteorder='big')
        print(value_bytes)
        print(to_send)

    except ValueError:
        input_error_message.configure(text="")
        error_msg = "Invalid format in " + inputs[index]

        input_error_message.grid(row=1, column=0, sticky="W", padx=5, pady=5)
        # input_error_message.destroy()
        input_error_message.configure(text=error_msg)
        # to correct afterward
        value = 0.0
        value_bytes = struct.pack('f', value)
        print(value_bytes)

        # ser.write(value_bytes)'''

'''
def send_all():  # send all inputs at once

    children = frame_error.winfo_children()
    for widget in children[1:]:
        widget.destroy()

    send_all_error_msg = ""
    error_count = 0

    for j, entry_field in enumerate(to_send):
        try:
            send_size = 0
            print(send_size)
            value = float(entry_field.get())

            value_size = link.tx_obj(value, send_size) - send_size
            send_size += value_size



            while not link.available():
                if link.status < 0:
                    if link.status == txfer.CRC_ERROR:
                        print("ERROR: CRC_ERROR")
                    elif link.status == txfer.PAYLOAD_ERROR:
                        print('ERROR: PAYLOAD_ERROR')
                    elif link.status == txfer.STOP_BYTE_ERROR:
                        print('ERROR: STOP_BYTE_ERROR')
                    else:
                        print('ERROR: {}'.format(link.status))
            # ser.write(value_bytes)
            threading.Thread(target=send_data, args=(value,inputs[index]))
            print(inputs[j] + ':', value)


        except ValueError:
            value = 0

            send_all_error_msg = "Invalid format in " + inputs[j]
            error_count += 1
            send_all_input_error_message = tk.Label(frame_error)
            send_all_input_error_message.config(text=send_all_error_msg, fg="red")
            send_all_input_error_message.grid(row=error_count, column=0, sticky="w", padx=10, pady=5)
            print(value)
    # error_count=0
'''
