# Generated by Django 3.2.8 on 2022-05-11 18:18

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Artist',
            fields=[
                ('id', models.IntegerField(db_column='fa_artist_ID', default=None, primary_key=True, serialize=False, unique=True)),
                ('artistname', models.CharField(db_column='fa_artist_name', max_length=255)),
                ('prefix', models.CharField(db_column='fa_artist_name_prefix', max_length=25)),
                ('suffix', models.CharField(db_column='fa_artist_name_suffix', max_length=25)),
                ('nationality', models.CharField(blank=True, db_column='fa_artist_nationality', max_length=255, null=True)),
                ('birthyear', models.CharField(blank=True, db_column='fa_artist_birth_year', max_length=10, null=True)),
                ('deathyear', models.CharField(blank=True, db_column='fa_artist_death_year', max_length=10, null=True)),
                ('birthyearidentifier', models.CharField(blank=True, choices=[('exact', 'exact'), ('after', 'after'), ('before', 'before'), ('circa', 'circa')], db_column='fa_artist_birth_year_identifier', max_length=20, null=True)),
                ('deathyearidentifier', models.CharField(blank=True, choices=[('exact', 'exact'), ('after', 'after'), ('before', 'before'), ('circa', 'circa')], db_column='fa_artist_death_year_identifier', max_length=20, null=True)),
                ('birthyearprecision', models.CharField(blank=True, choices=[('decade', 'decade'), ('century', 'century'), ('millennial', 'millennial')], db_column='fa_artist_birth_year_precision', max_length=20, null=True)),
                ('deathyearprecision', models.CharField(blank=True, choices=[('decade', 'decade'), ('century', 'century'), ('millennial', 'millennial')], db_column='fa_artist_death_year_precision', max_length=20, null=True)),
                ('description', models.TextField(db_column='fa_artist_description')),
                ('aka', models.CharField(blank=True, db_column='fa_artist_aka', max_length=100, null=True)),
                ('bio', models.TextField(db_column='fa_artist_bio')),
                ('genre', models.CharField(blank=True, db_column='fa_artist_genre', max_length=255, null=True)),
                ('artistimage', models.TextField(db_column='fa_artist_image')),
                ('priority', models.IntegerField(db_column='fa_artist_priority', default=0)),
                ('inserted', models.DateTimeField(auto_now_add=True, db_column='fa_artist_record_created')),
                ('edited', models.DateTimeField(auto_now=True, db_column='fa_artist_record_updated')),
                ('insertedby', models.CharField(blank=True, db_column='fa_arist_record_createdby', max_length=25, null=True)),
                ('editedby', models.CharField(blank=True, db_column='fa_artist_record_updatedby', max_length=25, null=True)),
            ],
            options={
                'verbose_name': 'Artists Information Table',
                'db_table': 'fineart_artists',
                'ordering': ('priority',),
            },
        ),
        migrations.CreateModel(
            name='Artwork',
            fields=[
                ('id', models.IntegerField(db_column='faa_artwork_ID', default=None, primary_key=True, serialize=False, unique=True)),
                ('artworkname', models.TextField(db_column='faa_artwork_title')),
                ('review', models.TextField(db_column='faa_artwork_requires_review')),
                ('creationstartdate', models.CharField(blank=True, db_column='faa_artwork_start_year', max_length=100, null=True)),
                ('creationenddate', models.CharField(blank=True, db_column='faa_artwork_end_year', max_length=100, null=True)),
                ('startyearidentifier', models.CharField(blank=True, choices=[('exact', 'exact'), ('after', 'after'), ('before', 'before'), ('circa', 'circa')], db_column='faa_artwork_start_year_identifier', max_length=100, null=True)),
                ('endyearidentifier', models.CharField(blank=True, choices=[('exact', 'exact'), ('after', 'after'), ('before', 'before'), ('circa', 'circa')], db_column='faa_artwork_end_year_identifier', max_length=100, null=True)),
                ('startyearprecision', models.CharField(blank=True, choices=[('decade', 'decade'), ('century', 'century'), ('millennial', 'millennial')], db_column='faa_artwork_start_year_precision', max_length=100, null=True)),
                ('endyearprecision', models.CharField(blank=True, choices=[('decade', 'decade'), ('century', 'century'), ('millennial', 'millennial')], db_column='faa_artwork_end_year_precision', max_length=100, null=True)),
                ('artist_id', models.IntegerField(db_column='faa_artist_ID', null=True)),
                ('artist2_id', models.IntegerField(db_column='faa_artist2_ID', null=True)),
                ('artist3_id', models.IntegerField(db_column='faa_artist3_ID', null=True)),
                ('artist4_id', models.IntegerField(db_column='faa_artist4_ID', null=True)),
                ('sizedetails', models.CharField(blank=True, db_column='faa_artwork_size_details', max_length=255, null=True)),
                ('height', models.DecimalField(db_column='faa_artwork_height', decimal_places=2, max_digits=13)),
                ('width', models.DecimalField(db_column='faa_artwork_width', decimal_places=2, max_digits=13)),
                ('depth', models.DecimalField(db_column='faa_artwork_depth', decimal_places=2, max_digits=13)),
                ('measureunit', models.CharField(blank=True, db_column='faa_arwork_measurement_unit', max_length=255, null=True)),
                ('medium', models.TextField(db_column='faa_artwork_material')),
                ('edition', models.TextField(db_column='faa_artwork_edition')),
                ('category', models.TextField(db_column='faa_artwork_category')),
                ('signature', models.TextField(db_column='faa_artwork_markings')),
                ('description', models.TextField(db_column='faa_artwork_description')),
                ('literature', models.TextField(db_column='faa_artwork_literature')),
                ('exhibitions', models.TextField(db_column='faa_artwork_exhibition')),
                ('priority', models.IntegerField(db_column='faa_artwork_priority', default=5)),
                ('image1', models.TextField(db_column='faa_artwork_image1')),
                ('inserted', models.DateTimeField(auto_now_add=True, db_column='faa_artwork_record_created')),
                ('edited', models.DateTimeField(auto_now=True, db_column='faa_artwork_record_updated')),
                ('insertedby', models.CharField(blank=True, db_column='faa_artwork_record_createdby', max_length=25, null=True)),
                ('editedby', models.CharField(blank=True, db_column='faa_artwork_record_updatedby', max_length=25, null=True)),
            ],
            options={
                'verbose_name': 'Artworks Information Table',
                'db_table': 'fineart_artworks',
                'ordering': ('priority',),
            },
        ),
    ]
