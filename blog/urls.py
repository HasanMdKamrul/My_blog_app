from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path,include
from posts.views import blog,post


urlpatterns = [
    path('admin/', admin.site.urls),
    path('posts/', include("posts.urls", namespace="posts")),
    path('blog/', blog),
    #path('post/', post),
]

if settings.DEBUG:
    urlpatterns+=static(settings.STATIC_URL,document_root=settings.STATIC_ROOT)
    urlpatterns+=static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
    