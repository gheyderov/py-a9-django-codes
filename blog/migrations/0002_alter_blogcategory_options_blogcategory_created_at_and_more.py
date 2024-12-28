# Generated by Django 5.1.4 on 2024-12-28 11:52

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='blogcategory',
            options={'verbose_name_plural': 'Blog Categories'},
        ),
        migrations.AddField(
            model_name='blogcategory',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='blogcategory',
            name='updated_at',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
