from django.contrib import admin
from django.urls import path, include
from accounts.views import login

urlpatterns = [
    path('admin/', admin.site.urls),
    path('admin/login/', login),
    path('accounts/', include('accounts.urls')),
    path('test/', include('test1.urls')),
    path('project/', include('project.urls')),

]
