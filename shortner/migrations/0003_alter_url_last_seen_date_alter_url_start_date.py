# Generated by Django 4.0.4 on 2022-04-30 07:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shortner', '0002_alter_url_last_seen_date_alter_url_redirect_count_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='url',
            name='last_seen_date',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='url',
            name='start_date',
            field=models.DateField(blank=True, null=True),
        ),
    ]
