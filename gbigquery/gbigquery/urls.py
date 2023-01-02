"""gbigquery URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
import app.views as app

urlpatterns = [
    path("addSetUnset/<int:client>/<int:customer_id>/<int:ad_group_id>/<int:ad_id>", app.addSetUnset, name='addSetUnset'),
    path('update/<int:cost>/<int:acquisition>', app.update, name='update'),
    path('roas', app.roas, name='roas'),
    path('cpc', app.cpc, name='cpc'),
    path('cpa', app.cpa, name='cpa'),
    path('create', app.create_table, name='createtable'),
    path('insert', app.insert_rows, name='insertDataSet'),
    path('list', app.list_datasets, name='listDataSet'),
    path('home', app.index, name='home'),
    path('admin/', admin.site.urls),
]
