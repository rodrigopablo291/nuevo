# Generated by Django 3.2.13 on 2022-05-04 23:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_rename_idustriaempresatitular_industriaempresatitular'),
    ]

    operations = [
        migrations.CreateModel(
            name='EmpresaTitular',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('nombreempresatitular', models.CharField(max_length=30)),
                ('descripcion', models.CharField(max_length=30)),
                ('idindustriaempresatitular', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.industriaempresatitular')),
            ],
            options={
                'verbose_name': 'EmpresaTitular',
                'verbose_name_plural': 'EmpresaTitular',
            },
        ),
    ]
