

from django.contrib import admin
from django.urls import path, include

from posts.views import TesView

urlpatterns = [
    path('admin/', admin.site.urls),
    #path('', include('posts.urls')),
    path('api-auth/', include('rest_frame.urls')),
    path('', TesView.as_view(), name='test' )
]
