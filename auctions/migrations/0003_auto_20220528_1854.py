# Generated by Django 3.2.8 on 2022-05-28 18:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0002_auto_20220511_1818'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='auction',
            options={'verbose_name': 'Auctions Information Table'},
        ),
        migrations.AlterModelOptions(
            name='lot',
            options={'verbose_name': 'Lots (Artworks) Information Table'},
        ),
    ]
