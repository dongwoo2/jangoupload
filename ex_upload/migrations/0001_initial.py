# Generated by Django 4.2 on 2024-04-11 08:06

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='UploadFile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(default='제목 없음', max_length=50)),
                ('file', models.FileField(null=True, upload_to='')),
            ],
        ),
    ]
