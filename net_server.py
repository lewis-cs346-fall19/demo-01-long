
import socket


def main():
	
	sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

	portNumber = 13798
	addr = ("0.0.0.0", portNumber)
	sock.bind(addr)
	
	sock.listen(5)
	
	while (1):
		(connecttedSock, clientAddress) = sock.accept() 
		msg = ""
		for i in range(10):
			try:				
				msg = connecttedSock.recv(1024).decode()
				print(msg+"\n")
			except:
				connecttedSock.close()
		
			msg = "hahaha" + msg
			connecttedSock.sendall(msg.encode())
		
main()
