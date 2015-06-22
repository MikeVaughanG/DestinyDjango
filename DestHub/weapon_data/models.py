from django.db import models

# Create your models here.

class Weapon(models.Model):
    weapon_name = models.CharField(max_length=300)
    weapon_tier = models.CharField(max_length=35)
    weapon_descrip = models.CharField(max_length=600)
    weapon_type = models.CharField(max_length=35)

    weapon_rolls = models.CharField(max_length=10000)
    def __unicode__(self): 
        return self.weapon_name

