from django.urls import path, include

urlpatterns = [
    path('google-sheets/', SheetsListView.as_view()),
]
