import socket

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

portNumber = 13798
addr = ("0.0.0.0", portNumber)
sock.connect(addr)

for i in range(10):
	msg = "this is the "+str(i)+" time"
	sock.sendall(msg.encode())
	try:
		revMsg = sock.recv(1024).decode()
		print("Send: " + revMsg + "\n")
	except:
		break

sock.close() 	

