# Generated by Django 5.1 on 2024-08-15 02:55

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("homepage", "0011_profile_claims"),
    ]

    operations = [
        migrations.AddField(
            model_name="claim",
            name="applied_date",
            field=models.DateField(blank=True, null=True),
        ),
    ]
