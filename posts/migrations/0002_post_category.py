# Generated by Django 4.2 on 2023-04-08 11:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("posts", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="post",
            name="category",
            field=models.CharField(default="uncategorized", max_length=200),
        ),
    ]