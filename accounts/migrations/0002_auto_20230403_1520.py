# Generated by Django 3.2.9 on 2023-04-03 12:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='birthday',
            field=models.DateField(null=True, verbose_name="Tug'ilgan sana"),
        ),
        migrations.AlterField(
            model_name='user',
            name='phone',
            field=models.CharField(max_length=13, null=True, verbose_name='Telefon raqam'),
        ),
    ]
