# Generated by Django 3.0.6 on 2020-05-30 07:24

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('path', models.ImageField(upload_to='images/')),
                ('title', models.CharField(max_length=60, null=True)),
                ('caption', models.CharField(max_length=140)),
                ('likes', models.IntegerField(default=0, null=True)),
                ('comments', models.TextField()),
            ],
        ),
    ]
