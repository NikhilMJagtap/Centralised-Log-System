import fileinput

def change(param, new_value, file='parameters.py'):

	'''
	this is to change the value of parameter in parameters.py file
	It can be done in various ways but I am changing the line which 
	is to be changed.
	'''

	for line in fileinput.input(file, inplace=True):
		# if server address is being changed, it should be
		# surrounded with quotes
		if param == 'HOST':
			if line.startswith(param+' '):
				print(param+' = '+"'"+new_value+	"'")
			else:
				print(line.strip())
		# for other parameters
		else:
			if line.startswith(param+' '):
				print(param+' = '+new_value)
			else:
				print(line.strip())
	
