# PJT10 - Django 종합 프로젝트

## 1. 프로젝트 개요

- 지금까지 배운 Django를 활용하여, 영화 좋아요 및 팔로우 페이지를 제작.
- ERD 모델링 구현하기
- 협업을 통한 데이터베이스 모델링 및 기능 구현



## 2. 코딩 과정

- Github의 브랜치를 통해서 협업하였습니다.
-  https://github.com/SBJ-practice/practice 

---

- ![image](https://user-images.githubusercontent.com/52685322/69312555-a7d85880-0c72-11ea-9cba-5bb75270be8b.png)

- movies/models.py

  ```python
  from django.db import models
  from django.conf import settings
  
  # Create your models here.
  class Genre(models.Model):
      name = models.CharField(max_length=20)
  
      def __str__(self):
          return self.name
      
  
  class Movie(models.Model):
      title = models.CharField(max_length=30)
      audience = models.IntegerField()
      poster_url = models.CharField(max_length=140)
      description = models.TextField()
      genre = models.ManyToManyField(Genre, related_name='movie_genre', blank=True)
      like_users = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='like_movies', blank=True)
  
      class Meta:
          ordering = ('-pk',)
  
      def __str__(self):
          return self.title
  
      # def movie_genres(self):
      #     return 
      
  
  class Review(models.Model):
      content = models.CharField(max_length=140)
      score = models.IntegerField()
      user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
      movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
  
      class Meta:
          ordering = ('-pk',)
  
  ```

  - genre와 movie는 M:N 관계
  - moive와 like_user는 M:N 관계
  - movie와 review는 1:N 관계

- accounts/models.py

  ```python
  from django.db import models
  from django.contrib.auth.models import AbstractUser
  from django.conf import settings
  
  # Create your models here.
  class User(AbstractUser):
      followers = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='followings', blank=True)
  
  ```
  - user와 follower은 M:N관계





## 3. 어려웠던 점

1. M:N 관계 및 1:N 관계인지 구별하기

   ERD를 구성할 때, 각 영역의 관계가 다수인지 1개인지 구별하여서, 어떻게 연결할 것인지를 정하는 것이 중요하였다.

2. Github 협업하기

   fork와 pull 방법으로 하나의 프로젝트를 여러명이서 협업시 필요한 배경지식에 대해서 학습하고, 이용하였다.

3. movies /  accounts 를 나누어서 서로 협업하였을 때에 

   같은 파일을 수정하였을 때에, conflict(충돌)시 어떤 것이 옳은 지 판단하고, 코드를 수정할 때에 충분한 의사소통이 필요하였다.

4. follow 기능을 각자의 유저정보인 profile에 넣을시에 `NoReverseMatch`오류가 발생하였다. 

   url 주소에 해당되는 `username`을 받아와서 접속되어 있는 user와 비교하여서 해결하였다.

   

## 4. 느낀점

 1. 협업 프로젝트의 어려움

    Github으로 협업을 한다는 점의 어려움을 많이 느꼈고, Github을 활용하는 방법을 학습하였습니다.

    또한, 분업 시 코드 충돌날 때에 수정해야될 항목을 검사하고, 맞는 코드를 찾아 넣는 방법을 선택하였습니다.

2. 협업 프로젝트의 장점

   오류가 나거나 논리적으로 코드가 모순 되었을 때에 서로의 코드를 확인하면서, 보다 빠르고 쉽게 문제들을 해결하였습니다.

   많은 양의 코드를 분업을 할 수 있다는 것에 시간을 단축할 수 있었습니다.

   