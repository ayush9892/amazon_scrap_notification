from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from django.views.generic.base import View
from .models import Link
from .forms import AddLinkForm
from django.views.generic import DeleteView
from plyer import notification
from .auto import AUTO_UP, fst_chk

# Create your views here.

def home_view(request):    # function based view
    no_discounted = 0
    error = None

    form = AddLinkForm(request.POST or None)  # Bound form: it’s capable of validating that data and rendering the form as HTML with the data displayed in the HTML.

    if request.method == 'POST':
        try:
            if form.is_valid():  # If it passes through all the validations of forms.py, means if all the data is valid. Then it return True.
                form.save()     # After generating the database in form, finally it will Save(by the overridden save method in models.py) and create the object into database.
                return redirect('home')    
        except AttributeError:
            error = "Name and Price not available"
        except:
            error = "Something went wrong"

    form = AddLinkForm()        # Unbound form:  it can render the blank form as HTML.


    qs = Link.objects.all()   
    items_no = qs.count()       # It counts how many item present in your list.

    if items_no > 0:
        discount_list = []
        for item in qs:
            if item.old_price > item.current_price:
                discount_list.append(item)
            no_discounted = len(discount_list)


    ob_chk = fst_chk()              # creating an object
    old_discount = ob_chk.fst_val

    if (no_discounted > old_discount):
        title = "Amazon Product Discount!!!"

        message =" Discount is there in you product list !!!"

        notification.notify(title = title,
                            message = message,
                            app_icon = "icon.ico",
                            timeout = 10,
                            toast = False)

    fst_chk.fst_val = no_discounted

    if(ob_chk.html_upt_chk == 1):
        view_upt_opt = 1
        fst_chk.html_stp_chk = 0        # Initializing to zero, so it will not show me option of "Stop Auto Update".
    else:
        view_upt_opt = 0
        fst_chk.html_stp_chk = 1    # Initializing to one, so it will show me option  of "Stop Auto Update".

    if(ob_chk.html_stp_chk == 1):
        view_del_opt = 1
    else:
        view_del_opt = 0



    context = {                 # It is dictionary.
        'qs': qs,
        'items_no': items_no,
        'no_discounted': no_discounted,
        'form': form,
        'error': error,
        'view_upt_opt': view_upt_opt,
        'view_del_opt': view_del_opt,
    }

    return render(request, 'links/main.html', context)

class LinkDeleteView(DeleteView):   # Generic class based view: it will automaticlly gives you basic work
    model = Link                    # Benefit of using class based view is, it automatically give you that particular obj. You don,t need to specify that particular obj you wanna to delete. And also it automatically check the POST that you have submitted in the html form. If yes then it automatically delete that obj from dbs.
    template_name = 'links/confirm_del.html'
    success_url = reverse_lazy('home')

    '''=> Doing same thing using fun based View

    def delete_view(request, id):
    # dictionary for initial data with
    # field names as keys
    context ={}
 
    # fetch the object related to passed id
    obj = get_object_or_404(GeeksModel, id = id)
 
 
    if request.method =="POST":
        # delete object
        obj.delete()
        # after deleting redirect to
        # home page
        return HttpResponseRedirect("home")
 
    return render(request, "confirm_del.html", context)
    '''

def update_prices(request):     # function based view
    qs = Link.objects.all()
    for link in qs:
        link.save()
    return redirect('home')    

def Auto(request):
    fst_chk.html_upt_chk = 0             # Initializing to zero, so it will not show me option again of "Auto Update".
    ob_auto = AUTO_UP()
    ob_auto.Auto_update()
    fst_chk.html_upt_chk = 1
    if request.method == 'POST':
        return redirect('home') 

def stop_Auto(request):
    fst_chk.html_stp_chk = 0    # Initializing to zero, so it will not again show me option again of "Stop Auto Update".    
    fst_chk.html_upt_chk = 1    # Initializing to one, so it will again show me option of "Auto Update".
    AUTO_UP.stop = 1
    if request.method == 'POST':
        return redirect('home') 
