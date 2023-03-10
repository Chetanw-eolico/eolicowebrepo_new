from django.db import models
from django.core.exceptions import ValidationError
from  django.core.validators import validate_email
from django.contrib.auth.models import User as djUser
from artists.models import Artist

favourite_choices = [('fineart_artists', 'fineart_artists'), ('fineart_artworks', 'fineart_artworks'), ('fineart_auction_calendar', 'fineart_auction_calendar')]

def profpicpath(instance, filename):
    return '/'.join([instance.user.displayname, 'images/profile', filename])


class User(models.Model):
    firstname = models.CharField(max_length=100)
    middlename = models.CharField(max_length=20)
    lastname = models.CharField(max_length=100)
    displayname = models.CharField(max_length=100, unique=True)
    password = models.CharField(max_length=100)
    emailid = models.EmailField(unique=True, validators=[validate_email, ])
    active = models.BooleanField(default=True, help_text='Specifies whether the user is an active member or not.')
    istest = models.BooleanField(default=False, help_text='Specifies whether the user object is a result of some testing or not.')
    joindate = models.DateTimeField(auto_now_add=True) # set the field to now when the object is first created
    sex = models.CharField(max_length=3, choices=(('M', 'Male'),('F', 'Female'), ('U', 'Undisclosed')), default='U')
    # usertype defines the type of user: CORP users are corporates that conduct tests for recruitment or internal performance evaluation,
    # CONS are consultants that act as a middleman between corporates and candidates seeking opportunities, ACAD users conduct tests
    # for academic purposes, CERT users are those who conduct tests to certify a candidate's knowledge on a specific subject, and finally
    # OTHR users are the ones who do not fall in any of the above 4 categories.
    usertype = models.CharField(max_length=4, choices=(('ART', 'Artist'), ('BUY', 'Buyer'), ('ANO', 'Anonymous User'), ('ADM', 'Administrator')))
    mobileno = models.CharField(max_length=12, blank=True)
    userpic = models.ImageField(max_length=100, upload_to=profpicpath, help_text='Path to user\'s profile image.')
    newuser = models.BooleanField(default=False, help_text='False if user hasn\'t validated her/his email address')
    #skinpic = models.ImageField(max_length=100, upload_to=profpicpath)

    class Meta:
        verbose_name = "User Information Table"
        db_table = 'Auth_user'

    def __unicode__(self):
        return "%s %s %s (%s)"%(self.firstname, self.middlename, self.lastname, self.displayname)



class Session(models.Model):
    sessioncode = models.CharField(max_length=50, unique=True)
    status = models.BooleanField(default=True) # Will be 'True' as soon as the user logs in, and will be 'False' when user logs out.
    # The 'status' will automatically be set to 'False' after a predefined period. So users will need to login again after that period.
    # The predefined value will be set in the settings file skills_settings.py. (skills_settings.SESSION_EXPIRY_LIMIT)
    user = models.ForeignKey(User, null=False, blank=False, db_column='userid_id', on_delete=models.CASCADE)
    starttime = models.DateTimeField(auto_now_add=True) # Should be automatically set when the object is created.
    endtime = models.DateTimeField(default=None)
    sourceip = models.GenericIPAddressField(protocol='both', help_text="IP of the client's/user's host")
    istest = models.BooleanField(default=False) # Set it to True during testing the app.
    useragent = models.CharField(max_length=255, default="", help_text="Signature of the browser of the client/user") # Signature of the user-agent to guess the device used by the user.
    # This info may later be used for analytics.


    class Meta:
        verbose_name = "Session Information Table"
        db_table = 'Auth_session'
    
    def __unicode__(self):
        return self.sessioncode

    def isauthenticated(self):
        if self.status and self.user.active:
            return self.user
        else:
            return None

    def save(self, **kwargs):
        super(Session, self).save(kwargs)

"""
class Privilege(models.Model):
    privname = models.CharField(max_length=50, unique=True)
    privdesc = models.TextField(default="")
    createdate = models.DateTimeField(auto_now_add=True) # Date and time at which this privilege was created.

    class Meta:
        verbose_name = "Authorization Information"
        verbose_name_plural = "Privileges Information"
        db_table = 'Auth_privilege'

    def __unicode__(self):
        return "%s - %s"%(self.privname, self.privdesc)


class UserPrivilege(models.Model):
    user = models.ForeignKey(User, db_column='userid_id', on_delete=models.CASCADE)
    privilege = models.ForeignKey(Privilege, null=False, blank=False, db_column='privilegeid_id', on_delete=models.CASCADE)
    lastmod = models.DateTimeField(auto_now=True) # Date and time at which this privilege was last modified.
    status = models.BooleanField(default=True) # This will be used in a case where the user has a privilege but
    # is not allowed to use it for a certain span of time. For example, a user may be allowed to conduct a test
    # only once in a month (a little far-fetched, but it might be necessary later).

    class Meta:
        verbose_name = "User Privileges Information"
        db_table = 'Auth_userprivilege'

    def __unicode__(self):
        return "user id: %s === privilege id: %s"%(self.user.id, self.privilege.id)


class WebConfig(models.Model):
    pagename = models.CharField(max_length=255)
    path = models.TextField()
    paramname = models.CharField(max_length=255)
    paramvalue = models.TextField()
    adminuser = models.ForeignKey(djUser, db_column='adminuser_id', on_delete=models.CASCADE)
    inserted = models.DateTimeField(auto_now_add=True)
    edited = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Website Configuration Information"
        db_table = 'webconfig'

    def __unicode__(self):
        return "page path: %s"%(self.page)


class Carousel(models.Model):
    title = models.CharField(max_length=255, null=False, blank=False)
    textvalue = models.TextField()
    imagepath = models.TextField()
    datatype = models.CharField(max_length=200, null=False, default='Artist')
    data_id = models.IntegerField(default=1)
    priority = models.IntegerField(default=0)
    inserted = models.DateTimeField(auto_now_add=True)
    edited = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Website Carousel Information"
        db_table = 'carousel'
        ordering = ('-edited', '-priority',)

    def __unicode__(self):
        return "Title: %s"%(self.title)


class Follow(models.Model):
    user = models.ForeignKey(djUser, db_column='user_id', on_delete=models.CASCADE)
    artist = models.ForeignKey(Artist, db_column='artist_id', on_delete=models.CASCADE)
    user_session_key = models.CharField(max_length=40, default=None)
    status = models.BooleanField(default=True)
    createdon = models.DateTimeField(auto_now_add=True)
    updatedon = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "User Following An Artist"
        db_table = 'fa_user_follows'

    def __unicode__(self):
        return ""
"""

class Favourite(models.Model):
    user = models.ForeignKey(djUser, db_column='user_id', on_delete=models.CASCADE)
    reference_model = models.CharField(max_length=40, default='fineart_artists', blank=False, db_column='reference_table', choices=favourite_choices)
    reference_model_id = models.IntegerField(blank=False, null=False, db_column='referenced_table_id')
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "User's Favourite Artist/Artwork/Auction"
        db_table = 'user_favorites'

    def __unicode__(self):
        return ""


class EmailAlerts(models.Model):
    user = models.ForeignKey(djUser, db_column='user_id', on_delete=models.CASCADE)
    emailcontent = models.TextField(db_column='email_content')
    emailtype = models.CharField(max_length=20, default='artist', blank=False, db_column='email_type')
    emaildate = models.DateTimeField(auto_now=True, db_column='email_date')
    sendstatus = models.BooleanField(default=True, db_column='send_status')

    class Meta:
        verbose_name = "Email Alerts Table"
        db_table = 'user_email_alert'

    def __unicode__(self):
        return ""

