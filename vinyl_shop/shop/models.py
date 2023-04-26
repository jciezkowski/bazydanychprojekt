# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior       
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Auctionitem(models.Model):
    itemid = models.AutoField(db_column='ItemID', primary_key=True)  # Field name made lowercase.   
    title = models.TextField(db_column='Title')  # Field name made lowercase.
    artist = models.TextField(db_column='Artist')  # Field name made lowercase.
    genre = models.TextField(db_column='Genre')  # Field name made lowercase.
    description = models.TextField(db_column='Description', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'AuctionItem'


class Auctions(models.Model):
    auctionid = models.AutoField(db_column='AuctionID', primary_key=True)  # Field name made lowercase.
    sellersusername = models.ForeignKey('Registeredclients', models.DO_NOTHING, db_column='SellersUsername')  # Field name made lowercase.
    employeeid = models.ForeignKey('Employees', models.DO_NOTHING, db_column='EmployeeID')  # Field 
# name made lowercase.
    itemid = models.ForeignKey(Auctionitem, models.DO_NOTHING, db_column='ItemID')  # Field name made lowercase.
    startdatetime = models.BinaryField(db_column='StartDateTime')  # Field name made lowercase.     
    enddatetime = models.TextField(db_column='EndDateTime')  # Field name made lowercase.
    checkedbystaff = models.IntegerField(db_column='CheckedByStaff', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Auctions'


class Bids(models.Model):
    username = models.OneToOneField('Registeredclients', models.DO_NOTHING, db_column='Username', primary_key=True)  # Field name made lowercase. The composite primary key (Username, Timestamp, AuctionID) found, that is not supported. The first column is selected.
    timestamp = models.TextField(db_column='Timestamp')  # Field name made lowercase.
    auctionid = models.ForeignKey(Auctions, models.DO_NOTHING, db_column='AuctionID')  # Field name 
# made lowercase.
    value = models.IntegerField(db_column='Value')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Bids'


class Clients(models.Model):
    clientid = models.AutoField(db_column='ClientID', primary_key=True)  # Field name made lowercase.
    name = models.TextField(db_column='Name')  # Field name made lowercase.
    surname = models.TextField(db_column='Surname')  # Field name made lowercase.
    address = models.TextField(db_column='Address')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Clients'


class Deliveries(models.Model):
    unitsdelivered = models.IntegerField(db_column='UnitsDelivered')  # Field name made lowercase.  
    dateofdelivery = models.TextField(db_column='DateOfDelivery', primary_key=True)  # Field name made lowercase. The composite primary key (DateOfDelivery, VinylID) found, that is not supported. The 
# first column is selected.
    vinylid = models.ForeignKey('Vinyls', models.DO_NOTHING, db_column='VinylID')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Deliveries'


class Employees(models.Model):
    employeeid = models.AutoField(db_column='EmployeeID', primary_key=True)  # Field name made lowercase.
    name = models.TextField(db_column='Name')  # Field name made lowercase.
    surname = models.TextField(db_column='Surname')  # Field name made lowercase.
    email = models.TextField(db_column='Email', blank=True, null=True)  # Field name made lowercase.    jobposition = models.TextField(db_column='JobPosition', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Employees'


class Registeredclients(models.Model):
    username = models.TextField(db_column='Username', primary_key=True)  # Field name made lowercase.
    password = models.TextField(db_column='Password')  # Field name made lowercase.
    email = models.TextField(db_column='Email', unique=True)  # Field name made lowercase.
    clientid = models.OneToOneField(Clients, models.DO_NOTHING, db_column='ClientID')  # Field name 
# made lowercase.

    class Meta:
        managed = False
        db_table = 'RegisteredClients'


class Sales(models.Model):
    saleid = models.AutoField(db_column='SaleID', primary_key=True)  # Field name made lowercase.   
    dateoftransaction = models.TextField(db_column='DateOfTransaction')  # Field name made lowercase.
    clientid = models.ForeignKey(Clients, models.DO_NOTHING, db_column='ClientID', blank=True, null=True)  # Field name made lowercase.
    vinylid = models.IntegerField(db_column='VinylID', blank=True, null=True)  # Field name made lowercase.
    quantity = models.IntegerField(db_column='Quantity', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Sales'


class Vinyls(models.Model):
    vinylid = models.AutoField(db_column='VinylID', primary_key=True)  # Field name made lowercase. 
    title = models.TextField(db_column='Title')  # Field name made lowercase.
    artist = models.TextField(db_column='Artist')  # Field name made lowercase.
    genre = models.TextField(db_column='Genre')  # Field name made lowercase.
    description = models.TextField(db_column='Description', blank=True, null=True)  # Field name 
        # made lowercase.

    class Meta:
        managed = False
        db_table = 'Vinyls'


class Workshopjobs(models.Model):
    jobid = models.AutoField(db_column='JobID', primary_key=True)  # Field name made lowercase.     
    clientid = models.ForeignKey(Clients, models.DO_NOTHING, db_column='ClientID')  # Field name made lowercase.
    employeeid = models.ForeignKey(Employees, models.DO_NOTHING, db_column='EmployeeID')  # Field name made lowercase.
    description = models.TextField(db_column='Description')  # Field name made lowercase.
    status = models.TextField(db_column='Status', blank=True, null=True)  # Field name made lowercase.
    ordereddate = models.TextField(db_column='OrderedDate', blank=True, null=True)  # Field name made lowercase.
    completeddate = models.TextField(db_column='CompletedDate', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'WorkshopJobs'