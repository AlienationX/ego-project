"""
URL configuration for server project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView, SpectacularRedocView

urlpatterns = [
    path('admin/', admin.site.urls),

    path('pokemon_library/', include('pokemon_library.urls')),
    path('pokemon_wallpaper/', include('pokemon_wallpaper.urls')),
    path('wallpaper/', include('wallpaper.urls')),

    # # drf-spectacular，只能在该处配置，不推荐使用
    # path('wallpaper/spe-schema/', SpectacularAPIView.as_view(), name='wallpaper-spe-schema'),
    # # 为 Swagger UI 添加路径
    # path('wallpaper/spe-swagger/', SpectacularSwaggerView.as_view(url_name='wallpaper-spe-schema'), name='spe-swagger'),
    # path('wallpaper/spe-redoc/', SpectacularRedocView.as_view(url_name='wallpaper-spe-schema'), name='redoc'),
]
