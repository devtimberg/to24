# encoding: utf-8

from __future__ import unicode_literals

from django.conf.urls import url, include

from django.contrib import admin
from django.conf import settings

admin.autodiscover()


urlpatterns = [
    url(r'^', include('transport_cards.urls')),
    url(r'^admin/', include(admin.site.urls)),
]


# Это нужно для раздачи медиа и подключеня дебаг-панели
if settings.DEBUG:
    from django.conf.urls.static import static
    from django.contrib.staticfiles.urls import staticfiles_urlpatterns
    import debug_toolbar

    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += staticfiles_urlpatterns()

    urlpatterns += [url(r'^__debug__/', include(debug_toolbar.urls)), ]
