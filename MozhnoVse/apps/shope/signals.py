from django.db.models.signals import (
    pre_save,
    post_save,
    pre_delete,
    post_delete,
)
from django.dispatch import receiver
from django.db.models.base import ModelBase

from abstracts.utils import send_email
from sweets.models import Anime


@receiver(
    post_save,
    sender=Anime
)
def post_save_sweets(
    sender: ModelBase,
    instance: Sweets,
    created: bool,
    **kwargs: dict
) -> None:
    """Signal post-save Sweets."""

    # Sending Email to User linked to Anime as uploader
    #
    send_email(
        'DJANGO_SUBJECT',
        'DJANGO_TEXT',
        'rrrrror55@gmail.com'
    )


@receiver(
    pre_save,
    sender=Sweets
)
def pre_save_sweets(
    sender: ModelBase,
    instance: Sweets,
    **kwargs: dict
) -> None:
    """Signal pre-save Sweets."""
    pass

    # instance.save()


@receiver(
    post_delete,
    sender=Sweets
)
def post_delete_sweets(
    sender: ModelBase,
    instance: Sweets,
    **kwargs: dict
) -> None:
    """Signal post-delete Sweets."""

    instance.delete()


@receiver(
    pre_delete,
    sender=Sweets
)
def pre_delete_sweet(
    sender: ModelBase,
    instance: Sweets,
    **kwargs: dict
) -> None:
    """Signal pre-delete Sweet."""

    instance.delete()