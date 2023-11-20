from django.db import models

class Item(models.Model):
    item = models.CharField(max_length=100)
    item_name = models.CharField(max_length=100,default='')
    category = models.CharField(max_length=100,default='')
    subcategory = models.CharField(max_length=100,default='')
    price = models.IntegerField(default=0)    
    desc = models.TextField(max_length = 300)
    pub_date = models.DateField()
    image = models.ImageField(upload_to ='shop/images',default ='')

    def __str__(self):
        return self.item_name
    


