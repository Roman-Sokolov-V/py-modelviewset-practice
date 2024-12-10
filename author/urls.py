from django.urls import path, include

from rest_framework import routers

from author.views import AuthorViewSet


urlpatterns = [
    path(
        "authors/",
        AuthorViewSet.as_view({"get": "list", "post": "create"}),
        name="manage"
    ),
    path(
        "authors/<int:pk>/",
        AuthorViewSet.as_view(
            {
                "get": "retrieve",
                "put": "update",
                "patch": "partial_update",
                "delete": "destroy"
            }
        ),
        name="manage-detail"

    )
]

app_name = "author"
