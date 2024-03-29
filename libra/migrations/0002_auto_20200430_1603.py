# Generated by Django 3.0.5 on 2020-04-30 13:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('libra', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='author',
            field=models.CharField(default='', max_length=50),
        ),
        migrations.AddField(
            model_name='book',
            name='cover',
            field=models.ImageField(default=None, upload_to=''),
        ),
        migrations.AddField(
            model_name='book',
            name='release_date',
            field=models.DateField(auto_now=True),
        ),
    ]
