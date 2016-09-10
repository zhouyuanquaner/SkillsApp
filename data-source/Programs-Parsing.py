#!/usr/bin/env python
# -*- coding: utf-8 -*-
import csv
import time
import datetime
from datetime import datetime, date, timedelta


def program_info():
	f_program = open("/Users/Tammy/Desktop/ProgramsInfo.csv", 'w')
	outputWriter = csv.writer(f_program)
	reader = csv.reader(open("/Users/Tammy/Downloads/parsed_for_yuan.csv"), 
		quotechar='"', delimiter=',', quoting=csv.QUOTE_ALL, skipinitialspace=True)
	for l in reader: 
		ll1 = l[:6]
		ll2= l[9:58]
		ll = ll1 + ll2
		outputWriter.writerow(ll)
	f_program.close()

def program_time():
	f_program = open("/Users/Tammy/Desktop/ProgramsTime.csv", 'w')
	outputWriter = csv.writer(f_program)
	f_source = open("/Users/Tammy/Downloads/parsed_for_yuan.csv")
	reader = csv.reader(f_source, 
		quotechar='"', delimiter=',', quoting=csv.QUOTE_ALL, skipinitialspace=True)
	for l in reader: 
		ll1 = l[6:9]
		ll2= l[58:]
		name = l[1:2]
		ll = name + ll1 + ll2
		outputWriter.writerow(ll)
	f_program.close()

def validate_date(date_text):
	try:
		datetime.strptime(date_text, '%A, %B %d, %Y')
		return True
	except ValueError:
		return False

def validate_time(text):
	try:
		time.strptime(text, '%I:%M %p')
		return True
	except ValueError:
		return False

def process_time(l):
	# reader = csv.reader(open("/Users/Tammy/Desktop/ProgramsTime.csv"))
	# f = open("/Users/Tammy/Desktop/ProgramsTime2.csv", 'w')
	# writer = csv.writer(f)
	# for l in reader:
	if l[2].find('-') > -1: # means that it have duration infomation 
		index = l[2].index('-')
		start = l[2][:index]
		end = l[2][index + 1:]
		# process start time
		# if it is standard format, do nothing
		if not (validate_time(start) or validate_time(start[:-1])):
			# 1. Like '10', only have hour
			if start.isdigit():
				start = start + ':00 ' + l[2][-2:]
			else:
				#2. like "10:30" have hours and minutes but no am or pm
				try:
					time.strptime(start, '%I:%M')
					start = start + " " + l[2][-2:]
				except ValueError:
					# 3. Like "10AM", have hour and am or pm but no minute
					try:
						time.strptime(start, '%I%p')
						start = start[:-2] + ":00 " + start[-2:]
					except ValueError:
						print start
						raise ValueError
		if start[-1] == " ":
			start = start[:-1]
		l[2] = start
		s = datetime.strptime(start, '%I:%M %p')

		# process end time
		if end[0] == " ":
			end = end[1:]		
		if not validate_time(end):
			# 1. like "3pm", only have hour and am or pm but no minute
			try:
				time.strptime(end, '%I%p')
				end = end[:-2] + ":00 " + end[-2:]
			except ValueError:
				# 2. like "8:00 pm", just lack one space
				try:
					time.strptime(end, '%I:%M%p')
					end = end[:-2] + " " + end[-2:]
				except ValueError:
					raise ValueError
		e = datetime.strptime(end, '%I:%M %p')
		duration = e - s
		print len(l)
		l[6] = str(duration)
	return l

def process_date():
	week_s = ['Mondays','Tuesdays', 'Wednesdays', 'Thursdays', 'Fridays', 'Saturdays', 'Sundays']
	week = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
	f_source = open("/Users/Tammy/Desktop/ProgramsTime.csv")
	reader = csv.reader(f_source)
	f = open("/Users/Tammy/Desktop/ProgramsTime2.csv", 'w')
	writer = csv.writer(f)
	c = 0
	for l in reader:
		if l[4] == '':
			date1 = l[1]
			date2 = l[1]
			# 1. without year, we have "Weekday, Month Date" but lack of year
			try:
				date_shown = datetime.strptime(l[1], '%A, %B %d')
				today = datetime.strptime('Thursday, September 1', '%A, %B %d')
				if today > date_shown:
					date1 = date1 + ", 2017"
				else:
					date1 = date1 + ", 2016"
			except ValueError:
				c = c + 1
				# 2. Have date like "Month Date" but do not have year and weekday
				try:
					date_shown = datetime.strptime(l[1], '%B %d')
					today = datetime.strptime('September 1', '%B %d')
					if today > date_shown:
						date1 = date1 + ", 2017"
					else:
						date1 = date1 + ", 2016"
					date1 = week[date_shown.weekday()] + ', ' + date1
				except ValueError:
					# 3. Have date like "August 8, 2016" but do not have weekday
					try:
						date_shown = datetime.strptime(l[1], '%B %d, %Y')
						date1 = week[date_shown.weekday()] + ', ' + l[1]
					except ValueError:
						# 4. contains a '-' like April 1-3, 2016
						if l[1].find('-') > -1:
							index = l[1].index('-')
							start = l[1][index - 1]
							end = l[1][index + 1]
							year = l[1][-4:]
							print l[1]
							index_mon_end = l[1].index(' ')
							mon = l[1][0: index_mon_end]
							for i in range (int(start), int(end)):
								date_shown = datetime.strptime(mon + ' ' + str(i) + ', ' + year, '%B %d, %Y')
								date1 = week[date_shown.weekday()] + ', ' + mon + ' ' + str(i) + ', ' + year
								l[1] = date1
								l[4] = date1
								l[5] = "TRUE"
								writer.writerow(l)
							date_shown = datetime.strptime(mon + ' ' + end + ', ' + year, '%B %d, %Y')
							date1 = week[date_shown.weekday()] + ', ' + mon + ' ' + end + ', ' + year
						else:
							c = c + 1
			if validate_date(date1) == True:
				l[1] = date1
				l[4] = date1
				l[5] = "TRUE"
		print l
		l = process_time(l)
		writer.writerow(l)
	f.close()
	f_source.close()


def check_result():
	f = open("/Users/Tammy/Documents/SkillsApp/ProgramsTime2 copy.csv")
	reader = csv.reader(f)
	cnt = 0
	for l in reader:
		cnt += 1
		if not validate_time(l[2]):
			print l
		if not validate_date(l[4]):
			print l[1]
	print cnt
	f.close()

def weekday_triggers():
	def get_dates(weekday):
		oneday = timedelta(days=1)
		oneweek = timedelta(days=7)
		year = 2016
		start = date(year=year, month=9, day=1)
		while start.weekday() != weekday:
			start += oneday

		days = []
		while start.year == year:
			days.append(start.strftime('%A, %B %d, %Y'))
			start += oneweek

		return days
	# open the files and process those only contain non-standard format like "Mondays, Tuesdays"
	# this file can only be used for later front-end trigger
	f_source = open("/Users/Tammy/Documents/SkillsApp/ProgramsTime2.csv")
	reader = csv.reader(f_source)
	f = open("/Users/Tammy/Documents/SkillsApp/ProgramsTime2 copy.csv", 'w')
	writer = csv.writer(f)

	mon = get_dates(0)
	tue = get_dates(1)
	wed = get_dates(2)
	thu = get_dates(3)
	fri = get_dates(4)
	sat = get_dates(5)
	sun = get_dates(6)
	for l in reader:
		if l[5] != 'TRUE':
			if l[1].find('First') > -1:
				print l[0] + ': ' + l[1]
			if l[1].find('Mondays') > -1:
				for d in mon:
					l[5] = 'TRUE'
					l[4] = d
					writer.writerow(l)
			if l[1].find('Tuesdays') > -1:
				for d in tue:
					l[5] = 'TRUE'
					l[4] = d
					writer.writerow(l)
			if l[1].find('Wednesdays') > -1:
				for d in wed:
					l[5] = 'TRUE'
					l[4] = d
					writer.writerow(l)
			if l[1].find('Thursdays') > -1:
				for d in thu:
					l[5] = 'TRUE'
					l[4] = d
					writer.writerow(l)
			if l[1].find('Fridays') > -1:
				for d in fri:
					l[5] = 'TRUE'
					l[4] = d
					writer.writerow(l)
			if l[1].find('Saturdays') > -1:
				for d in sat:
					l[5] = 'TRUE'
					l[4] = d
					writer.writerow(l)
			if l[1].find('Sundays') > -1:
				for d in sun:
					l[5] = 'TRUE'
					l[4] = d
					writer.writerow(l)
		else:
			writer.writerow(l)
	f.close()
	f_source.close()


if __name__ == '__main__':
	# program_info()
	# program_time()
	# process_date()
	# process_time()
	check_result()
	# weekday_triggers()