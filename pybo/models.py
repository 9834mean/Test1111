from django.db import models

#질문 모델 클래스를 정의
class Question(models.Model):
    subject = models.CharField(max_length=200) # 글자 수 제한이 있는 데이터
    content = models.TextField()    # 글자 수 제한이 없는 데이터
    create_date = models.DateTimeField()    # 날짜, 시간을 나타내는 데이터

    def __str__(self):
        return self.subject #제목반환
    
# 답변 모델 클래스를 정의
class Answer(models.Model):
    # 답변 모델이 가지는 속성을 정의
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    content = models.TextField()
    create_date = models.DateTimeField()
