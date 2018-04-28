import re
import xlwt
file_actor = open("actor.txt","r")
file_actress=open("actress.txt","r")
file_writer=open("writer.txt","r")
file_director=open("director.txt","r")

class Actor:
    def __init__(self, name,starmeter):
        self.name=name
        self.starmeter=starmeter

starlist=[]
def write_to_list(file, starlist):
    data= file.readline()
    data=data.split("\"")
    print(len(data))
    for element in data:
        list_element = re.split('\( | Actor |Producer | Director | Writer | Actress', element)
        actor_name=list_element[0].split('(')
        name=actor_name[0]
        value_list=element.split(" ")
        if len(value_list) > 2:
            number=len(value_list)-5
            rating=value_list[number]
            starlist.append(Actor(name, rating))
    return starlist

starlist=write_to_list(file_actor,starlist)
starlist=write_to_list(file_actress,starlist)
starlist=write_to_list(file_director,starlist)
starlist=write_to_list(file_writer,starlist)


F = open("workfile.txt","w")
workbook = xlwt.Workbook(encoding = 'utf-8')
sheet1=workbook.add_sheet('actors')
index=0
for element in starlist:
    sheet1.write(index,0,element.name)
    sheet1.write(index,1,element.starmeter)
    index +=1
    F.write(element.name+';'+element.starmeter)

workbook.save('actors.xlt')
