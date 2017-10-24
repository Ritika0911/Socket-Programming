import socket;
def main():
        host='127.0.0.1'
        port=8002
        
        s=socket.socket()
        s.bind((host,port))
        print "Server running successfully."
        s.listen(1)
        c, addr=s.accept()
        
        print "Connection from client :"+str(addr)
        
        while True:
            data=c.recv(1024)
            if not data:
                break;
            print "From connected user:"+str(data)
            msg=raw_input("-->")
            while msg != "Bye from server":
                c.send(msg)
                data_s=c.recv(1024)
                print "Client: "+str(data_s)
                msg=raw_input("-->")
        c.send(msg)
        data_s=c.recv(1024)
        print "Client: "+str(data_s)
        c.close()
if __name__=='__main__':
		main()
	
		
			
