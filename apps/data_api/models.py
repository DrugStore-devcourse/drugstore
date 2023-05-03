from django.db import models


class Drug(models.Model):
    id = models.AutoField(
        primary_key=True,
    )  # pk
    drug_no = models.CharField(
        max_length=3000, default="", null=False, verbose_name="약물번호"
    )
    drfstf = models.CharField(
        max_length=3000, default="", null=False, verbose_name="한글명"
    )
    drfstf_eng = models.CharField(
        max_length=3000, default="", null=False, verbose_name="영문명"
    )
    type_code = models.CharField(
        max_length=3000, default="", null=False, verbose_name="분류/구분"
    )
    pharm = models.CharField(
        max_length=3000, default="", null=True, verbose_name="이화학정보"
    )
    side_effect = models.CharField(
        max_length=3000, default="", null=True, verbose_name="남용정보"
    )
    medication = models.CharField(
        max_length=3000, default="", null=True, verbose_name="약물정보"
    )

    del_field = models.BooleanField(default=False, verbose_name="삭제여부")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="생성일시")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="수정일시")

    class Meta:
        db_table = "drugs"
