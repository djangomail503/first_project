# Generated by Django 3.2.14 on 2022-07-14 07:08

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='UserProfileModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=25)),
                ('email', models.EmailField(max_length=254)),
                ('pic', models.ImageField(upload_to='profile_pics')),
                ('pdf', models.FileField(upload_to='resume')),
                ('p_link', models.URLField()),
            ],
        ),
    ]
