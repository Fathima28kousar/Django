# Generated by Django 4.2.6 on 2023-10-18 09:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('A', '0002_employee'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='ename',
            field=models.TextField(max_length=100),
        ),
    ]
