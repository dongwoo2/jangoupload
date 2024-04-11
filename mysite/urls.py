"""
URL configuration for mysite project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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

urlpatterns = [
    path('admin/', admin.site.urls),
    path('ex/', include('ex_upload.urls')),
]

from django.conf import settings # 장고의 세팅 정보를 가져오기 위해 임폴트
from django.conf.urls.static import static # 스태틱 경로에 해당하는 거기 때문에 임폴트 이미지 요청자체는 스태틱 정적파일을 요청하는 것과 개념이 똑같다

urlpatterns += static(
                    settings.MEDIA_URL,
                    document_root=settings.MEDIA_ROOT  
                    )