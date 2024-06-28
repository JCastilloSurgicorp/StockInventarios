from django.urls import path
from . import views as v

urlpatterns = [
    path("", v.index, name="index"),
    path("<int:question_id>/", v.detail, name="detail"),
    path("<int:question_id>/results/", v.results, name="results"),
    path("<int:question_id>/vote/", v.vote, name="vote"),
]