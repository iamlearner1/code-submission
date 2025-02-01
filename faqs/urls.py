from django.urls import path, include
from rest_framework.routers import DefaultRouter
from faqs import views
from .views import FAQViewSet

router = DefaultRouter()
router.register(r'faqs', FAQViewSet, basename='faqs')

urlpatterns = [
    path('api/', include(router.urls)),
     path('', views.index,name =  'index'),
]
