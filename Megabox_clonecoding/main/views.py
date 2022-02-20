from django.shortcuts import render
from django.templatetags.static import static
# Create your views here.
def main_ind(request) :
    movie = Movie.objects.all()
    content = {'movie': movie}
    return render(request, 'main/index.html', content)

import csv
from .models import *

def info(request, movie_id) :
    # path = static('movie.csv')
    # file = open(path)

    # file = open('C:\PythonStudy\Megabox_clonecoding\Megabox_clonecoding\main\movie.csv')
    # reader = csv.reader(file)
    #
    # list = []
    # for row in reader:
    #     list.append(Movie(movie_type=row[0], movie_title=row[1], movie_title_eng=row[2],
    #                      movie_like=row[3], movie_score=row[4], movie_rank=row[5],
    #                      movie_rate=row[6], movie_audience=row[7], movie_age=row[8],
    #                       movie_summary=row[9], movie_type2=row[10], movie_line1=row[11],
    #                       movie_line2=row[12], movie_line3=row[13], movie_line4=row[14],
    #                       movie_line5=row[15], movie_actor=row[16]))
    # Movie.objects.bulk_create(list) # 이런식으로 리스트를 한번에 넣는다.
    movie = Movie.objects.get(id=movie_id)
    content = {'movie': movie}
    return render(request, 'main/info.html', content)