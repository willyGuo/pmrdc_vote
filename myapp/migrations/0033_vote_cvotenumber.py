# Generated by Django 4.0.6 on 2022-10-03 12:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0032_remove_requisition_cvotename'),
    ]

    operations = [
        migrations.AddField(
            model_name='vote',
            name='cVotenumber',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='myapp.requisition'),
        ),
    ]
