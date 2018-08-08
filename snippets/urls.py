from snippets import views
from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
    path("", views.SnippetList.as_view()),
    # 后加 /， 否则被识别为 snippets/ <int:pk>
    path("<int:pk>/", views.SnippetDetail.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)
