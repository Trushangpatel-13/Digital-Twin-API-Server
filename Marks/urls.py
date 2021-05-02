from django.urls import path
from django.conf.urls import url
from Marks import views
from .views import index
urlpatterns = [
    path('api/v1',views.MarksApiView.as_view()),
    url(r'^$',views.index,name='index'),
]
