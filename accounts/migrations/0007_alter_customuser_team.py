# Generated by Django 3.2.5 on 2021-08-01 12:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0006_auto_20210801_1546'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='team',
            field=models.ForeignKey(default=1, null=True, on_delete=django.db.models.deletion.SET_NULL, to='accounts.team', verbose_name='Team'),
        ),
    ]
