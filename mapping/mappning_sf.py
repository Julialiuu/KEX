from xlrd import open_workbook
import xlwt

class Filminstitutet:
	def __init__(self, titel, betyg):
		self.titel = titel
		self.betyg = betyg


def NameToSf():
	sf_fil = open_workbook("mappning.xlsx")
	namn_fil = open_workbook("namn.xlsx")
	workbook = xlwt.Workbook(encoding='utf-8')
	worksheet=workbook.add_sheet("My worksheet")
	sheet2=workbook.add_sheet("SF_data")

	namnlista = []
	for r in namn_fil.sheets():
		for row in range(0, r.nrows):
			#rowvals = sheet_namn.row_values
			namnlista.append(r.cell(row,0).value)

	sf_lista = []
	for r in sf_fil.sheets():
		for row in range(0, r.nrows):
			#rowval = sheet_sf.row_values
			sf_lista.append(Filminstitutet(r.cell(row,0).value ,r.cell(row,1).value))
	print(len(sf_lista))
	correctList = []
	iter=0
	index=0
	for element in namnlista:
		for obj in sf_lista:
			if element==obj.titel:
				correctList.append(element+" ; "+str(obj.betyg))
				worksheet.write(index,0,element)
				worksheet.write(index,1,obj.betyg)
				sf_lista.remove(obj)
				break
			else:
				iter +=1
		if iter == len(sf_lista):
			correctList.append(element)
			print(element)
			worksheet.write(index,0,element)
		iter = 0
		index = index+1
	workbook.save('Excel_Workbook.xls')

	index2=0
	for obj in sf_lista:
		sheet2.write(index2,0,obj.titel)
		sheet2.write(index2,1,obj.betyg)
		index2=index2+1
	workbook.save('Excel_Workbook.xls')
	#print(correctList)
	#print(sf_lista)
	#for element in sf_lista:
	#	print(element.titel)

NameToSf()