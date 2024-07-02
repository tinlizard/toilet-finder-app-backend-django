from django.urls import path
from . import views

urlpatterns = [
    path("toilets/",views.toilets_list),
    path("reviews/",views.reviews_list),
    path("users/",views.user_list)
]