# Generated by Django 2.2.12 on 2020-09-02 15:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("core", "0004_auto_20200826_1907"),
    ]

    operations = [
        migrations.RenameField(
            model_name="objecttype",
            old_name="contact",
            new_name="maintainer_contact_email",
        ),
        migrations.RenameField(
            model_name="objecttype",
            old_name="maintainer",
            new_name="maintainer_organization",
        ),
        migrations.RenameField(
            model_name="objecttype", old_name="public", new_name="public_data"
        ),
    ]
