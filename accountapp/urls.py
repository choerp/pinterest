from django.urls import path
from accountapp.views import hello_world, AccountCreateView

app_name = "accountapp"

urlpatterns = [
    path('hello_world/', hello_world, name='hello_world'),
    # parameter1 : url주소. // parameter2 : views의 함수 // parameter3 : name??
    path('create/', AccountCreateView.as_view(), name='create')
]
