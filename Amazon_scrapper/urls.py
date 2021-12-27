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
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from My_app.views import home_view, update_prices, LinkDeleteView

admin.site.site_header = "Amazon Scraper"
admin.site.site_title = "Amazon Scraper Portal"
admin.site.index_title = "Ready to Scrape Products"

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home_view, name='home'),
    path('update/', update_prices, name='update-prices'),
    path('delete/<pk>/', LinkDeleteView.as_view(), name="delete"),
    
]
