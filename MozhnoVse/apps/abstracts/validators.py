import pytz
from typing import Optional
from datetime import datetime

from rest_framework.status import (
    HTTP_500_INTERNAL_SERVER_ERROR,
    HTTP_404_NOT_FOUND,
    HTTP_403_FORBIDDEN,
    HTTP_400_BAD_REQUEST,
)
from rest_framework.exceptions import APIException

from django.core.exceptions import ValidationError
from django.utils.encoding import force_str


class APIValidator(APIException):

    status_code: Optional[str] = None

    def __init__(
        self, detail: dict, field: str, status_code: str
    ) -> None:
        """Initialize."""

        if status_code is not None:
            if status_code == '500':
                self.status_code = HTTP_500_INTERNAL_SERVER_ERROR
            elif status_code == '404':
                self.status_code = HTTP_404_NOT_FOUND
            elif status_code == '403':
                self.status_code = HTTP_403_FORBIDDEN
            elif status_code == '400':
                self.status_code = HTTP_400_BAD_REQUEST
            else:
                raise ValidationError(
                    'Status code is unknown'
                )
        if detail is not None:
            self.detail = {
                field: force_str(detail)
            }
        else:
            self.detail = {
                'error': force_str('Server is down')
            }


