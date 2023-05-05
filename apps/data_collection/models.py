from django.db import models
from django.db.models import UniqueConstraint

class Article(models.Model):
    article_id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=500, null=False, verbose_name='제목')
    content = models.CharField(max_length=30000, null=False, verbose_name='본문')
    written_at = models.DateField(null=False, verbose_name='작성일')
    url = models.CharField(max_length=2000, null=False, verbose_name='주소')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='생성일시')

    class Meta:
        db_table = 'article'

    def __str__(self):
        return self.created_at.strftime('%Y-%m-%d')

class Word(models.Model):      
    word_id = models.AutoField(primary_key=True)
    article_id = models.ForeignKey(Article, null=False, on_delete=models.CASCADE, verbose_name='기사')
    text = models.CharField(max_length=100, verbose_name='단어')
    frequency = models.IntegerField(default=1, verbose_name='빈도')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='생성일시')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='수정일시')

    class Meta:
        db_table = 'words'
        constraints = [
            UniqueConstraint(fields=['article_id', 'text'], name='unique_article_text')
        ]
