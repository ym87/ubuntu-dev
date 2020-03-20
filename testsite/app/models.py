from django.db import models
from django.contrib.postgres.fields import ArrayField
from django.utils import timezone

#プロジェクトテーブル
class project(models.Model):
    project_id = models.AutoField(primary_key=True)
    project_name = models.CharField(max_length=100)
    created_date = models.DateTimeField(default=timezone.now)

#プロジェクトテーブル
class column_name(models.Model):
    project_id = models.ForeignKey(project, on_delete=models.CASCADE)
    column_name = ArrayField(
            models.CharField(max_length=50),size=10)

#単語リスト            
class tokenizer(models.Model):
    project_id = models.ForeignKey(project, on_delete=models.CASCADE)

class train_status(models.Model):
    project_id = models.ForeignKey(project, on_delete=models.CASCADE)

class training_data(models.Model):
    project_id = models.ForeignKey(project, on_delete=models.CASCADE)

class test_result(models.Model):
    project_id = models.ForeignKey(project, on_delete=models.CASCADE)




class Post(models.Model):

    title = models.CharField('タイトル', max_length=50)

    def __str__(self):
        return self.title







