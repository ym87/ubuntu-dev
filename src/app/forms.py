import csv
import io
from django import forms
from django.core.validators import FileExtensionValidator
from .models import Post

from .models import project
from .models import project_data

import os #拡張子分割用


class CSVUploadForm(forms.Form):
    file = forms.FileField(
        label='CSVファイル',
        help_text='※拡張子csvのファイルをアップロードしてください。',
        validators=[FileExtensionValidator(allowed_extensions=['csv'])]
    )

    def clean_file(self):
        file = self.cleaned_data['file']

        # csv.readerに渡すため、TextIOWrapperでテキストモードなファイルに変換
        csv_file = io.TextIOWrapper(file, encoding='utf-8')
        reader = csv.reader(csv_file)

        # 各行から作った保存前のモデルインスタンスを保管するリスト
        self._instances = []
        try:
            for i,row in enumerate(reader):
                #プロジェクト名、カラム名　保存処理
                if i == 0:
                    self.project_instances = project(project_name = os.path.splitext(csv_file.name)[0])
                    self.column_name = row                   
                else:
                    post = Post(pk=i, title=row[1])
                    self._instances.append(post)
        except UnicodeDecodeError:
            raise forms.ValidationError('ファイルのエンコーディングや、正しいCSVファイルか確認ください。')

        return file

    def save(self):
        project_save = self.project_instances.save()
        var_project_id = self.project_instances.project_id
        
        #プロジェクトデータ保存
        self.project_data_instances = project_data(project_id = var_project_id,
                            column_name = self.column_name,data_type = [],column_data = b"")
        self.project_data_instances.save()

        Post.objects.bulk_create(self._instances, ignore_conflicts=True)
        Post.objects.bulk_update(self._instances, fields=['title'])
