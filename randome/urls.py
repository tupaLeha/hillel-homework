from django.urls import path
from randome.views import index

urlpatterns = [
    path('', index),

]