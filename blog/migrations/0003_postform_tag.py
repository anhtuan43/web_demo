# Generated by Django 4.2.8 on 2024-02-20 06:23

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("blog", "0002_postform_body_alter_postform_title"),
    ]

    operations = [
        migrations.AddField(
            model_name="postform",
            name="tag",
            field=models.CharField(default="general", max_length=100),
        ),
    ]
