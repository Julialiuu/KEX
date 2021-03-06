#!/usr/bin/env python
# -*- coding: utf-8 -*- 
# 180227
# author: Linnea Lindahl and Julia Liu
from xlrd import open_workbook

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
	file_object=open_workbook(file_name)
	for r in file_object.sheets():
		for row in range(1, r.nrows):
			movie=Movie(r.cell(row,1).value, r.cell(row,5).value, r.cell(row,3).value, r.cell(row,3).value)
			movie_list.append(movie)
	return movie_list

def date_to_check(date, plus_minus_days, movie_list):
	date_list=[]
	month=date[0:2]
	day=date[3:5]
	month_length=month_length(month) #returns length of month
	
	"""
	Calculates the intervall from the given parameters.
	returns a list of date to check
	"""
	return date_list
	
def month_length(month): 
	if month%2 == 0:
		return 30
	elif month%2 == 1:
		return 31
	else: 
		return 28


class Movie:

	def __init__(self, title, movie_date, turnover, attendence):
		self.title=title
		self.movie_date=movie_date #gives the date in form YYYY-MM-DD
		self.turnover=int(turnover)
		self.attendence=int(attendence)
		self.date_month = date[5:7] #returns the date in form MM
		self.date_day = date[8:10] #returns the date in form DD


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

