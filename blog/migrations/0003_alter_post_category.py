# Generated by Django 3.2.15 on 2022-09-16 13:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_auto_20220916_0835'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='category',
            field=models.CharField(choices=[('Snacks', 'Snacks'), ('Meals', 'Meals'), ('Desserts', 'Desserts')], default=0, max_length=8),
        ),
    ]