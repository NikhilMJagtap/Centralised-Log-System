import crontab
from crontab import CronTab as C
import os
import sys
import pwd

COMMAND = "./opt/Centralised-Log-System/init.py"

'''
crontab syntax:
Minute Hour Day Month Day_of_the_Week
Minute  0 to 59
Hour    0 to 23
Day    	1 to 31
Month   1 to 12
Day_of_the_Week  0 to 6

for each:
, comma to seperate multiple values
- hyphen for range
* asterisk for all values
/ slash for every

'''

def get_user_name():
	return pwd.getpwuid(os.getuid())[0]

# add a new crontab
# this is by default done with schedule: first minute, every 12 hours, all days, all months
def add_cron_tab():
	cron = C(user=True)
	job = cron.new(command=COMMAND)
	job.minute.on(0)
	job.hour.every(12)
	job.enable()
	cron.write()

def reschedule_to_def():
	cron = C(user=True)
	jobs = cron.find_command(command=COMMAND)
	for job in jobs:
		job.clear()
		job.minute.on(0)
		job.hour.every(12)
		job.enable()
	cron.write()

# update the cronjob with command
def update_cron_tab(user=True, minute='0', hour='/12', day='*', month='*'):
	print("Updating job...")
	cron = C(user=True)
	jobs = cron.find_command(command=COMMAND)
	x = sum(1 for job in jobs)
	if x<=0:
		print("No cronjob exist. Rescheduling default cronjob...")
		add_cron_tab()
		sys.exit()
	elif x > 1:
		print("Multiple crontabs for same are found! All will be replaced by same schedule!")

	# TODO: should iterate over jobs and not cron
	for job in cron:
		job.clear()
		
		# handling minute
		if minute=='*':
			pass
		elif minute.startswith("/"):
			minute = minute[1:]
			try:
				minute = int(minute)
			except:
				print("Expecting integer after /. Cronjob will be set to default.")
				reschedule_to_def()
				sys.exit()
			if minute<0 or minute>59:
				print("Minute value should be in the range 0 - 59. Cronjob will be set to default")
				reschedule_to_def()
				sys.exit()
			else:
				job.minute.every(minute)
		else:
			try:
				minute = int(minute)
			except:
				print("Minute value should be integer in the range 0 - 59. Cronjob will be set to default")
				reschedule_to_def()
				sys.exit()
			if minute<0 or minute>59:
				print("Minute value should be in the range 0 - 59. Cronjob will be set to default")
				reschedule_to_def()
				sys.exit()
			else:
				job.minute.on(minute)

		# updating hour
		if hour=="*":
			pass
		elif hour.startswith("/"):
			hour = hour[1:]
			try:
				hour = int(hour)
			except:
				print("Expecting integer after /. Cronjob will be set to default.")
				reschedule_to_def()
				sys.exit()
			if hour<1 or hour>23:
				print("Hour should be in range 1-23. Cronjob will be set to default")
				reschedule_to_def()
				sys.exit()
			else:
				job.hour.every(hour)
		else:
			try:
				hour = int(hour)
			except:
				print("Hour value must be an integer in range 1-23. Cronjob will be set to default")
				reschedule_to_def()
				sys.exit()
			if hour<1 or hour>23:
				print("Hour should be in range 1-23. Cronjob will be set to default")
				reschedule_to_def()
				sys.exit()
			else:
				job.hour.on(hour)

		# updating day
		if day=="*":
			pass
		elif day.startswith("/"):
			day = day[1:]
			try:
				day = int(day)
			except:
				print("Expecting integer after /. Cronjob will be set to default.")
				reschedule_to_def()
				sys.exit()
			if day<0 or day>6:
				print("Day should be in range 0-6. Cronjob will be set to default")
				reschedule_to_def()
				sys.exit()
			else:
				job.day.every(day)
		else:
			try:
				day = int(day)
			except:
				print("Day value must be an integer in range 0-6. Cronjob will be set to default")
				reschedule_to_def()
				sys.exit()
			if day<0 or day>6:
				print("Day should be in range 0-6. Cronjob will be set to default")
				reschedule_to_def()
				sys.exit()
			else:
				job.day.on(day)

		# updating month
		if month=="*":
			pass
		elif month.startswith("/"):
			month = month[1:]
			try:
				month = int(month)
			except:
				print("Expecting integer after /. Cronjob will be set to default.")
				reschedule_to_def()
				sys.exit()
			if month<1 or month>12:
				print("Month should be in range 1-12. Cronjob will be set to default")
				reschedule_to_def()
				sys.exit()
			else:
				job.month.every(month)
		else:
			try:
				month = int(month)
			except:
				print("Month value must be an integer in range 1-12. Cronjob will be set to default")
				reschedule_to_def()
				sys.exit()
			if month<1 or month>12:
				print("Month should be in range 1-12. Cronjob will be set to default")
				reschedule_to_def()
				sys.exit()
			else:
				job.month.on(month)

		job.enable()
	# writing the job
	cron.write()

# list the tabs for current user
def list_cron_tabs():
	cron = C(user=get_user_name())
	jobs = cron.find_command(command=COMMAND)
	for job in jobs:
		print(job)


if __name__ == "__main__":
	update_cron_tab(minute="3", hour="*", day="*", month="*")
	list_cron_tabs()