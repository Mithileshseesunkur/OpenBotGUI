import tkinter as tk
import numpy as np
import serial
import time

root = tk.Tk()

# title of window
root.title("Testing input")

#change according to inputs
inputs = ["yellow", "blue", "red", "white"]

#open serial connection
ser=serial.Serial('COM3',9600)

#wait for arduino to reset
time.sleep(1)


# initial settings
entry_fields = []  # List to store entry fields
error_message_matrix = []


#functions down>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
def send_input(index):  # send inputs selected

    # refresh frame_error everytime this func is called
    children = frame_error.winfo_children()
    for widget in children[1:]:
        widget.destroy()
    input_error_message = tk.Label(frame_error)

    # initialise error msg
    error_msg = ""

    #try except errors
    try:
        input_error_message.config(text="")
        value = float(entry_fields[index].get())
        print(inputs[index] + ":", value)
        # Here commands to send the value to Arduino
        value_to_arduino=bytes(value)
        ser.write(value_to_arduino)

    except ValueError:
        input_error_message.config(text="")
        error_msg = "Invalid format in " + inputs[index]

        input_error_message.grid(row=1, column=0, sticky="W", padx=5, pady=5)
        # input_error_message.destroy()
        input_error_message.config(text=error_msg)
        input_error_message.config(fg="red")


def send_all(): #send all inputs at once

    children = frame_error.winfo_children()
    for widget in children[1:]:
        widget.destroy()

    send_all_error_msg = ""
    error_count = 0

    for j, entry_field in enumerate(entry_fields):
        try:
            value = float(entry_field.get())

            print(inputs[j] + ':', value)


        except ValueError:
            send_all_error_msg = "Invalid format in " + inputs[j]
            #error_count += 1
            send_all_input_error_message = tk.Label(frame_error)
            send_all_input_error_message.config(text=send_all_error_msg,fg="red")
            send_all_input_error_message.grid(row=error_count, column=0, sticky="w", padx=10, pady=5)

    # error_count=0


def clear_all():# clear all fields

    for entry_field in entry_fields:
        entry_field.delete(0, tk.END)
    # Clear error message label

    children = frame_error.winfo_children()
    for widget in children[1:]:
        widget.destroy()


#functions up>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

# Inputs Frame#########################
frame_inputs = tk.Frame(root, borderwidth=1, relief="groove")
frame_inputs.grid(row=0, column=0, padx=10, pady=5, sticky="nsew")  # Packing the frame within the root window

# for loop to create GUI
row_no = 0
for i in inputs:
    label = tk.Label(frame_inputs, text=i + ":")
    label.grid(row=row_no, column=0, sticky="W", padx=10, pady=5)

    entry_field = tk.Entry(frame_inputs)
    entry_field.grid(row=row_no, column=1, sticky="W", padx=10, pady=5)

    button = tk.Button(frame_inputs, text="Send " + i, command=lambda index=row_no: send_input(index))
    button.grid(row=row_no, column=2, sticky="W", padx=10, pady=5)
    entry_fields.append(entry_field)
    row_no += 1
# end of for loop to create GUI


# send all inputs button

button_send_all = tk.Button(frame_inputs, text="Send all", command=send_all)
button_send_all.grid(row=row_no + 1, column=2, sticky="W", padx=10, pady=5)

# clear all button

button_clear_all = tk.Button(frame_inputs, text="Clear all", command=clear_all)
button_clear_all.grid(row=row_no + 1, column=0, sticky="W", padx=10, pady=5)
# print("yes")

# frame error messages>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

frame_error = tk.Frame(root, borderwidth=1, relief="groove")
frame_error.grid(row=1, column=0, padx=10, pady=10, sticky="nsew")

# frame_error title
label_error = tk.Label(frame_error, text="Error messages:")
label_error.grid(row=0, column=0, sticky="W", padx=10, pady=5)

# send_input error label
input_error_message = tk.Label(frame_error)

# send all error message label
send_all_input_error_message = tk.Label(frame_error)
# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
root.mainloop()

ser.close()