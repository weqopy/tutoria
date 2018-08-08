from snippets import views
from django.urls import path, re_path, include
from rest_framework.urlpatterns import format_suffix_patterns
from rest_framework import renderers

snippet_list = views.SnippetViewSet.as_view({"get": "list", "post": "create"})

snippet_detail = views.SnippetViewSet.as_view(
    {
        "get": "retrieve",
        "post": "update",
        "patch": "partial_update",
        "delete": "destroy",
    }
)

snippet_highlight = views.SnippetViewSet.as_view(
    {"get": "highlight"}, render_classes=[renderers.StaticHTMLRenderer]
)

user_list = views.UserViewSet.as_view({"get": "list"})
user_detail = views.UserViewSet.as_view({"get": "retrieve"})


# TODO: 因添加了 users/ 路径，暂时使用 re_path
urlpatterns = [
    re_path(r"^$", views.api_root),
    re_path(r"^snippets/$", snippet_list, name="snippet-list"),
    re_path(r"^snippets/(?P<pk>[0-9]+)/$", snippet_detail, name="snippet-detail"),
    re_path(
        r"^snippets/(?P<pk>[0-9]+)/highlight/$",
        snippet_highlight,
        name="snippet-highlight",
    ),
    re_path(r"^users/$", user_list, name="user-list"),
    re_path(r"^users/(?P<pk>[0-9]+)/$", user_detail, name="user-detail"),
]
urlpatterns += [
    re_path(r"^api-auth/", include("rest_framework.urls", namespace="rest_framework"))
]
urlpatterns = format_suffix_patterns(urlpatterns)
