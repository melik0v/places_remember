# Generated by Django 4.0.4 on 2022-06-04 17:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("memories", "0001_initial"),
    ]

    operations = [
        migrations.RenameField(
            model_name="memoryimage",
            old_name="product",
            new_name="memory",
        ),
        migrations.AddField(
            model_name="memory",
            name="description",
            field=models.TextField(blank=True, default=None, null=True),
        ),
        migrations.AddField(
            model_name="memory",
            name="place",
            field=models.CharField(blank=True, default=None, max_length=255, null=True),
        ),
    ]
