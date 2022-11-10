from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from cart.views import add_to_cart

urlpatterns = [
    path('admin/', admin.site.urls),
    path('add_to_cart/<int:product_id>/', add_to_cart, name="add_to_cart"),
    path('', include('catlog.urls'))
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
