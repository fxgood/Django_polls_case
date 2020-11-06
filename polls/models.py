from django.db import models

# Create your models here.

class Question(models.Model):
    # Question表的第一列属性：问题文本
    question_text=models.CharField(max_length=200)
    # Question表的第二列属性：问题发布时间
    pub_date=models.DateTimeField('发布时间')
    # 将每一项的简介信息，改为自身的问题文本
    def __str__(self):
        return self.question_text

class Choice(models.Model):
    question=models.ForeignKey(Question,on_delete=models.CASCADE)
    choice_text=models.CharField(max_length=200)
    votes=models.IntegerField(default=0)

    def __str__(self):
        return self.choice_text