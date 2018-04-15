from xlrd import open_workbook
import xlwt
import csv
import pandas as pd

"""
Each movie represent one object of the class Movie. The goal with our program is to predict the revenue of each Movie
by comparing the other attributes.
"""
class Movie:
    def __init__(self, title, revenue, imdb_rating, wiki_sv, wiki_eng, production_budget, sf_rating, mpaa_rating):
        self.title=title
        self.revenue=revenue
        if imdb_rating=='N/A':
            imdb_rating=0
        self.imdb_rating=imdb_rating
        if wiki_sv=='N/A':
            wiki_sv=0
        self.wiki_sv=wiki_sv
        if wiki_eng=='N/A':
            wiki_eng=0
        self.wiki_eng=wiki_eng
        if production_budget=='N/A':
            production_budget=0
        self.production_budget=production_budget
        if sf_rating=='N/A':
            sf_rating=0
        self.sf_rating=sf_rating
        self.mpaa_rating=mpaa_rating

def create_objects(file_name):
    index=0
    movie_list=[]
    for r in file_name.sheets():
        for row in range(1,r.nrows):
            movie_object=Movie(r.cell(row,0).value,r.cell(row,1).value,r.cell(row,7).value,r.cell(row,10).value,r.cell(row,11).value,r.cell(row,5).value,r.cell(row,6).value,r.cell(row,4).value)
            movie_list.append(movie_object)
            print(movie_object.title, movie_object.revenue, movie_object.imdb_rating, movie_object.wiki_sv,movie_object.wiki_eng,movie_object.production_budget,movie_object.sf_rating,movie_object.mpaa_rating)
    return movie_list

def print_csv(movie_list):
    res =[['revenue','imdb_rating','wiki_sv','wiki_en','production_budget','sf_rating','mpaa_rating']]
    for element in movie_list:
        if element.wiki_eng != 0:
            res.append([element.revenue,element.imdb_rating,element.wiki_sv,element.wiki_eng,element.production_budget,element.sf_rating,element.mpaa_rating])
    my_df=pd.DataFrame(res)
    my_df.to_csv('wiki_en.csv',index=False,header=False)
    print(my_df)
    """
    with open('movies.csv', 'wb') as csvfile:
        wr=csv.writer(csvfile,quoting=csv.QUOTE_ALL)
        data=[]
        for element in movie_list:
            data.append(str(element.revenue)+','+str(element.imdb_rating)+','+str(element.wiki_sv)+','+str(element.wiki_eng)+','+str(element.production_budget)+','+str(element.sf_rating))
        wr.writerow(data)
    """

def cross_vali():
    df=pd.read_csv("out_headers.csv")

    y=df['revenue']
    x=df['imdb_rating']

    x=x.reshape(len(x),1)
    y=y.reshape(len(y),1)



def main():
    data_file=open_workbook('master.xlsx')
    movie_list=create_objects(data_file)
    print_csv(movie_list)
    #return movie_list

if __name__ == '__main__':
    main()
