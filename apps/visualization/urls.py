from django.urls import path
from . import views
from .constants import TOP10_PIE_CHART, APP_NAME

app_name = APP_NAME
urlpatterns = [
    path('top10/', views.top10_pie_chart, name=TOP10_PIE_CHART),
]
