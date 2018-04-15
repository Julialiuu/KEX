# -*- coding: utf-8 -*-
from xlrd import open_workbook
import xlwt
from datetime import *
import datetime as dt
import pageviewapi
import sys
reload(sys)
sys.setdefaultencoding('UTF8')

class Filminstitutet:
	def __init__(self, titel1, titel2, titel3, firstdate, lastdate=None):
		self.titel1 = titel1
		self.titel2 = titel2
		self.titel3 = titel3
		#print(titel3)
		self.firstdate = firstdate
		self.lastdate = datefunc(firstdate)


def datefunc(firstdate):
	if firstdate == '/N///A':
		return None
	firstdate = str(firstdate)
	year = firstdate[2:4]
	month = firstdate[4:6]
	day = firstdate[6:8]
	plus_days = 30
	#print(firstdate)
	#print(year,month,day)
	date = dt.datetime(int(year),int(month),int(day))
	date2=date-dt.timedelta(days=plus_days)
	year = '20'+str(date2.year)
	if len(str(date2.month)) == 1:
		month='0'+str(date2.month)
	else:
		month=str(date2.month)
	if len(str(date2.day))==1:
		day='0'+str(date2.day)
	else:
		day=str(date2.day)
	return_day=year+month+day
	return return_day


def movie_to_object(namn_fil):
	index = 0
	movie_object_list=[]
	for r in namn_fil.sheets():
		for row in range(1,r.nrows):
			movie=Filminstitutet(r.cell(row,0).value,r.cell(row,8).value,r.cell(row,9).value, r.cell(row,2).value)
			movie_object_list.append(movie)
	return movie_object_list

def wiki_scraper(workbook, sheet1, object_list):
	iteration=0
	for element in object_list:
		try: 
			#print('1')
			#print(element.titel1)
			#print(element.lastdate)
			#print(element.firstdate)
                        titel1=element.titel1
                        titel2=element.titel2
                        titel3=element.titel3
			print(titel2,titel3)
			"""
			views = pageviewapi.per_article('sv.wikipedia', element.title1, element.firstdate, element.lastdate,
                        	access='all-access', agent='all-agents', granularity='daily')
			"""
			views=pageviewapi.per_article('en.wikipedia', element.titel1, element.lastdate, element.firstdate,
                        access='all-access', agent='all-agents', granularity='daily')
			views = select_views(views)
			#print(1, views)
		except:
			try:
                                print(2)
                                print(titel2)
				views = pageviewapi.per_article('en.wikipedia', element.titel2, element.lastdate, element.firstdate,
                        	access='all-access', agent='all-agents', granularity='daily')
				views = select_views(views)
			except:
				try:
                                        print(3)
                                        print(element.titel3)
                                        views = pageviewapi.per_article('en.wikipedia', element.titel3, element.lastdate, element.firstdate,
                                        access='all-access', agent='all-agents', granularity='daily')
                                        views = select_views(views)
                                except:
                                        views = 'N/A'
		write_to_file(sheet1, views, iteration, element)
		iteration=iteration+1
	workbook.save('Wiki_workbook.xls')
	print 'hola!'

def select_views(views):
	tot_views=0
	for i in range(0,30):
		try:
			tot_views = views.items()[0][1][i]['views'] 
		except:
			pass
	return tot_views


def write_to_file(sheet1, views, iteration, element):
	sheet1.write(iteration,0, element.titel1)
	sheet1.write(iteration,1,element.titel2)
	sheet1.write(iteration,2,element.firstdate)
	sheet1.write(iteration,3,views)
	return None


def main():
	namn_fil=open_workbook('master.xlsx', encoding_override="cp1252")
	object_list=movie_to_object(namn_fil)
	wikiworkbook = xlwt.Workbook(encoding='UTF-8')
	sheet1=wikiworkbook.add_sheet('wiki')
	wiki_scraper(wikiworkbook,sheet1, object_list)

main()
