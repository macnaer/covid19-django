# Generated by Django 3.1.3 on 2020-11-09 15:24

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='covid19',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('country', models.CharField(max_length=250)),
                ('countrycode', models.CharField(max_length=250)),
                ('slug', models.CharField(max_length=250)),
                ('newconfirmed', models.CharField(max_length=250)),
                ('totalconfirmed', models.CharField(max_length=250)),
                ('newdeaths', models.CharField(max_length=250)),
                ('totaldeaths', models.CharField(max_length=250)),
                ('newrecovered', models.CharField(max_length=250)),
                ('totalrecovered', models.CharField(max_length=250)),
            ],
            options={
                'verbose_name': 'covid19',
                'verbose_name_plural': 'covid19',
            },
        ),
    ]
