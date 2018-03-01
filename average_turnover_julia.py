#!/usr/bin/env python
# -*- coding: utf-8 -*- 
# 180227
# author: Linnea Lindahl and Julia Liu
from xlrd import open_workbook
import datetime as dt
from datetime import *

def average_turnover_and_attendence_in_window(data, date, plus_minus_days):
	"""
	returns the average turnover per movie and average attendence per movie in the window.
	the windows is defined as the given date +/- the given days.
	Example:

	average_turnover_and_attendence_in_window(data=the_raw_data, date="02-20", plus_minus_days=7)
	should return the average numbers for the window of February to February 27.
	"""
	movie_list=read_file(data)

	date_list=date_to_check(date, plus_minus_days, movie_list)
	
	average_turnover_per_movie_in_window=None
	average_attendence_per_movie_in_window=None

	return (average_turnover_per_movie_in_window, average_attendence_per_movie_in_window)

def read_file(file_name):
	movie_list=[]
	file_object=open_workbook("svensk_bio_index.xlsx")
	for r in file_object.sheets():
		for row in range(1, r.nrows):
			movie=Movie(r.cell(row,1).value, r.cell(row,5).value, r.cell(row,3).value, r.cell(row,3).value, r.cell(row,5).value)
			movie_list.append(movie)
			#xlrd.xldate.xldate_as_datetime(xldate, 1)
	return movie_list

def date_to_check(date, plus_minus_days, month_length):
	year = input("Choose year: ")
	month = input("Choose month: ")
	day = input("Choose day: ")
	plus_minus_days = input("Choose plus_minus_days: ")

	temp = dt.datetime(1899, 12, 30)
	date1 = dt.datetime(year, month, day)

	print "Searched date: "
	print date1
	delta = date1 - temp

	print "Searched date converted to Excel serial: "
	print delta

	lower_bound = date1 - timedelta(days=plus_minus_days)
	print "Lower bound: "
	print lower_bound

	upper_bound = date1 + timedelta(days=plus_minus_days)
	print "Upper bound: "
	print upper_bound

	"""right_movies = []
	if movie.movie_date > lower_bound and movie_date < upper_bound:
		right_movies.append(movie)"""
	
	#no = (float(delta.days) + (float(delta.seconds) / 86400))
    #print no
	#month_length=month_length(month) #returns length of month
	"""range_of_date = (range(day-plus_minus_days, day + plus_minus_days, 1))
	print range_of_date

	L_bound = day - plus_minus_days
	U_bound = day + plus_minus_days - 1
	print L_bound, U_bound
	return L_bound, U_bound"""

	"""
	Calculates the intervall from the given parameters.
	returns a list of date to check
	"""

class Movie:

	def __init__(self, title, movie_date, turnover, attendence, date_index):
		self.title=title
		self.movie_date=movie_date #gives the date in form YYYY-MM-DD
		self.turnover=int(turnover)
		self.attendence=int(attendence)
		self.date_month = movie_date[5:7] #returns the date in form MM
		self.date_day = movie_date[8:10] #returns the date in form DD
		self.date_index = date_index #date in the format date value

"""
	def get_title(self):
		return self.title

	def get_date(self):
		return self.date

	def get_turnover(self):
		return self.turnover

	def get_attendence(self):
		return self.attendence
"""
average_turnover_and_attendence_in_window("svensk_bio.xlsx", "02-20", plus_minus_days=7)

