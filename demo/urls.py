from django.urls import URLPattern, path
from . import views

urlpatterns=[
    path('',views.index,name='index'),
    path('fraud',views.fraud,name='fraud'),
    path('learn',views.learn,name='learn'),
    path('vote',views.vote,name='vote'),
]