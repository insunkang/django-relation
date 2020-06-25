# django relation 1:N
---
## CREATE

```python
# 1. 댓글 생성
comment = Comment()
comment.Content = '첫번째 댓글'
comment.save()

# 2. 게시글 하나 불러오기
article = Article.objects.get(pk=1)

# 2-1. comment와 article 연결하기
comment.article = article
comment.save()

# 또 다른 방법
# 작성하는 숫자는 article의 pk값
comment.article_id = 1
comment.save()
```

## READ

```python
# comment 변수를 불러오기
# 1. 댓글 pk 조회
comment.pk

# 2. 댓글 content 조회
comment.content

# 3. 댓글이 어느 게시글에 연결되어 있는.
comment.article_id

# 4. 댓글이 연결된 게시글
comment.article

# 4-1. 댓글이 연결된 게시글의 제목과 내용
comment.article.pk
comment.article.title
comment.article.content

# article의 경우는?
article.comment_set.all()
```

## 0625 M:N

```python
doctor = Doctor.objects.create(name='KIM') 
patient = Patient.objects.create(name='TOM') 
Reservation.objects.create(doctor=doctor,patient=patient)
<Reservation: 1의사 KIM의 1번 환자, TOM>

 doctor.reservation_set.all()
 <QuerySet [<Reservation: 1의사 KIM의 1번 환자, TOM>]>
```

```python
like_users = models.ManyToManyField(settings.AUTH_USER_MODEL,related_name='like_articles',
    blank=True)
    # article에 좋아여 기능
```