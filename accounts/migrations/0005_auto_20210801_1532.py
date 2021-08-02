# Generated by Django 3.2.5 on 2021-08-01 12:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0004_auto_20210728_1023'),
    ]

    operations = [
        migrations.CreateModel(
            name='Submission',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=300)),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True)),
                ('update_at', models.DateTimeField(auto_now=True, null=True)),
            ],
        ),
        migrations.AlterField(
            model_name='customuser',
            name='role',
            field=models.ForeignKey(default=4, null=True, on_delete=django.db.models.deletion.SET_NULL, to='accounts.role', verbose_name='Role'),
        ),
    ]