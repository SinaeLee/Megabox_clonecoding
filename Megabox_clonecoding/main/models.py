from django.db import models

# Create your models here.
# 영화 정보를 저장한 테이블 생성
# class Movie(models.Model) :
#     movie_type = models.CharField(max_length=50) #영화의 타입
#     movie_title = models.CharField(max_length=100) # 영화 제목
#     movie_title_eng = models.CharField(max_length=100)  # 영화 영어 제목
#     movie_like = models.CharField(max_length=100)  # 좋아요 수
#     movie_score = models.CharField(max_length=100)  # 평점
#     movie_rank = models.CharField(max_length=100)  # 영화 순위
#     movie_rate = models.CharField(max_length=100)  # 예매율
#     movie_audience = models.CharField(max_length=100)  # 관람자 수
#     movie_age = models.CharField(max_length=100)  # 나이제한(12 15 19 전체관람가 등)
#     movie_summary = models.TextField(max_length=1000) # 영화 요약
#     movie_type2 = models.CharField(max_length=50)  # 2D, 3D
#     movie_line1 = models.CharField(max_length=100)  # 감독
#     movie_line2 = models.CharField(max_length=100)  # 영화 장르
#     movie_line3 = models.CharField(max_length=100)  # 영화 상영 시간(분)
#     movie_line4 = models.CharField(max_length=100)  # 나이제한(12 15 19 전체관람가 등)
#     movie_line5 = models.CharField(max_length=100)  # 개봉일
#     movie_actor = models.CharField(max_length=500)  # 출연진

class test(models.Model) :
    movie_type = models.CharField(max_length=50) #영화의 타입
    movie_title = models.CharField(max_length=100) # 영화 제목
    movie_title_eng = models.CharField(max_length=100)  # 영화 영어 제목
    movie_like = models.CharField(max_length=100)  # 좋아요 수
    movie_score = models.CharField(max_length=100)  # 평점
    movie_rank = models.CharField(max_length=100)  # 영화 순위
    movie_rate = models.CharField(max_length=100)  # 예매율
    movie_audience = models.CharField(max_length=100)  # 관람자 수
    movie_age = models.CharField(max_length=100)  # 나이제한(12 15 19 전체관람가 등)
    movie_summary = models.TextField(max_length=1000) # 영화 요약
    movie_type2 = models.CharField(max_length=50)  # 2D, 3D
    movie_line1 = models.CharField(max_length=100)  # 감독
    movie_line2 = models.CharField(max_length=100)  # 영화 장르
    movie_line3 = models.CharField(max_length=100)  # 영화 상영 시간(분)
    movie_line4 = models.CharField(max_length=100)  # 나이제한(12 15 19 전체관람가 등)
    movie_line5 = models.CharField(max_length=100)  # 개봉일
    movie_actor = models.CharField(max_length=500)  # 출연진