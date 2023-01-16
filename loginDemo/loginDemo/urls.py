
from django.contrib import admin
from django.urls import path

from  login import  views
urlpatterns = [
    path('admin/', admin.site.urls),
    path(r'hello/',views.hello),
    path(r'register/',views.register)

]
