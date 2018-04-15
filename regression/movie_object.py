from xlrd import open_workbook
import xlwt

"""
Each movie represent one object of the class Movie. The goal with our program is to predict the revenue of each Movie
by comparing the other attributes.
"""
class Movie:
    def __init__(self, title, revenue, imdb_rating, wiki_sv, wiki_eng, production_budget, sf_rating, mpaa_rating):
        self.title=title
        self.revenue=revenue
        self.imdb_rating=imdb_rating
        self.wiki_sv=wiki_sv
        self.wiki_eng=wiki_eng
        self.production_budget=production_budget
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

def main():
    data_file=open_workbook('master.xlsx')
    movie_list=create_objects(data_file)
    pass

if __name__ == '__main__':
    main()
