# Generated by Django 3.0.6 on 2020-06-01 09:12

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0011_update_proxy_permissions'),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('profile_path', models.ImageField(default='profile_pics/default.jpg', upload_to='profile_pics/')),
                ('bio', models.TextField()),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
                ('followers', models.ManyToManyField(blank=True, related_name='followers_profile', to='user.Profile')),
                ('following', models.ManyToManyField(blank=True, related_name='following_profile', to='user.Profile')),
            ],
        ),
    ]
