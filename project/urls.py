from django.conf import settings
from django.conf.urls import include, url
from django.conf.urls.static import static
from django.contrib import admin
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.views.generic import TemplateView

import debug_toolbar

from main.views import (
    bad_request, page_not_found, permission_denied, server_error,
    simulated_error,
)
from utils.aldryn_categories import *

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^hijack/', include('hijack.urls')),
    url(r'^simulated-error/', simulated_error),
]

if settings.DEBUG:
    urlpatterns += staticfiles_urlpatterns()
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += [
        url(r'^__debug__/', include(debug_toolbar.urls)),
        url(r'^error400/$', bad_request),
        url(r'^error403/$', permission_denied),
        url(r'^error404/$', page_not_found),
        url(r'^error500/$', server_error),
    ]

urlpatterns += [
    url(r'^', include('cms.urls')),
]

admin.site.site_header = settings.PROJECT_DISPLAY_NAME

# pylint: disable=invalid-name
handler400 = 'main.views.bad_request'
handler403 = 'main.views.permission_denied'
handler404 = 'main.views.page_not_found'
handler500 = 'main.views.server_error'
