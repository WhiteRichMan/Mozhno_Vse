from typing import Optional

from django.core.handlers.wsgi import WSGIRequest
from django.contrib import admin

from sweets.models import (
    Description,
    Title,
    ReleaseDate,

)


class ReleaseDateAdmin(admin.ModelAdmin):

    readonly_fields = (
        'published',
        'date',
    )


class DescriptionAdmin(admin.ModelAdmin):

    readonly_fields = ()


class TitleAdmin(admin.ModelAdmin):

    readonly_fields = ()


class SweetsAdmin(admin.ModelAdmin):

    readonly_fields = (
        'datetime_created',
        'datetime_updated',
        'datetime_deleted',
    )


admin.site.register(
    ReleaseDate, ReleaseDateAdmin
)
admin.site.register(
    Description, DescriptionAdmin
)
admin.site.register(
    Title, TitleAdmin
)
admin.site.register(
    Sweets, SweetsAdmin
)
