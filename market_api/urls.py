# market_api/urls.py
from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from products.views import ProductViewSet, OrderViewSet
from django.conf import settings
from django.conf.urls.static import static
from django.http import HttpResponse   # ✅ ضروري تستورد هادي

# Router ديال الـ API
router = DefaultRouter()
router.register(r'products', ProductViewSet, basename="product")
router.register(r'orders', OrderViewSet, basename="order")

# View باش root / يرجع رسالة بسيطة
def home(request):
    return HttpResponse("مرحباً بك في متجر آتاي! 🚀 تيكرو /api/ باش تشوف الـ API.")

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
    path('', home),  # root route
]

# باش تقدر تشوف الصور فـ MEDIA فـ DEBUG mode
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
