# Generated by Django 2.2.11 on 2020-03-18 22:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_load_initial_data'),
    ]

    operations = [
        migrations.CreateModel(
            name='CustomModel344pm',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('meaningless_field', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='CustomModel345pm',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('test', models.BigIntegerField()),
            ],
        ),
    ]
