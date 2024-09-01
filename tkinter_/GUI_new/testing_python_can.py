import can

bus1 = can.interface.Bus('test1', interface='virtual')
bus2 = can.interface.Bus('test2', interface='virtual')

msg1 = can.Message(arbitration_id=0xabcde, data=[1,2,3])
bus1.send(msg1)
recv1 = bus2.recv()

print(recv1)
