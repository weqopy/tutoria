from snippets import views
from django.urls import path, re_path, include
from rest_framework.urlpatterns import format_suffix_patterns

# TODO: 因添加了 users/ 路径，暂时使用 re_path
urlpatterns = [
    re_path(r"^$", views.api_root),
    re_path(r"^snippets/$", views.SnippetList.as_view(), name="snippet-list"),
    re_path(
        r"^snippets/(?P<pk>[0-9]+)/$",
        views.SnippetDetail.as_view(),
        name="snippet-detail",
    ),
    re_path(
        r"^snippets/(?P<pk>[0-9]+)/highlight/$",
        views.SnippetHighlight.as_view(),
        name="snippet-highlight",
    ),
    re_path(r"^users/$", views.UserList.as_view(), name="user-list"),
    re_path(r"^users/(?P<pk>[0-9]+)/$", views.UserDetail.as_view(), name="user-detail"),
]
urlpatterns += [
    re_path(r"^api-auth/", include("rest_framework.urls", namespace="rest_framework"))
]
urlpatterns = format_suffix_patterns(urlpatterns)
