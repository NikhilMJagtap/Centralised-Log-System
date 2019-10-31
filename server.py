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

	#while True:
	#	connection, address = soc.accept()
	#	print("Serving ", address)
	#	 
	#	if os.path.exists('./logs/'+address[0]):
	#		f = open('./logs/'+address[0]+'/log.txt', 'wb')
	#	else:
	#	
	#	while(data):
	#		f.write(data)
	#		data = connection.recv(BUFF_SIZE)
	#	f.close()
	#	connection.close()


	while True:
		connection , address = soc.accept()
		print("Serving " , address)
		idx=0
		data = connection.recv(BUFF_SIZE)
		data_ = data.decode("utf-8")
		idx = data_.find("********")
		print("Data header recieved! :" , data_)
		while idx != -1:

			if idx!=-1:
				if os.path.exists('./logs/'+address[0]):
					print("Opening file!")
					f = open('./logs/'+address[0]+data_[idx+16:]+'.txt' , "wb")
					print(data_[idx+16:])
				else:
					os.makedirs('./logs/'+address[0])
					print("Creating directory and opening file!")	
					f = open('./logs/'+address[0]+data_[idx+16:]+'.txt' , "wb")
					print(data_[idx+16:])
				data = connection.recv(BUFF_SIZE)
				data_ = data.decode("utf-8")
				#print("Recieved data")
				idx_ = data_.find("********")
				while idx_ ==-1:
					f.write(data)
					data = connection.recv(BUFF_SIZE)
					data_ = data.decode("utf-8")
					#print("Data received!")
					if data_ == "":
						idx =-1	
						break
					idx_ = data_.find("********")
					idx = idx_
				print("Data header found :" , data_)
		f.close()
		connection.close()
		print("Connection terminated!")
	#soc.close()		
					
					

	sys.exit()
 
