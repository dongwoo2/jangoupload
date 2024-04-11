from django.db import models

# Create your models here.

class UploadFile(models.Model):
    title = models.CharField(
                default="제목 없음",
                max_length=50
    )
    file = models.FileField(
        # upload_to="", # MEDIA_ROOT 하위 경로(계정, 날짜 등으로 폴더 구조를 관리할 때 사용)
        null=True)
    
    def __str__(self):
        return f"제목={self.title} 파일명:{self.file}" 