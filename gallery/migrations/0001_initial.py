# Generated by Django 3.2.8 on 2022-03-13 13:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Artist',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('artistname', models.CharField(max_length=255)),
                ('nationality', models.CharField(blank=True, max_length=255, null=True)),
                ('birthdate', models.CharField(blank=True, max_length=30, null=True)),
                ('deathdate', models.CharField(blank=True, max_length=10, null=True)),
                ('about', models.TextField()),
                ('profileurl', models.TextField()),
                ('gender', models.CharField(blank=True, max_length=10, null=True)),
                ('slug', models.CharField(blank=True, max_length=255, null=True)),
                ('squareimage', models.TextField()),
                ('largeimage', models.TextField()),
                ('edges', models.TextField()),
                ('inserted', models.DateTimeField(auto_now_add=True)),
                ('edited', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name': 'Artists Information Table',
                'db_table': 'artists',
            },
        ),
        migrations.CreateModel(
            name='Gallery',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('galleryname', models.TextField()),
                ('location', models.TextField()),
                ('description', models.TextField()),
                ('galleryurl', models.TextField()),
                ('website', models.TextField()),
                ('coverimage', models.TextField()),
                ('slug', models.CharField(blank=True, default='', max_length=255)),
                ('inserted', models.DateTimeField(auto_now_add=True)),
                ('edited', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name': 'Galleries Information Table',
                'db_table': 'galleries',
            },
        ),
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('eventname', models.CharField(max_length=255)),
                ('eventurl', models.TextField()),
                ('eventinfo', models.TextField()),
                ('eventtype', models.CharField(blank=True, default='', max_length=20)),
                ('eventstatus', models.CharField(blank=True, default='', max_length=15)),
                ('eventperiod', models.CharField(blank=True, default='', max_length=255)),
                ('artworkscount', models.IntegerField()),
                ('inserted', models.DateTimeField(auto_now_add=True)),
                ('edited', models.DateTimeField(auto_now=True)),
                ('gallery', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='gallery.gallery')),
            ],
            options={
                'verbose_name': 'Events Information Table',
                'db_table': 'events',
            },
        ),
        migrations.CreateModel(
            name='Artwork',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('artworkname', models.TextField()),
                ('creationdate', models.CharField(blank=True, max_length=10, null=True)),
                ('artistname', models.CharField(blank=True, max_length=255, null=True)),
                ('artistbirthyear', models.CharField(blank=True, max_length=4, null=True)),
                ('artistdeathyear', models.CharField(blank=True, max_length=4, null=True)),
                ('artistnationality', models.CharField(blank=True, max_length=4, null=True)),
                ('size', models.CharField(blank=True, max_length=255, null=True)),
                ('estimate', models.CharField(blank=True, max_length=100, null=True)),
                ('soldprice', models.CharField(blank=True, max_length=40, null=True)),
                ('medium', models.TextField()),
                ('signature', models.TextField()),
                ('letterofauthenticity', models.TextField()),
                ('description', models.TextField()),
                ('provenance', models.TextField()),
                ('literature', models.TextField()),
                ('exhibitions', models.TextField()),
                ('image1', models.TextField()),
                ('image2', models.TextField()),
                ('image3', models.TextField()),
                ('image4', models.TextField()),
                ('workurl', models.TextField()),
                ('inserted', models.DateTimeField(auto_now_add=True)),
                ('edited', models.DateTimeField(auto_now=True)),
                ('event', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='gallery.event')),
                ('gallery', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='gallery.gallery')),
            ],
            options={
                'verbose_name': 'Artworks Information Table',
                'db_table': 'artworks',
            },
        ),
    ]
