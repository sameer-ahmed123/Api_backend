# Generated by Django 4.2 on 2024-01-29 17:16

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Employees',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=1000)),
                ('designation', models.CharField(max_length=1500)),
                ('salary', models.IntegerField()),
            ],
        ),
    ]
