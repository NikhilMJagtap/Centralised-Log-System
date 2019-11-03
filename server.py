from socket import socket, gethostname, AF_INET, SOCK_STREAM
import sys
import os
from parameters import *


def is_data_header(data):
	"""
	Checks whether the received data is a data header or not.
	Returns file name if true
	Returns false otherwise
	"""
	file_name=""
	print(len(data))
	if data[:8] == "********":
		for char in data[17:]:
			if char!="*":
				file_name+=char
			else:
				break
		return file_name			
	return False	

def is_data_trailer(data):
	print(len(data))
	if data[:8]=="^^^^^^^^":
		return True
	return False	

if __name__ == "__main__":

	soc = socket(AF_INET, SOCK_STREAM)
	# host = gethostname()
	soc.bind((HOST, PORT))
	soc.listen(1)
	print("Listening to ", HOST ," on port ", PORT)


	# while True:
	# 	connection , address = soc.accept()
	# 	print("Serving " , address)
	# 	idx=0
	# 	data = connection.recv(BUFF_SIZE)
	# 	data_ = data.decode("utf-8")
	# 	idx = data_.find("********")
	# 	print("Data header recieved! :" , data_)
	# 	while idx != -1:

	# 		if idx!=-1:
	# 			if os.path.exists('./logs/'+address[0]):
	# 				print("Opening file!")
	# 				i = data_.find("log")
	# 				f = open('./logs/'+address[0]+data_[idx+16:i+3]+'.txt' , "wb")
	# 				print(data_[idx+16:i+3])
	# 				f.write(data_[i+3:])
	# 			else:
	# 				os.makedirs('./logs/'+address[0])
	# 				i = data_.find("log")
	# 				print("Creating directory and opening file!")	
	# 				f = open('./logs/'+address[0]+data_[idx+16:i+3]+'.txt' , "wb")
	# 				print(data_[idx+16:i+3])
	# 			data = connection.recv(BUFF_SIZE)
	# 			data_ = data.decode("utf-8")
	# 			#print("Recieved data")
	# 			idx_ = data_.find("********")
	# 			while idx_ ==-1:
	# 				f.write(data)
	# 				data = connection.recv(BUFF_SIZE)
	# 				data_ = data.decode("utf-8")
	# 				#print("Data received!")
	# 				if data_ == "":
	# 					idx =-1	
	# 					break
	# 				idx_ = data_.find("********")
	# 				idx = idx_
	# 			print("Data header found :" , data_)
	# 	f.close()
	# 	connection.close()
	# 	print("Connection terminated!")
	# #soc.close()		
					

	while True:
		connection , address = soc.accept()
		print("Serving " , address)
		while True:          #iterates for each file received	
			data = connection.recv(BUFF_SIZE)
			data_ = data.decode("utf-8")

			data_header = is_data_header(data_)
			if data_header!=False:
				file_name = data_header
				print("File name :" , file_name)
				if os.path.exists('./logs/'+address[0]):
						print("Opening file!")
						f = open('./logs/'+address[0]+"/"+file_name+'.txt' , "wb")
						print("Opened file!")
						# print(data_[idx+16:i+3])
						# f.write(data_[i+3:])
				else:
					os.makedirs('./logs/'+address[0])
					# i = data_.find("log")
					print("Creating directory and opening file!")	
					f = open('./logs/'+address[0]+"/"+file_name+'.txt' , "wb")

				while True:
					data = connection.recv(BUFF_SIZE)
					data_ = data.decode("utf-8")
					is_trailer = is_data_trailer(data_)

					if is_trailer==True:
						f.close()
						break
					else:
						f.write(data)	
			else:
				print("First message not data header!")
				break
			
		# f.close()
		# connection.close()
	sys.exit()
 
