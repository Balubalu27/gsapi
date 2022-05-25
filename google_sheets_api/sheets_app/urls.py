from django.urls import path
from sheets_app.views import DbUpdateView

urlpatterns = [
    path('', DbUpdateView.as_view()),
]
