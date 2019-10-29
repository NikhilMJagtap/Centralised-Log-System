from socket import socket, gethostname, AF_INET, SOCK_STREAM
import sys
import os
from parameters import *

if __name__ == "__main__":

	soc = socket(AF_INET, SOCK_STREAM)
	# host = gethostname()
	soc.bind((HOST, PORT))
	soc.listen(1)
	print("Listening to ", HOST ," on port ", PORT)

	while True:
		connection, address = soc.accept()
		print("Serving ", address)
		# f = open('./log.txt', 'wb')
		if os.path.exists('./logs/'+address[0]):
			f = open('./logs/'+address[0]+'/log.txt', 'wb')
		else:
			os.makedirs('./logs/'+address[0])
			f = open('./logs/'+address[0]+'/log.txt', 'wb')
		data = connection.recv(BUFF_SIZE)
		while(data):
			f.write(data)
			data = connection.recv(BUFF_SIZE)
		f.close()
		connection.close()

	sys.exit()
