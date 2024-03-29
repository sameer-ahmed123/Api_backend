# Generated by Django 4.2 on 2024-02-26 07:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Status',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('State', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Task_title', models.CharField(max_length=250)),
                ('Slug', models.SlugField(max_length=250)),
                ('Content', models.TextField(max_length=1000)),
                ('status', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='App.status')),
            ],
        ),
    ]
