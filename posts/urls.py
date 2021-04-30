from django.urls import path
from .views import PostListView,SignupCreateView

app_name = "posts"


urlpatterns = [
    path('', PostListView.as_view(), name="index"),
    path('create/', SignupCreateView.as_view(), name="Signup-create"),
]
