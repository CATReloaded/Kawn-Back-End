# Generated by Django 3.1.1 on 2020-10-08 15:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0004_auto_20201008_1543'),
    ]

    operations = [
        migrations.AlterField(
            model_name='member',
            name='image',
            field=models.ImageField(default='1.jpg', upload_to='media/profile_pics'),
        ),
    ]