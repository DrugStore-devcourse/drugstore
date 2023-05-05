# Generated by Django 4.2 on 2023-05-03 16:34

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Drug',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('drug_no', models.CharField(default='', max_length=3000, verbose_name='약물번호')),
                ('drfstf', models.CharField(default='', max_length=3000, verbose_name='한글명')),
                ('drfstf_eng', models.CharField(default='', max_length=3000, verbose_name='영문명')),
                ('type_code', models.CharField(default='', max_length=3000, verbose_name='분류/구분')),
                ('pharm', models.CharField(default='', max_length=3000, null=True, verbose_name='이화학정보')),
                ('side_effect', models.CharField(default='', max_length=3000, null=True, verbose_name='남용정보')),
                ('medication', models.CharField(default='', max_length=3000, null=True, verbose_name='약물정보')),
                ('del_field', models.BooleanField(default=False, verbose_name='삭제여부')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='생성일시')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='수정일시')),
            ],
            options={
                'db_table': 'drugs',
            },
        ),
    ]
