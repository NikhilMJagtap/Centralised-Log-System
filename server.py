from socket import socket, gethostname, AF_INET, SOCK_STREAM
import sys
from parameters import *

if __name__ == "__main__":

	soc = socket(AF_INET, SOCK_STREAM)
	# host = gethostname()
	soc.bind((HOST, PORT))
	soc.listen()
	print("Listening to ", HOST ," on port ", PORT)

	while True:
		connection, address = soc.accept()
		print("Serving ", address)
		f = open('log.txt', 'wb')
		data = connection.recv(BUFF_SIZE)
		while(data):
			f.write(data)
			data = connection.recv(BUFF_SIZE)
		f.close()
		connection.close()

	sys.exit()
