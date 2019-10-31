#!/usr/bin/python
import crontab
import argparse
import fileinput
import sys
import ipaddress
from changer import change
from parameters import *
from cron import *


FLAGS = []

if __name__ == "__main__":

	parser = argparse.ArgumentParser()

	parser.add_argument('-c', '--critical-files',
		type=str,
		# default='True',
		help='Backup only critical log files to the server. By default, \
		only critical files are backed up')

	parser.add_argument('-i','--important-files',
		type=str,
		# default='False',
		help='')

	parser.add_argument('-a', '--all-files',
		type=str,
		# default='True',
		help='Backup all log files to the server.')

	parser.add_argument('-s', '--server-address',
		type=str,
		# default='192.168.1.101'.
		help = 'Server address should be the address to the PC running server.py file')


	parser.add_argument('-p','--port',
		type=int,
		# default=10000,
		help='The port for the server. This port must match with server.py file running \
		on the server. Default port number is 10000')

	parser.add_argument('-m', '--minute',
		type=str,
		help='Schedule minute for cronjob. Default value is 0. Should be in range of 0 to 59. Use / for every minute schedulig. * mean for each minute.')

	parser.add_argument('-H', '--hour',
		type=str,
		help='Schedule hour for cronjob. Default value is /12 i.e. every 12 hour. Range: 0-23')

	parser.add_argument('-d', '--day',
		type=str,
		help='Schedule day for cronjob. Default value is * i.e. each day. Range: 1-31')

	parser.add_argument('-M', '--month',
		type=str,
		help='Schedule month for cronjob. Default value is * i.e. each month. Range 1-12')

	FLAGS, _ = parser.parse_known_args()

	# handling critical files

	if FLAGS.critical_files:
		if CRITICAL == False:
			print('Critical log files must be backed up at any cost. Use -c=True')
			change('CRITICAL', True)
			sys.exit()
		else:
			value = FLAGS.critical_files == 'True'
			if not value:
				print('Critical log files must be backed up at any cost. Cannot set it to False')

	# handling important files:

	if FLAGS.important_files:
		if IMPORTANT == False:
			value = FLAGS.important_files == 'True'
			if value != IMPORTANT:
				if not CRITICAL:
					print('Critical files must be backed up before all files. Try using -c=True before -i=True')
					sys.exit()
				else:
					change('IMPORTANT', value)
			else:
				pass
		else:
			pass

	# handling all files
	if FLAGS.all_files:
		if ALL == False:
			value = FLAGS.all_files == 'True'
			# print(ALL, value)
			if value != ALL:
				if not IMPORTANT:
					print('''Important files must be backed up before all files. Try using -i=True before -a=True''')
					sys.exit()
				else:
					change('ALL', value)
			else:

				pass
		else:
			pass

	# changing server address
	if FLAGS.server_address:
		if HOST != FLAGS.server_address:
			try:
				address = ipaddress.ip_address(FLAGS.server_address)
			except ValueError:
				print('The server address should be a valid IPv4 address, example: 192.168.1.102')
				sys.exit()
			change('HOST', str(address))
			print('The server changed to ', address)

	# changing port
	if FLAGS.port:
		if PORT != FLAGS.port:
			change('PORT', FLAGS.port)
			print('The port changed to ', FLAGS.port)	

	# handling cronjob
	if not CRON_JOB_SCHEDULED:
		change('CRON_JOB_SCHEDULED', "True")
		add_cron_tab()
	else:
		if FLAGS.minute or FLAGS.hour or FLAGS.day or FLAGS.month:
		# print("Cron update with", FLAGS.minute, FLAGS.hour, FLAGS.day, FLAGS.month)
			if FLAGS.minute == None:FLAGS.minute="0"
			if FLAGS.hour == None: FLAGS.hour="/12"
			if FLAGS.day == None: FLAGS.day = "*"
			if FLAGS.month == None: FLAGS.month = "*"			
			update_cron_tab(minute=FLAGS.minute, hour=FLAGS.hour, day=FLAGS.day, month=FLAGS.month)
		# list_cron_tabs()
