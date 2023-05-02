from django.db import models
from django.utils import timezone


# Create your models here.
class Drug(models.Model):
    id = models.IntegerField(primary_key=True, auto_created=True)

    DRUG_NO = models.CharField(max_length=3000, default="")  # 약물번호
    DRFSTF = models.CharField(max_length=3000, default="")  # 한글명
    DRFSTF_ENG = models.CharField(max_length=3000, default="")  # 영문명
    TYPE_CODE = models.CharField(max_length=3000, default="")  # 분류/구분
    PHARM = models.CharField(max_length=3000, default="")  # 이화학정보
    SIDE_EFFECT = models.CharField(max_length=3000, default="")  # 남용정보
    MEDICATION = models.CharField(max_length=3000, default="")  # 약물정보

    DEL_FIELD = models.BooleanField("")  # 삭제여부
    created_at = models.DateTimeField(timezone.now())  # 생성일시
    updated_at = models.DateTimeField(timezone.now())  # 수정일시


# class Choice(models.Model):
#     question = models.ForeignKey(Question, on_delete=models.CASCADE)
#     choice_text = models.CharField(max_length=200)
#     votes = models.IntegerField(default=0)
