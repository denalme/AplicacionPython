# Generated by Django 2.2.12 on 2020-05-13 20:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('userdata', '0002_auto_20200512_2101'),
    ]

    operations = [
        migrations.AddField(
            model_name='datosuser',
            name='adddata',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AddField(
            model_name='datosuser',
            name='apelUser',
            field=models.CharField(max_length=200, null=True, verbose_name='Apellidos'),
        ),
        migrations.AddField(
            model_name='datosuser',
            name='geneUser',
            field=models.CharField(choices=[('Femenino', 'F'), ('Masculino', 'M'), ('Otro', 'O')], default='Otro', max_length=20, verbose_name='Género'),
        ),
        migrations.AddField(
            model_name='datosuser',
            name='modifiat',
            field=models.DateTimeField(auto_now=True, null=True),
        ),
        migrations.AddField(
            model_name='datosuser',
            name='nombUser',
            field=models.CharField(max_length=200, null=True, verbose_name='Nombres'),
        ),
        migrations.AddField(
            model_name='datosuser',
            name='profeUser',
            field=models.CharField(max_length=100, null=True, verbose_name='Profesión'),
        ),
        migrations.AlterField(
            model_name='datosuser',
            name='teleUser',
            field=models.CharField(max_length=20, verbose_name='Número de Teléfono'),
        ),
        migrations.AlterField(
            model_name='datosuser',
            name='userDNI',
            field=models.CharField(max_length=20, verbose_name='Identificación'),
        ),
        migrations.AlterField(
            model_name='detaroles',
            name='udtuser',
            field=models.DateTimeField(auto_now=True, null=True),
        ),
    ]