from django.db import models

# Create your models here.
class Films(models.Model):
    name = models.CharField(max_length = 100)
    description = models.TextField()
    pic = models.ImageField( upload_to='pics')
    # special = models.BooleanField(default = False)
    star = models.FloatField(default= 5.0)
    genre = models.CharField(max_length = 30, default='Action')
    actors = models.TextField(max_length= 500)
    runtime = models.IntegerField(default = 60)
    year = models.IntegerField(default = 2021)
    is_popular = models.BooleanField(default=False)
    is_top_rated = models.BooleanField(default=False)
    is_coming_soon = models.BooleanField(default=False)
    price = models.IntegerField(default=10000)
    day = models.IntegerField(default = 2)

    def isTopRate(self):
        if self.star >= 8.0:
            return True
        else:
            return False

    def Showday(self):
        if self.day == 2:
            return 2
        if self.day == 7:
            return 7
        if self.day == 4:
            return 4
        if self.day == 6:
            return 6
        

    def __str__(self):
        return self.name
    
    
