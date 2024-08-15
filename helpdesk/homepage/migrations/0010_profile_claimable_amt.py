# Generated by Django 5.1 on 2024-08-15 02:38

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("homepage", "0009_profile_unique_id"),
    ]

    operations = [
        migrations.AddField(
            model_name="profile",
            name="claimable_amt",
            field=models.DecimalField(decimal_places=2, default=0, max_digits=15),
            preserve_default=False,
        ),
    ]
