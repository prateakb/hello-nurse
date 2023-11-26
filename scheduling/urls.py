from django.urls import path
from . import views

urlpatterns = [
    path('', views.list_slots, name='slots_list'),  # The root path for the 'scheduling' app
    path('slots/', views.list_slots, name='slots_list'),
    path('slots/<int:slot_id>/sign_up/', views.sign_up_for_slot, name='slot_sign_up'),
]
