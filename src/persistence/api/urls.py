from django.urls import path

from .views import (
    RandomPolyPhraseView,
    ReadOtherDataView,
    WriteOtherDataView,
    WritePolyPhraseView,
)

app_name = "persistence"

urlpatterns = [
    path("other-data/read", ReadOtherDataView.as_view(), name="read"),
    path("other-data/write", WriteOtherDataView.as_view(), name="write"),
    path("poly-says", RandomPolyPhraseView.as_view(), name="poly-says"),
    path("poly-hears", WritePolyPhraseView.as_view(), name="poly-hears"),
]
