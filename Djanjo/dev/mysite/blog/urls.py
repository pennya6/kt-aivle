from django.urls import path,include
from . import views

urlpatterns = [
    path('test1/',views.test1),
    path('test2/<no>/',views.test2),
    path('test3/<year>/<month>/<day>/',views.test3),
    path('',views.list),
    path('<int:id>/',views.detail),
]