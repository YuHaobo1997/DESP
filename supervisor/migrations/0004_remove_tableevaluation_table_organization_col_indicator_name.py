# Generated by Django 3.1 on 2020-10-29 15:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('supervisor', '0003_tableorganization_table_organization_col_unicode'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='tableevaluation',
            name='table_organization_col_indicator_name',
        ),
    ]