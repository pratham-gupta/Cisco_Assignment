from django.urls import path
from router_api.views import Router_View


urlpatterns = [

    path("router",Router_View.as_view()),
]