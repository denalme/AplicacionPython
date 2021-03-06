# Generated by Django 2.2.12 on 2020-06-05 03:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('userdata', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='CategProye',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Lenguaje', models.CharField(max_length=50, verbose_name='Lenguaje')),
                ('MotorDB', models.CharField(max_length=155, verbose_name='Motor de Base De Datos')),
                ('Arquitectura', models.CharField(max_length=255, verbose_name='Arquitectura')),
            ],
            options={
                'verbose_name': 'Categoria del Proyecto',
                'verbose_name_plural': 'Categorias',
            },
        ),
        migrations.CreateModel(
            name='TipoDocu',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('NombTiDoc', models.CharField(max_length=45, verbose_name='Nombre Tipo Documento')),
            ],
            options={
                'verbose_name': 'Tipo Documento',
                'verbose_name_plural': 'Tipos de Documentos',
            },
        ),
        migrations.CreateModel(
            name='Proyectos',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('NombProyect', models.CharField(max_length=45, verbose_name='Nombre Del Proyecto')),
                ('descproyect', models.TextField(verbose_name='Descripción del proyecto')),
                ('logoProyect', models.ImageField(upload_to='img/proyectos', verbose_name='Icono')),
                ('FechaIni', models.DateTimeField(verbose_name='Fecha de Inicio')),
                ('FechaFin', models.DateTimeField(verbose_name='Fecha de Finalización')),
                ('UrlRepo', models.TextField(verbose_name='Url del Repositorio')),
                ('EstaProy', models.CharField(max_length=45, verbose_name='Estado del Proyecto')),
                ('idCategProye', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='proyectos.CategProye')),
            ],
            options={
                'verbose_name': 'Proyectos de Usuarios',
                'verbose_name_plural': 'Proyectos y Experiencias',
            },
        ),
        migrations.CreateModel(
            name='Documentos',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('NombDocu', models.CharField(max_length=50, verbose_name='Nombre Del Documento')),
                ('PathDocu', models.CharField(max_length=50, verbose_name='Ruta de Almacenamiento del Documento')),
                ('idProyectos', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='proyectos.Proyectos')),
                ('idTipoDocu', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='proyectos.TipoDocu')),
                ('idUsuarios', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='userdata.DatosUser')),
            ],
            options={
                'verbose_name': 'Documento',
                'verbose_name_plural': 'Documentos',
            },
        ),
    ]
