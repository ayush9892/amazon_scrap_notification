"""Amazon_scrapper URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from My_app.views import home_view, update_prices, LinkDeleteView, Auto, stop_Auto

admin.site.site_header = "Amazon Scraper"
admin.site.site_title = "Amazon Scraper Portal"
admin.site.index_title = "Ready to Scrape Products"

urlpatterns = [
    path('admin/', admin.site.urls),
    path('auto/', Auto, name='AUTO'),
    path('auto_rev/', stop_Auto, name='REV-AUTO'),
    path('', home_view, name='home'),     # function based view
    path('update/', update_prices, name='update-prices'), # function based view
    path('delete/<pk>/', LinkDeleteView.as_view(), name="delete"),  # class based view. Basically server will not understand class and obj, it only understand the funs. So, "as_view" works here for taking instances or dispacthing or other stuffs...
    
]
