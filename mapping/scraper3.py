import requests
from bs4 import BeautifulSoup
from xlrd import open_workbook
import xlwt

class imdb:
	def __init__(self, title, rating):
		self.title = title
		self.rating=rating

#title = raw_input("Enter Movie name to search: ") 

def search_movie(title):
	s="+".join(title.split())


	f_url = 'http://www.imdb.com/find?q='
	url=f_url+s+'&s=all'
	try:
		var = requests.get(url)
		soup = BeautifulSoup(var.content)

		x = soup.find("td", {"class": "result_text"})
		m = x.find("a")['href']

	except Exception:
		print "Check Your Movie Name"
		exit()
		
	new_url = 'http://www.imdb.com' + m 

	content = requests.get(new_url)
	soup = BeautifulSoup(content.content)


	x = soup.find("div", {"class": "title_wrapper"})
	print "-------------------------------------------------------------------"
	c = x.findChildren()[0]
	print "Movie Name: %s" % c.text
	title_name=c.text

	c = soup.find("div", {"class":"ratingValue"})
	print "IMDb: %s" % c.text 

	"""

	print "--------------------------------------------------------------------"
	print "Director: "
	for tag in soup.find_all("span", {"itemprop":"director"}):
		print "%s" % tag.text

	print "--------------------------------------------------------------------"
	print "Writers: "
	for tag in soup.find_all("span", {"itemprop":"creator"}):
		print "%s" % tag.text


	print "--------------------------------------------------------------------"
	print "Actors: "
	for tag in soup.find_all("span", {"itemprop":"actors"}):
		print "%s" % tag.text

	"""
	print "--------------------------------------------------------------------"
	return (c.text, title_name)

def main():
	namn_fil = open_workbook("namn.xlsx")
	workbook = xlwt.Workbook()
	sheet1=workbook.add_sheet("imdb")
	index=0
	for r in namn_fil.sheets():
		for row in range(0, r.nrows):
			try:
				imdb_value=search_movie(r.cell(row,0).value)
				sheet1.write(index,0,r.cell(row,0).value)
				sheet1.write(index,1, imdb_value[0])
				sheet1.write(index,2,imdb_value[1])
			except:
				sheet1.write(index,0,r.cell(row,0).value)
				sheet1.write(index,1, "N/A")
			index=index+1
	workbook.save("IMDB_answer")
main()
