# Generated by Django 4.0.4 on 2022-04-30 06:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shortner', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='url',
            name='last_seen_date',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='url',
            name='redirect_count',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='url',
            name='shortcode',
            field=models.CharField(max_length=100, unique=True),
        ),
        migrations.AlterField(
            model_name='url',
            name='start_date',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
