# Generated by Django 2.0.7 on 2019-10-27 16:50

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_time', models.DateTimeField(auto_now_add=True, help_text='创建时间')),
                ('last_modified', models.DateTimeField(auto_now=True, help_text='修改时间')),
                ('content', models.CharField(help_text='话题评论', max_length=255)),
                ('up', models.IntegerField(default=0, help_text='支持')),
                ('down', models.IntegerField(default=0, help_text='反对')),
            ],
            options={
                'ordering': ['-created_time'],
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Topic',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_time', models.DateTimeField(auto_now_add=True, help_text='创建时间')),
                ('last_modified', models.DateTimeField(auto_now=True, help_text='修改时间')),
                ('title', models.CharField(help_text='话题标题', max_length=255, unique=True)),
                ('content', models.TextField(help_text='话题内容')),
                ('is_online', models.BooleanField(default=True, help_text='话题是否在线')),
                ('user', models.ForeignKey(help_text='关联用户表', on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['-created_time'],
                'abstract': False,
            },
        ),
        migrations.AddField(
            model_name='comment',
            name='topic',
            field=models.ForeignKey(help_text='关联话题表', on_delete=django.db.models.deletion.CASCADE, to='post.Topic'),
        ),
    ]
