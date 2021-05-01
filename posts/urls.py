from django.urls import path
from .views import index

app_name = "posts"


urlpatterns = [
    path('', index, name="index"),
   # path('create/', SignupCreateView.as_view(), name="Signup-create"),
]
