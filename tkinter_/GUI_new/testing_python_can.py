import can


bus1 = can.interface.Bus(channel='test1', interface='virtual')
bus2 = can.interface.Bus(channel='test1', interface='virtual')

msg1 = can.Message(arbitration_id=0xabcde, data=[1,2,3])
bus1.send(msg1)
recv1 = bus2.recv()

print(recv1)

msg=[msg1,recv1]
print("this is message sent:",msg[0])
print("this is message received:",msg[1])

bus1.shutdown()
bus2.shutdown()