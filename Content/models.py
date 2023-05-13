from django.db import models

COLOUR_CHOICES = (
    ("red", "red"),
    ("black", "black"),
    ("nude", "nude"),
    ("pink", "pink"),
    ("brown", "brown"),
    ("purple","purple"),
    ("white", "white")    
)

GENDER_CHOICES = (
    ("male", "male"),
    ("female", "female")
)


class cosmetics(models.Model):
    name = models.CharField(max_length=100)
    gender = models.CharField(choices=GENDER_CHOICES, max_length=100)
    colour = models.CharField(choices=COLOUR_CHOICES,max_length=100)
    company = models.CharField(max_length=100)
    description = models.TextField()
    quantity = models.IntegerField()
    phone_number = models.BigIntegerField()
    passport = models.ImageField(upload_to="passport_pictures",default="default.jpg", blank=True, null=True) 
    
    # def __str__(self):
    #     return self.name
