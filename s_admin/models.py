from django.db import models


from django.db import models

class AdminLoginModel(models.Model):
    username = models.CharField(max_length=20,unique=True)
    password = models.CharField(max_length=30)
    otp = models.IntegerField()

class StateModel(models.Model):
    state_no = models.AutoField(primary_key=True)
    State_name = models.CharField(max_length=30,unique=True)

class CityModel(models.Model):
    city_no = models.AutoField(primary_key=True)
    city_name = models.CharField(max_length=30,unique=True)
    city_state = models.ForeignKey(StateModel,on_delete=models.CASCADE)

class AreaModel(models.Model):
    area_no = models.AutoField(primary_key=True)
    area_name = models.CharField(max_length=30,unique=True)
    area_city = models.ForeignKey(CityModel,on_delete=models.CASCADE)

class RestaurenttypeModel(models.Model):
    no = models.AutoField(primary_key=True)
    type_name = models.CharField(max_length=50)
