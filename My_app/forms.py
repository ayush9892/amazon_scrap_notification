from django import forms
from .models import Link

class AddLinkForm(forms.ModelForm):  # ModelForms
    class Meta:
        model = Link                # The whole form is created for new url without again defining same database.
        fields = ('url',)           # It just show the template of URL. To add new url.

'''
=> Lets understand how it works.

First it make all the same fields present in models.py, then it takes the POST request and put it into fields, i.e url field.
then in views.py it checks, wheteher the url fiel is correct or not?. If it it correct then it takes all the data from url 
and saves it into all its fields, and finally create an object in database.

the region for taking none argument, is basically for like, we have seen in some web pages that, "its required to enter that 
field". So, if we not enter that field, we wiil not able to go further. So, we take None to skip this required field.

Or when we don't pass any POST request, then it only makes all the same fields present in models.py, and in url fields is empty. So, neither it
validate the url or neither it create the obj. 
'''
     
