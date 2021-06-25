# Generated by Django 3.2.4 on 2021-06-24 21:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Pata',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('largo', models.FloatField(null=True)),
                ('ancho', models.FloatField(null=True)),
                ('espesor', models.FloatField(null=True)),
                ('cantidad', models.IntegerField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Tablero',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('largo', models.IntegerField(null=True)),
                ('ancho', models.IntegerField(null=True)),
                ('espesor', models.FloatField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Tornillo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('largo', models.FloatField(null=True)),
                ('diametro', models.FloatField(null=True)),
                ('cantidad', models.IntegerField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Mesa',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('patas', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.pata')),
                ('tablero', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.tablero')),
                ('tornillos', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.tornillo')),
            ],
        ),
    ]