from django.db import models
from datetime import datetime

class Article(models.Model):
    class Meta:
        db_table = 'article'

    article_id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=500, null=False, verbose_name='제목')
    content = models.CharField(max_length=30000, null=False, verbose_name='본문')
    written_at = models.DateField(null=False, verbose_name='작성일')
    url = models.CharField(max_length=2000, null=False, verbose_name='주소')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='생성일시')

    def __str__(self):
        return self.created_at.strftime('%Y-%m-%d')

class Word(models.Model):
    class Meta:
        db_table = 'words'

    word_id = models.AutoField(primary_key=True)
    article_id = models.ForeignKey(Article, null=False, on_delete=models.CASCADE, verbose_name='기사')
    text = models.CharField(max_length=100, verbose_name='단어')
    frequecny = models.IntegerField(default=1, verbose_name='빈도')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='생성일시')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='수정일시')
