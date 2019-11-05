from parameters import *
from socket import socket, gethostname, AF_INET, SOCK_STREAM
import sys
import time
print("Executing client.py")


def create_data_header(file):
	"""
	Creates a data header for a given file name
	"""
	file_name_length = len(file)
	data_header = "*"*8 + file + "*"*(BUFF_SIZE-file_name_length-8)
	return data_header

def create_data_trailer(file):
	return "^"*8 + file + "^"*(BUFF_SIZE-len(file)-8)

def pad(data):
	if len(data) == BUFF_SIZE:
		print(len(data))
		return data
	else:
		print(len(data))
		data_length = len(data)
		data_ = str(data)
		data_+=" "*(BUFF_SIZE - data_length)
		print("Length padded :",BUFF_SIZE - data_length)
		return data_.encode('utf-8')

if __name__ == '__main__':
	
	soc = socket(AF_INET, SOCK_STREAM)
	try:
		soc.connect((HOST, PORT))
	except:
		print("Connection refused!")
		sys.exit()

	if CRITICAL:
		# senf critical files
		for file in CRITICAL_FILES:
			print("Sending ", file)
			
			try:
				f = open(file, 'rb')
			except:
				print("Failed read file", file)
				continue

			# data_header = "********" + file
			data_header = create_data_header(file)
			soc.send(data_header.encode('utf-8'))
			print("Sending ",file," header")
				
			data = f.read(BUFF_SIZE)
			#time.sleep(0.5)
			while data:
				print("Sending contents of ",file)
				soc.send(pad(data))
				data = f.read(BUFF_SIZE)
			data_trailer = create_data_trailer(file)
			soc.send(data_trailer.encode('utf-8'))
			print("Sending trailer of ",file)
			f.close()


	if IMPORTANT:
		# send important files
		for file in IMPORTANT_FILES:
			print("Sending ", file)
			
			try:
				f = open(file, 'rb')
			except:
				print("Failed read file", file)
				continue
			# data_header = "********" + file
			data_header = create_data_header(file)
			soc.send(data_header.encode('utf-8'))
			print("Sending ",file," header")

			data = f.read(BUFF_SIZE)
			#time.sleep(0.5)
			while data:
				print("Sending contents of ",file)
				soc.send(pad(data))
				data = f.read(BUFF_SIZE)
			data_trailer = create_data_trailer(file)
			soc.send(data_trailer.encode('utf-8'))	
			print("Sending trailer of ",file)
			f.close()

	if ALL:
		# send important files
		for file in ALL_FILES:
			print("Sending ", file)
			
			try:
				f = open(file, 'rb')
			except:
				print("Failed read file", file)
				continue

			# data_header = "********" + file
			data_header = create_data_header(file)
			soc.send(data_header.encode('utf-8'))
			print("Sending ",file," header")

			data = f.read(BUFF_SIZE)
			while data:
				print("Sending contents of ",file)
				soc.send(pad(data))
				data = f.read(BUFF_SIZE)
			data_trailer = create_data_trailer(file)
			soc.send(data_trailer.encode('utf-8'))
			print("Sending trailer of ",file)
			f.close()	

	soc.close()
	sys.exit()


