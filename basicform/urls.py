from django.urls import path
from basicform import views

urlpatterns=[
    path('',views.form_name_view)
]