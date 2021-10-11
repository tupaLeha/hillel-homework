from django.urls import path

from about.views import whoami, source_code

urlpatterns = [
    path('whoami', whoami),
    path('source_code', source_code),
]
