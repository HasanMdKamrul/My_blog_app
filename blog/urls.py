from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path,include
from posts.views import blog,post,index


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index , name= "index"),
    path('blog/', blog, name = "post-list"),
    path('post/<int:pk>/', post, name = "post-detail"),
]

if settings.DEBUG:
    urlpatterns+=static(settings.STATIC_URL,document_root=settings.STATIC_ROOT)
    urlpatterns+=static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
    