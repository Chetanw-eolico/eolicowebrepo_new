from django.db import models
from django.core.exceptions import ValidationError


published_choices = [ ('yes', 'yes'), ('no', 'no')]
pricetype_choices = [('hammer', 'hammer'), ('premium', 'premium')]
lotstatus_choices = [('yet to be sold', 'yet to be sold'),('sold', 'sold'),('bought-in', 'bought-in'),('withdrawn', 'withdrawn')]

class Auction(models.Model):
    id = models.IntegerField(primary_key=True, unique=True, default=None, blank=False, null=False, db_column='faac_auction_ID')
    auctionname = models.TextField(db_column='faac_auction_title')
    auctionid = models.CharField(max_length=25, blank=True, default='', db_column='faac_auction_sale_code')
    auctionhouse_id = models.IntegerField(default=None, db_column='faac_auction_house_ID')
    #auctionlocation = models.CharField(max_length=200, blank=True, default='', db_column='faac_auction_location')
    #description = models.TextField(db_column='faac_auction_description')
    auctionurl = models.TextField(db_column='faac_auction_source')
    auctionstartdate = models.DateField(db_column='faac_auction_start_date')
    auctionenddate = models.DateField(db_column='faac_auction_end_date')
    #lotslistingurl = models.TextField()
    lotcount = models.IntegerField(db_column='faac_auction_lot_count')
    coverimage = models.TextField(db_column='faac_auction_image')
    #auctiontype = models.CharField(max_length=255, blank=True, default='') # Classifies the auctions as "Online", "Location Bound" etc.
    published = models.CharField(max_length=10, db_column='faac_auction_published', choices=published_choices)
    priority = models.IntegerField(default=5, db_column='faac_auction_priority')
    inserted = models.DateTimeField(auto_now_add=True, db_column='faac_auction_record_created')
    edited = models.DateTimeField(auto_now=True, db_column='faac_auction_record_updated')
    insertedby = models.CharField(max_length=25, db_column='faac_auction_record_createdby')
    editedby = models.CharField(max_length=25, db_column='faac_auction_record_updatedby')

    class Meta:
        verbose_name = "Auctions Information Table"
        db_table = 'fineart_auction_calendar'
        ordering = ('priority',)

    def __unicode__(self):
        return "%s"%(self.auctionname)


class Lot(models.Model):
    id = models.IntegerField(primary_key=True, unique=True, default=None, blank=False, null=False, db_column='fal_lot_ID')
    lotid = models.IntegerField(db_column='fal_lot_no')
    sublotid = models.CharField(max_length=10, blank=True, default='', db_column='fal_sub_lot_no')
    artwork_id = models.IntegerField(db_column='fal_artwork_ID')
    category = models.CharField(max_length=100, db_column='fal_lot_category')
    auction_id = models.IntegerField(db_column='fal_auction_ID')
    saledate = models.DateTimeField(db_column='fal_lot_sale_date')
    #lottitle = models.TextField(db_column='fal_lot_no')
    #lotdescription = models.TextField(db_column='fal_lot_no')
    #artistname = models.TextField(db_column='fal_lot_no')
    #artistbirth = models.CharField(max_length=50, blank=True, default='', db_column='fal_lot_no')
    #artistdeath = models.CharField(max_length=50, blank=True, default='')
    #artistnationality = models.CharField(max_length=100, blank=True, default='')
    medium = models.CharField(max_length=200, blank=True, default='', db_column='fal_lot_material')
    sizedetails = models.CharField(max_length=200, blank=True, default='', db_column='fal_lot_size_details')
    height = models.DecimalField(max_digits=13, decimal_places=2, db_column='fal_lot_height')
    width = models.DecimalField(max_digits=13, decimal_places=2, db_column='fal_lot_width')
    depth = models.DecimalField(max_digits=13, decimal_places=2, db_column='fal_lot_depth')
    measureunit = models.CharField(max_length=10, db_column='fal_lot_measurement_unit')
    #loturl = models.TextField(db_column='fal_lot_measurement_unit')
    category = models.CharField(max_length=200, blank=True, default='', db_column='fal_lot_category') # Could be 'Painting', 'Etching', 'Sculpture', etc.
    #auction = models.ForeignKey(Auction, blank=False, null=False, on_delete=models.CASCADE)
    #estimate = models.CharField(max_length=100, blank=True, default='')
    highestimate = models.DecimalField(max_digits=15, decimal_places=2, db_column='fal_lot_high_estimate')
    lowestimate = models.DecimalField(max_digits=15, decimal_places=2, db_column='fal_lot_low_estimate')
    highestimateUSD = models.DecimalField(max_digits=15, decimal_places=2, db_column='fal_lot_high_estimate_USD')
    lowestimateUSD = models.DecimalField(max_digits=15, decimal_places=2, db_column='fal_lot_low_estimate_USD')
    #soldprice = models.CharField(max_length=100, blank=True, default='')
    soldprice = models.DecimalField(max_digits=15, decimal_places=2, db_column='fal_lot_sale_price')
    soldpriceUSD = models.DecimalField(max_digits=15, decimal_places=2, db_column='fal_lot_sale_price_USD')
    pricetype = models.CharField(max_length=20, blank=True, default='', db_column='fal_lot_price_type', choices=pricetype_choices)
    #currency = models.CharField(max_length=10, blank=True, default='')
    condition = models.TextField(db_column='fal_lot_condition')
    status = models.CharField(max_length=20, blank=True, default='', db_column='fal_lot_status', choices=lotstatus_choices)
    provenance = models.TextField(db_column='fal_lot_provenance')
    #literature = models.TextField(db_column='fal_lot_price_type')
    #exhibited = models.TextField(db_column='fal_lot_price_type')
    published = models.CharField(max_length=20, db_column='fal_lot_published', choices=published_choices)
    lotimage1 = models.TextField(db_column='fal_lot_image1')
    lotimage2 = models.TextField(db_column='fal_lot_image2')
    lotimage3 = models.TextField(db_column='fal_lot_image3')
    lotimage4 = models.TextField(db_column='fal_lot_image4')
    lotimage5 = models.TextField(db_column='fal_lot_image5')
    priority = models.IntegerField(default=5, db_column='fal_lot_priority')
    inserted = models.DateTimeField(auto_now_add=True, db_column='fal_lot_record_created')
    edited = models.DateTimeField(auto_now=True, db_column='fal_lot_record_updated')
    insertedby = models.CharField(max_length=25, db_column='fal_lot_record_createdby')
    editedby = models.CharField(max_length=25, db_column='fal_lot_record_updatedby')
    #signature = models.TextField()
    #creationdate = models.CharField(max_length=50, blank=True, default='')
    source = models.TextField(db_column='fal_lot_source')
    

    class Meta:
        verbose_name = "Lots (Artworks) Information Table"
        db_table = 'fineart_lots'
        ordering = ('priority',)

    def __unicode__(self):
        return "%s"%(self.lottitle)




