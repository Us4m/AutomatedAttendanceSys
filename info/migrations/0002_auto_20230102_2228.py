# Generated by Django 3.0.14 on 2023-01-02 17:28

from django.db import migrations, models
import info.models


class Migration(migrations.Migration):

    dependencies = [
        ('info', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to=info.models.filepath),
        ),
        migrations.AlterField(
            model_name='teacher',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to=info.models.filepath),
        ),
    ]
