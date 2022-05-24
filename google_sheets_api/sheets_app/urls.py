from django.urls import path, include

from sheets_app.views import DbUpdateView

urlpatterns = [
    path('', DbUpdateView.as_view()),
]
