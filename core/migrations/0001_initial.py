# Generated by Django 3.2.7 on 2021-09-16 20:01

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Depoimentos',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100, verbose_name='Nome')),
                ('cargo', models.CharField(max_length=100, verbose_name='Cargo')),
                ('foto', models.ImageField(upload_to='foto', verbose_name='Foto')),
                ('depoimento', models.CharField(max_length=200, verbose_name='Depoimento')),
            ],
        ),
    ]
