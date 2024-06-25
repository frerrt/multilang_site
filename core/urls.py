from django.contrib import admin
from django.urls import path, include
from django.conf.urls.i18n import i18n_patterns
from django.utils.translation import gettext_lazy as _

urlpatterns = [
    path(_('admin/'), admin.site.urls),  # Localized admin URL
     path('chat/', include('chatbot.urls')),
]

# Internationalized URL patterns
urlpatterns += i18n_patterns(
    path('', include('main.urls', namespace='main')),
)
# Add any additional non-i18n patterns outside i18n_patterns if necessary
