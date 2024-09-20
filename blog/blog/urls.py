from django.urls import re_path, include
from django.contrib import admin

# Specifies the path to the given forces 

urlpatterns = [
    re_path(r'^admin/', admin.site.urls),
    re_path(r'^', include('blog_app.urls')),
    re_path(r'^register/', include('blog_app.urls')),
    re_path(r'^login/', include('blog_app.urls')),
    re_path(r'^register_/', include('blog_app.urls')),
    re_path(r'^pregister/', include('blog_app.urls')),
    re_path(r'^uregister/', include('blog_app.urls')),
    re_path(r'^nlogin/', include('blog_app.urls')),
    re_path(r'^nnlogin/', include('blog_app.urls')),
    re_path(r'^topics/', include('blog_app.urls')),
]
