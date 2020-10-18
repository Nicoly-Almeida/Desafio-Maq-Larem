# Generated by Django 3.1.2 on 2020-10-18 01:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_usuario_contatos'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contato',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('nome', models.CharField(max_length=100, verbose_name='nome')),
                ('celular', models.CharField(max_length=11, verbose_name='celular')),
                ('email', models.EmailField(max_length=254, verbose_name='email')),
                ('endereço', models.CharField(max_length=200, verbose_name='endereco')),
                ('dia', models.CharField(max_length=2, verbose_name='dia')),
                ('mes', models.CharField(max_length=2, verbose_name='mes')),
                ('ano', models.CharField(max_length=4, verbose_name='ano')),
            ],
        ),
        migrations.AlterField(
            model_name='usuario',
            name='contatos',
            field=models.ManyToManyField(blank=True, to='api.Contato'),
        ),
    ]
