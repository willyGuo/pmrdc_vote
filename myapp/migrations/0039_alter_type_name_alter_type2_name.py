# Generated by Django 4.0.6 on 2022-10-12 15:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0038_type2_rename_person_type_addressinfo_publications2'),
    ]

    operations = [
        migrations.AlterField(
            model_name='type',
            name='name',
            field=models.CharField(blank=True, max_length=50),
        ),
        migrations.AlterField(
            model_name='type2',
            name='name',
            field=models.CharField(blank=True, max_length=50),
        ),
    ]