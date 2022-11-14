from django.urls import path,include
from . import views

urlpatterns = [
    path('a/',views.a),
    path('contact/<int:no>/>',views.contact)
]