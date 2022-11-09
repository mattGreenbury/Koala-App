# Generated by Django 4.1.3 on 2022-11-09 17:16

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='KoalaDB',
            fields=[
                ('koala_id', models.BigAutoField(primary_key=True, serialize=False)),
                ('sex', models.CharField(max_length=1, verbose_name='m = male, f= female, u = unkown')),
                ('dob', models.DateField(blank=True, null=True, verbose_name='Koalas D.O.B if known else: leave blank')),
            ],
        ),
    ]
