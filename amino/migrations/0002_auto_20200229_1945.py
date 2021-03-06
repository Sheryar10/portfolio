# Generated by Django 3.0.3 on 2020-02-29 14:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('amino', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='amino',
            old_name='title',
            new_name='amino_name',
        ),
        migrations.RenameField(
            model_name='amino',
            old_name='price',
            new_name='mol_weight',
        ),
        migrations.RenameField(
            model_name='amino',
            old_name='description',
            new_name='symbol',
        ),
        migrations.RemoveField(
            model_name='amino',
            name='summary',
        ),
        migrations.AddField(
            model_name='amino',
            name='symbol_3_letters',
            field=models.TextField(blank=True, null=True),
        ),
    ]
