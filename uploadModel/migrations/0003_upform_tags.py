# Generated by Django 4.2.8 on 2024-02-23 03:18

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("uploadModel", "0002_upform_title"),
    ]

    operations = [
        migrations.AddField(
            model_name="upform",
            name="tags",
            field=models.CharField(default="general", max_length=255),
        ),
    ]
