from django.contrib import admin
from django.urls import path

from selfstudy.apps import SelfstudyConfig

app_name = SelfstudyConfig.name

urlpatterns = [
    # path('admin/', admin.site.urls),
]
