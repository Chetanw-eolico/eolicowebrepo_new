# Generated by Django 3.2.8 on 2022-04-11 10:25

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('gallery', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='artist',
            options={'ordering': ('-priority',), 'verbose_name': 'Artists Information Table'},
        ),
        migrations.AlterModelOptions(
            name='artwork',
            options={'ordering': ('-priority',), 'verbose_name': 'Artworks Information Table'},
        ),
        migrations.AlterModelOptions(
            name='event',
            options={'ordering': ('-priority',), 'verbose_name': 'Events Information Table'},
        ),
        migrations.AlterModelOptions(
            name='gallery',
            options={'ordering': ('-priority',), 'verbose_name': 'Galleries Information Table'},
        ),
        migrations.AddField(
            model_name='artist',
            name='event',
            field=models.ForeignKey(default=-1, on_delete=django.db.models.deletion.CASCADE, to='gallery.event'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='artist',
            name='priority',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='artwork',
            name='priority',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='event',
            name='eventenddate',
            field=models.DateTimeField(default=datetime.datetime(2022, 4, 11, 10, 25, 23, 318764)),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='event',
            name='eventimage',
            field=models.TextField(default=''),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='event',
            name='eventlocation',
            field=models.CharField(blank=True, default='', max_length=200),
        ),
        migrations.AddField(
            model_name='event',
            name='eventstartdate',
            field=models.DateTimeField(default=datetime.datetime(2022, 4, 11, 10, 25, 46, 863371)),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='event',
            name='priority',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='gallery',
            name='gallerytype',
            field=models.CharField(default='', max_length=255),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='gallery',
            name='priority',
            field=models.IntegerField(default=0),
        ),
    ]