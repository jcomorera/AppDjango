# Generated by Django 2.1.5 on 2019-02-03 17:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('publicacion', '0003_publicacion_imagen'),
    ]

    operations = [
        migrations.AlterField(
            model_name='publicacion',
            name='imagen',
            field=models.ImageField(upload_to='img/posts/'),
        ),
    ]
