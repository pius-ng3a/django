# Generated by Django 2.2.2 on 2019-06-12 14:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movie', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Manager',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('experience', models.FloatField(blank=True, null=True)),
            ],
        ),
        migrations.DeleteModel(
            name='Person',
        ),
    ]
