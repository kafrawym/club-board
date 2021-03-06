# Generated by Django 3.1.3 on 2020-11-25 14:04

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Members',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('member_no', models.CharField(max_length=25)),
                ('member_name', models.CharField(max_length=200)),
                ('id_no', models.CharField(max_length=25)),
                ('created_date', models.DateTimeField(auto_now=True)),
                ('date_of_birth', models.DateField()),
                ('member_type', models.CharField(choices=[('Normal', 'Normal'), ('Active', 'Active'), ('Honer', 'Honer')], max_length=25)),
                ('gender', models.CharField(choices=[('Male', 'Male'), ('Female', 'Female'), ('Other', 'Other')], max_length=25)),
            ],
        ),
    ]
