from django.contrib import admin
from django.urls import path, include
from dramas import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns=[
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('blog/', include('blog.urls')),
    path('ranking/',include('ranking.urls')),
    path('accounts/', include('accounts.urls', namespace='accounts')),
    path("authaccounts/", include('allauth.urls')),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
