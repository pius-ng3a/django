# Generated by Django 2.2.2 on 2019-06-13 11:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('movie', '0003_auto_20190612_1533'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movie',
            name='manager',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='movie.Manager'),
        ),
    ]
