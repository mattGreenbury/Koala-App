from django.db import models

# Create your models here.
class KoalaDB(models.Model):
    koala_id = models.BigAutoField(primary_key = True)
    sex = models.CharField("m = male, f= female, u = unkown", max_length=1)
    dob = models.DateField("Koalas D.O.B if known else: leave blank", blank= True, null = True)

    # clean table names for admin
    def __str__(self):
        return 'Koala ' + str(self.koala_id)

    @property
    def gender(self):
        if self.sex == 'm':
            fullSex = 'Male'
        elif self.sex == 'f':
            fullSex = 'Female'
        else: fullSex = 'Uknown'
        return 'The koalas sex is ' + fullSex