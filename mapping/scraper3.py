import requests
from bs4 import BeautifulSoup
from xlrd import open_workbook
import xlwt

class imdb:
	def __init__(self, title, rating, director1,director2,actor1,actor2,actor3,writer1,writer2,writer3):
		self.title = title
		self.rating=rating
		self.director1 = director1
		self.director2 = director2
		self.actor1=actor1
		self.actor2=actor2
		self.actor3=actor3
		self.writer1=writer1
		self.writer2=writer2
		self.writer3=writer3

#title = raw_input("Enter Movie name to search: ") 

def search_movie(title):
        title_name='N/A'
        director1='N/A'
        director2='N/A'
        actor1='N/A'
        actor2='N/A'
        actor3='N/A'
        writer1='N/A'
        writer2='N/A'
        writer3='N/A'
        
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

	

	print "--------------------------------------------------------------------"
	print "Director: "
	iter_D=0
	for tag in soup.find_all("span", {"itemprop":"director"}):
		print "%s" % tag.text
		print(tag.text)
		if iter_D ==0:
                        director1=tag.text
                        iter_D=1
                if iter_D ==1 and tag.text != director1:
                        director2=tag.text
                        iter_D=2

	print "--------------------------------------------------------------------"
	print "Writers: "
	iter_W = 0
	for tag in soup.find_all("span", {"itemprop":"creator"}):
		print "%s" % tag.text
		if iter_W ==0:
                        writer1=tag.text
                        iter_W=1
                if iter_W==1 and tag.text != writer1:
                        writer2=tag.text
                        iter_W=2
                if iter_W==2 and tag.text != writer1 and tag.text != writer2:
                        writer3=tag.text
                        iter_W=3


	print "--------------------------------------------------------------------"
	print "Actors: "
	iter_A=0
	for tag in soup.find_all("span", {"itemprop":"actors"}):
		print "%s" % tag.text
		if iter_A ==0:
                        actor1=tag.text
                        iter_A=1
                if iter_A==1 and tag.text != actor1:
                        actor2=tag.text
                        iter_A=2
                if iter_A==2 and tag.text != actor1 and tag.text != actor2:
                        actor3=tag.text
                        iter_A=3
	
	print "--------------------------------------------------------------------"
	return (c.text, title_name,director1,director2,actor1,actor2,actor3,writer1,writer2,writer3)

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
				sheet1.write(index,3,imdb_value[2])
				sheet1.write(index,4,imdb_value[3])
				sheet1.write(index,5,imdb_value[4])
				sheet1.write(index,6,imdb_value[5])
				sheet1.write(index,7,imdb_value[6])
				sheet1.write(index,8,imdb_value[7])
				sheet1.write(index,9,imdb_value[8])
				sheet1.write(index,10,imdb_value[9])
			except:
				sheet1.write(index,0,r.cell(row,0).value)
				sheet1.write(index,1, "N/A")
			index=index+1
	workbook.save("IMDB_answer")
main()
