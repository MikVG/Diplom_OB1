from django.urls import path

from selfstudy.apps import SelfstudyConfig
from selfstudy.views import TestAPIView, TestMaterialListAPIView, TestMaterialRetrieveAPIView

app_name = SelfstudyConfig.name

urlpatterns = [
    path('', TestMaterialListAPIView.as_view(), name='test_list'),
    path('<int:pk>/', TestMaterialRetrieveAPIView.as_view(), name='test_detail'),
    path('test/', TestAPIView.as_view(), name='test'),
]
