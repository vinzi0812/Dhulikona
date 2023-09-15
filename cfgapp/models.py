from django.db import models

# Create your models here.
class Address(models.Model):
    street = models.CharField(max_length=50)
    village = models.CharField(max_length=50)
    district = models.CharField(max_length=50)

    def __str__(self):
        return self.street + ", " + self.village + ", " + self.district

class Villager(models.Model):
    name = models.CharField(max_length=50)
    phone = models.BigIntegerField(primary_key=True)
    isSarpanch = models.BooleanField(default=False)
    isPumpOp = models.BooleanField(default=False)
    isWqm = models.BooleanField(default=False)
    isWuc = models.BooleanField(default=False)
    address = models.OneToOneField(Address, on_delete=models.CASCADE)
    def __str__(self):
        return self.phone


class adminAcc(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=50)
    phone = models.BigIntegerField()
    password = models.CharField(max_length=50)
    address = models.OneToOneField(Address, on_delete=models.CASCADE)
    def __str__(self):
        return self.id

# class Quality(models.Model):
#     component = models.CharField(max_length=50)
#     minval = models.IntegerField()
#     maxval = models.IntegerField()

class Issues(models.Model):
    id = models.IntegerField(primary_key=True)
    village = models.CharField(max_length=50, null=True, blank=True)
    phone = models.BigIntegerField()
    stage = models.CharField(max_length=50)
    option1 = models.BooleanField(default=False)
    option2 = models.BooleanField(default=False)
    option3 = models.BooleanField(default=False)
    option4 = models.BooleanField(default=False)
    option5 = models.BooleanField(default=False)
    issue = models.TextField()
    date = models.DateField()

    def __str__(self):
        return self.issue + ", " + self.date

class WaterQuality(models.Model):
    village = models.CharField(max_length=50, null=True, blank=True)
    name = models.CharField(max_length=50, null=True, blank=True)
    date = models.DateField()
    pH = models.FloatField()
    chlorine_level = models.FloatField()
    turbidity = models.FloatField()
    taste = models.CharField(max_length=50)
    colour = models.CharField(max_length=50)
    status = models.BooleanField(default=False)
    def __str__(self):
        return self.pH + ", " + self.chlorine_level + ", " + self.turbidity + ", " + self.taste + ", " + self.colour
    

class PumpOperator(models.Model):
    id = models.IntegerField(primary_key=True)
    phone = models.BigIntegerField()
    name = models.CharField(max_length=20, blank=True)
    village = models.CharField(max_length=20, blank=True)
    date = models.DateField()
    status = models.BooleanField()

    def __str__(self):
        return self.phone + ", " + self.date + ", " + self.status
