# Generated by Django 4.2 on 2024-01-30 09:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Api', '0003_remove_employees_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='employees',
            name='image',
            field=models.ImageField(default=112, upload_to='Employee_images/'),
            preserve_default=False,
        ),
    ]