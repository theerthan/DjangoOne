# Generated by Django 5.0.1 on 2024-02-15 00:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("DieManager", "0003_alter_batch_errorrate"),
    ]

    operations = [
        migrations.AlterField(
            model_name="batch",
            name="ErrorRate",
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=4),
        ),
    ]
