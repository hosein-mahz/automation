# Generated by Django 2.2 on 2019-12-21 18:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Accounting', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='invoice',
            name='Operation_record_id',
            field=models.ForeignKey(null=True, on_delete=True, related_name='invoice', to='ParaClininical.Operation_record'),
        ),
    ]
