from django.contrib import admin
from django.urls import path, include
from profiles import urls as profile_urls 
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('auth/', include('accounts.urls')),  # URLs for user management
    path('api/profile/', include(profile_urls)),  # URLs for user profiles
    path('api/mgi/', include('mgicandles.urls')),  # Include mgicandles URLs
    path('api/tradedetails/', include('tradedetails.urls')),  # Include TradeDetails URLs
    path('api/candleimages/', include('candleimages.urls')),  # Include CandleImages URLs
    path('api/tradingindicators/', include('tradingindicators.urls')),  # Include TradingIndicators URLs
]


urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
