from xlrd import open_workbook
import xlwt

class Person:
	def __init__(self, name, betyg):
		self.name = name
		self.betyg = betyg
class Rating:
	def __init__(self,movie,director,writer,actor):
		self.movie=movie
		self.director=director
		self.writer=writer
		self.actor=actor

class  Imdb:
	def __init__(self, movie,director1,director2,writer1,writer2,writer3,actor1,actor2,actor3):
		self.movie=movie
		list=director1.split(",")
		director1=list[0].split('(')
		self.director1=director1[0].strip()
		list=director2.split(",")
		director2=list[0].split('(')
		self.director2=director2[0].strip()
		list=writer1.split(",")
		writer1=list[0].split('(')
		self.writer1=writer1[0].strip()
		list=writer2.split(",")
		writer2=list[0].split('(')
		self.writer2=writer2[0].strip()
		list=writer3.split(",")
		writer3=list[0].split('(')
		self.writer3=writer3[0].strip()
		list=actor1.split(",")
		actor1=list[0].split('(')
		self.actor1=actor1[0].strip()
		list=actor2.split(",")
		actor2=list[0].split('(')
		self.actor2=actor2[0].strip()
		list=actor3.split(",")
		actor3=list[0].split('(')
		self.actor3=actor3[0].strip()


def NameToSf():
	imdb_fil = open_workbook("imdb_persons.xlsx")
	people_fil = open_workbook("people.xlsx")
	workbook = xlwt.Workbook(encoding='utf-8')
	worksheet=workbook.add_sheet("My worksheet")
	sheet2=workbook.add_sheet("imdb_data")

	namnlista = []
	for r in people_fil.sheets():
		for row in range(0, r.nrows):
			#rowvals = sheet_namn.row_values
			namnlista.append(Person(r.cell(row,0).value.strip(),r.cell(row,1).value))

	imdb_lista = []
	for r in imdb_fil.sheets():
		for row in range(0, r.nrows):
			#rowval = sheet_sf.row_values
			imdb_lista.append(Imdb(r.cell(row,0).value.strip(),r.cell(row,1).value.strip() ,r.cell(row,2).value.strip(),r.cell(row,3).value.strip(),r.cell(row,4).value.strip(),r.cell(row,5).value.strip(),r.cell(row,6).value.strip(),r.cell(row,7).value.strip(),r.cell(row,8).value.strip()))

	
	rating_list=[]
	for movie in imdb_lista:
		d1=0; d2=0; w1=0; w2=0; w3=0; a1=0; a2=0; a3=0
		title=movie.movie
		for person in namnlista:
			if person.name==movie.director1:
				d1=int(person.betyg)
			if person.name==movie.director2:
				d2=int(person.betyg)
			if person.name==movie.writer1:
				w1=int(person.betyg)
			if person.name==movie.writer2:
				w2=int(person.betyg)
			if person.name==movie.writer3:
				w3=int(person.betyg)
			print(movie.actor1)
			if person.name==movie.actor1:
				
				a1=int(person.betyg)
			if person.name==movie.actor2:
				a2=int(person.betyg)
			if person.name==movie.actor3:
				a3=int(person.betyg)

		d_index=0
		director=0
		for element in [d1,d2]:
			if element != 0:
				d_index +=1
				director+=element
		if d_index !=0:
			director=director/d_index
		else:
			director = 'N/A'

		w_index=0
		writer=0
		for element in [w1,w2,w3]:
			if element != 0:
				w_index +=1
				print(writer,element)
				writer+=element
		if w_index !=0:
			writer=writer/w_index
		else:
			writer = 'N/A'

		a_index=0
		actor=0
		for element in [a1,a2,a3]:
			if element != 0:
				a_index +=1
				actor+=element
		if a_index !=0:
			actor=actor/a_index
		else:
			actor = 'N/A'




		rating_list.append(Rating(title,director,writer,actor))


	index2=0
	for obj in rating_list:
		sheet2.write(index2,0,obj.movie)
		sheet2.write(index2,1,obj.director)
		sheet2.write(index2,2,obj.writer)
		sheet2.write(index2,3,obj.actor)
		index2=index2+1
	workbook.save('persons_Workbook.xls')
	#print(correctList)
	#print(sf_lista)
	#for element in sf_lista:
	#	print(element.titel)

NameToSf()