import socket

def main():
	host='127.0.0.1'
	port=8002
	
	s=socket.socket()
	s.connect((host,port))
	message=raw_input("-->")
	while message !="Bye from client":
		s.send(message)
		data=s.recv(1024)
		print "Server: "+str(data)
		message=raw_input("-->")
	s.send(message)
	data=s.recv(1024)
	print "Server: "+str(data)
	s.close()
        
if __name__=='__main__':
        main()
