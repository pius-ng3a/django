# Generated by Django 2.2.2 on 2019-06-12 14:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('movie', '0002_auto_20190612_1518'),
    ]

    operations = [
        migrations.RenameField(
            model_name='manager',
            old_name='name',
            new_name='manager_name',
        ),
    ]