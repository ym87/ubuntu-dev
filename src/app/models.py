from django.db import models
from django.contrib.postgres.fields import ArrayField
from django.utils import timezone
from django.core.validators import MaxValueValidator, MinValueValidator
from django.contrib.postgres.fields import JSONField

#カラム数
number_of_columns = 10


#プロジェクトテーブル
class project(models.Model):
    project_id = models.AutoField(primary_key=True)
    project_name = models.CharField(max_length=100)
    created_date = models.DateTimeField(default=timezone.now)

#プロジェクトデータ
class project_data(models.Model):
    project = models.OneToOneField(project, on_delete=models.CASCADE,primary_key=True)
    column_data = JSONField()
        

#形態素解析の種類            
class tokenizer(models.Model):
    project = models.OneToOneField(project, on_delete=models.CASCADE)
    column_id = models.IntegerField(
        blank = True,
        null = True,
        validators = [MinValueValidator(0),
                    MaxValueValidator(number_of_columns)])
    tokenizer_choices = models.CharField(max_length=50)

#学習状況
class train_status(models.Model):
    project = models.OneToOneField(project, on_delete=models.CASCADE)


class training_data(models.Model):
    project = models.OneToOneField(project, on_delete=models.CASCADE)

class test_result(models.Model):
    project = models.OneToOneField(project, on_delete=models.CASCADE)



class Post(models.Model):

    title = models.CharField('タイトル', max_length=50)

    def __str__(self):
        return self.title







