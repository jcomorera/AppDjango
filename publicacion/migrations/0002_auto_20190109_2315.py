# Generated by Django 2.1.2 on 2019-01-09 22:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('publicacion', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='publicacion',
            old_name='modificacion',
            new_name='actualizado',
        ),
        migrations.RenameField(
            model_name='publicacion',
            old_name='insercion',
            new_name='insertado',
        ),
    ]