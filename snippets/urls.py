from snippets import views
from django.urls import path

urlpatterns = [
    path("", views.snippet_list),
    # 后加 /， 否则被识别为 snippets/ <int:pk>
    path("<int:pk>/", views.snippet_detail),
]
