# Generated by Django 2.2 on 2019-12-14 12:59

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('ParaClininical', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Invoice',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Operation_record_id', models.ForeignKey(null=True, on_delete=True, to='ParaClininical.Operation_record')),
            ],
        ),
    ]