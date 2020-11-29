# Generated by Django 3.1.3 on 2020-11-29 08:33

from django.db import migrations, models
import members.models


class Migration(migrations.Migration):

    dependencies = [
        ('members', '0002_members_member_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='members',
            name='first_name',
            field=models.CharField(default='', max_length=25),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='members',
            name='last_name',
            field=models.CharField(default='', max_length=25),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='members',
            name='middle_name',
            field=models.CharField(default='', max_length=25),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='members',
            name='slug',
            field=models.SlugField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='members',
            name='member_image',
            field=models.ImageField(null=True, upload_to=members.models.image_upload),
        ),
        migrations.AlterField(
            model_name='members',
            name='member_name',
            field=models.CharField(max_length=200, null=True),
        ),
    ]