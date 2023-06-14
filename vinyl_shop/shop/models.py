# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models
from django.db.models import Sum

class Customers(models.Model):
    customerid = models.AutoField(db_column='CustomerID', primary_key=True)  # Field name made lowercase.
    name = models.CharField(db_column='Name', max_length=30)  # Field name made lowercase.
    surname = models.CharField(db_column='Surname', max_length=50)  # Field name made lowercase.
    address = models.CharField(db_column='Address', max_length=100)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Customers'


class Deliveries(models.Model):
    dateofdelivery = models.DateTimeField(db_column='DateOfDelivery', primary_key=True)  # Field name made lowercase. The composite primary key (DateOfDelivery, VinylID) found, that is not supported. The first column is selected.
    vinylid = models.ForeignKey('Vinyls', models.DO_NOTHING, db_column='VinylID')  # Field name made lowercase.
    unitsdelivered = models.IntegerField(db_column='UnitsDelivered')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Deliveries'
        

class Sales(models.Model):
    saleid = models.AutoField(db_column='SaleID', primary_key=True)  # Field name made lowercase.
    customerid = models.ForeignKey(Customers, models.DO_NOTHING, db_column='CustomerID')  # Field name made lowercase.
    vinylid = models.ForeignKey('Vinyls', models.DO_NOTHING, db_column='VinylID')  # Field name made lowercase.
    dateoftransaction = models.DateTimeField(db_column='DateOfTransaction')  # Field name made lowercase.
    quantity = models.IntegerField(db_column='Quantity')  # Field name made lowercase.
    price = models.IntegerField(db_column='Price')
    
    class Meta:
        managed = False
        db_table = 'Sales'


class Vinyls(models.Model):
    vinylid = models.AutoField(db_column='VinylID', primary_key=True)  # Field name made lowercase.
    title = models.CharField(db_column='Title', max_length=130)  # Field name made lowercase.
    artist = models.CharField(db_column='Artist', max_length=100)  # Field name made lowercase.
    genre = models.CharField(db_column='Genre', max_length=30)  # Field name made lowercase.
    description = models.CharField(db_column='Description', max_length=200)  # Field name made lowercase.
    url = models.CharField(db_column='URL', max_length=200)  # Field name made lowercase.
    price = models.IntegerField(db_column='Price')
    
    @property
    def is_available(self):
        return get_units(self) > 0
    
    class Meta:
        managed = False
        db_table = 'Vinyls'

def get_units(vinyl):
    vid = vinyl.vinylid
    unitsDelivered = Deliveries.objects.filter(vinylid=vid).aggregate(total=Sum('unitsdelivered'))['total']
    if unitsDelivered is None:
        unitsDelivered = 0
    unitsSold = Sales.objects.filter(vinylid=vid).aggregate(total=Sum('quantity'))['total']
    if unitsSold is None:
        unitsSold = 0
    return unitsDelivered - unitsSold