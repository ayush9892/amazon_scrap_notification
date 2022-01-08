from django.db import models
from .scrape import get_link_data

# Create your models here.

class Link(models.Model):
    name = models.CharField(max_length=220, blank=True) 
    url = models.URLField()
    current_price = models.FloatField(blank=True)
    old_price = models.FloatField(default=0)
    price_difference = models.FloatField(default=0)
    update = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):                                # This is used to string representation of that object. Basically it helpful for human reading. Instead of showing "object 1" in Admin. It showing the name of object.
        return str(self.name)
    

    class Meta:                                     # The classes that generate other child classes are defined as metaclasses.
        ordering = ('price_difference', '-created') # It indicate that how do we want to order our objects. It orders our all objects of Link class on the basis of minimum price difference and latest date.
         

    # This save method is overriding, the already defined save method in Model class. The benefit of doing overriding save method is, before saving, the developer may need to be modified may need to modify data first, then after it save it.
    def save(self, *args, **kwargs):  # *args allows to accept multiple arguments without knowing how many arguments.
        name, price = get_link_data(self.url)  # kwargs allows to accept variable length argument lists. We use ** because it allows to pass Keywords arguments(means variables with names). You can see like a dictionary. 
        old_price = self.current_price          # self is used to represent the instances of the class.
        if self.current_price:
            if price != old_price:
                diff = price - old_price
                self.price_difference = round(diff, 2)  # It round up the float value up to 2, after decimal.
                self.old_price = old_price
                self.current_price = price
        else:
            self.old_price = 0
            self.price_difference = 0

        self.name = name
        self.current_price = price 

        super().save(*args, **kwargs)  # A parent class can be referred to with the use of the super() function. Here the parent class is models.
                                        # The super function returns a temporary object of the superclass that allows access to all of its methods to its child class.