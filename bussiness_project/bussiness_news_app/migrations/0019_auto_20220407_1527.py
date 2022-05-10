# Generated by Django 3.2.12 on 2022-04-07 12:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bussiness_news_app', '0018_auto_20220407_1426'),
    ]

    operations = [
        migrations.CreateModel(
            name='AboutAuthor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('author', models.CharField(max_length=30)),
                ('description', models.TextField()),
                ('image', models.FileField(default=None, upload_to='author_image/')),
                ('fullname', models.CharField(default=None, max_length=40)),
            ],
            options={
                'verbose_name': 'image',
                'verbose_name_plural': 'images',
            },
        ),
        migrations.AlterField(
            model_name='posts',
            name='article_permission',
            field=models.CharField(choices=[('private', 'PRIVATE'), ('public', 'PUBLIC')], default='public', max_length=35),
        ),
        migrations.AlterField(
            model_name='user',
            name='status',
            field=models.CharField(choices=[('pedestrian', 'PEDESTRIAN'), ('editor', 'EDITOR')], default='pedestrian', max_length=10),
        ),
    ]