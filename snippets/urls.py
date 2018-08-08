from snippets import views
from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
    path("", views.snippet_list),
    # 后加 /， 否则被识别为 snippets/ <int:pk>
    path("<int:pk>/", views.snippet_detail),
]

urlpatterns = format_suffix_patterns(urlpatterns)
