# Generated by Django 5.0.7 on 2024-08-05 05:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("homepage", "0005_remove_profile_email_remove_profile_password"),
    ]

    operations = [
        migrations.AddField(
            model_name="profile",
            name="insurer",
            field=models.CharField(default="hdfc", max_length=255),
            preserve_default=False,
        ),
    ]
