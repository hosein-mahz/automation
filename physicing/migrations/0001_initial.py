# Generated by Django 2.2 on 2019-12-13 11:06

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='physician',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('degree', models.CharField(max_length=100)),
                ('expert', models.CharField(max_length=100)),
            ],
        ),
    ]
