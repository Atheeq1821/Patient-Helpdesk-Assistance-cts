# Generated by Django 5.1 on 2024-08-15 02:40

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("homepage", "0010_profile_claimable_amt"),
    ]

    operations = [
        migrations.AddField(
            model_name="profile",
            name="claims",
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
    ]
