from django.contrib import admin
from .models import Post,Catagory,Author


admin.site.register([Post,Catagory,Author])
