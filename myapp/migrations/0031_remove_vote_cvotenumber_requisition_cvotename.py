# Generated by Django 4.0.6 on 2022-10-02 08:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0030_alter_vote_cvotenumber'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='vote',
            name='cVotenumber',
        ),
        migrations.AddField(
            model_name='requisition',
            name='cVotename',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='myapp.vote'),
        ),
    ]
