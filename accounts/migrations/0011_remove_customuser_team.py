# Generated by Django 3.2.5 on 2021-08-01 13:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0010_customuser_team'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customuser',
            name='team',
        ),
    ]