import socket
import time
import pickle


HEADERSIZE = 10

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((socket.gethostname(), 1234))
s.listen(5)

while True:
	clientsocket, address = s.accept()
	print(f"Connection from {address} has been created!")

	d = {1: "Hey", 2: "There"}
	msg = pickle.dumps(d)
	#print(msg)



	msg = bytes(f'{len(msg):<{HEADERSIZE}}', "utf-8") + msg



	clientsocket.send(bytes(msg))

	#while True:
		#time.sleep(3)
		#msg = f"The time is! {time.time()}"
		#msg = f'{len(msg):<{HEADERSIZE}}' + msg
		#clientsocket.send(bytes(msg, "utf-8"))




