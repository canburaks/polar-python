"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from datetime import datetime
from polar_sdk.types import BaseModel, Nullable, OptionalNullable, UNSET, UNSET_SENTINEL
from pydantic import model_serializer
from typing import Dict, Optional, Union
from typing_extensions import NotRequired, TypeAliasType, TypedDict


EventCreateExternalCustomerMetadataTypedDict = TypeAliasType(
    "EventCreateExternalCustomerMetadataTypedDict", Union[str, int, float, bool]
)


EventCreateExternalCustomerMetadata = TypeAliasType(
    "EventCreateExternalCustomerMetadata", Union[str, int, float, bool]
)


class EventCreateExternalCustomerTypedDict(TypedDict):
    name: str
    r"""The name of the event."""
    external_customer_id: str
    r"""ID of the customer in your system associated with the event."""
    metadata: NotRequired[Dict[str, EventCreateExternalCustomerMetadataTypedDict]]
    r"""Key-value object allowing you to store additional information.

    The key must be a string with a maximum length of **40 characters**.
    The value must be either:

    * A string with a maximum length of **500 characters**
    * An integer
    * A floating-point number
    * A boolean

    You can store up to **50 key-value pairs**.
    """
    timestamp: NotRequired[datetime]
    r"""The timestamp of the event."""
    organization_id: NotRequired[Nullable[str]]
    r"""The ID of the organization owning the event. **Required unless you use an organization token.**"""


class EventCreateExternalCustomer(BaseModel):
    name: str
    r"""The name of the event."""

    external_customer_id: str
    r"""ID of the customer in your system associated with the event."""

    metadata: Optional[Dict[str, EventCreateExternalCustomerMetadata]] = None
    r"""Key-value object allowing you to store additional information.

    The key must be a string with a maximum length of **40 characters**.
    The value must be either:

    * A string with a maximum length of **500 characters**
    * An integer
    * A floating-point number
    * A boolean

    You can store up to **50 key-value pairs**.
    """

    timestamp: Optional[datetime] = None
    r"""The timestamp of the event."""

    organization_id: OptionalNullable[str] = UNSET
    r"""The ID of the organization owning the event. **Required unless you use an organization token.**"""

    @model_serializer(mode="wrap")
    def serialize_model(self, handler):
        optional_fields = ["metadata", "timestamp", "organization_id"]
        nullable_fields = ["organization_id"]
        null_default_fields = []

        serialized = handler(self)

        m = {}

        for n, f in type(self).model_fields.items():
            k = f.alias or n
            val = serialized.get(k)
            serialized.pop(k, None)

            optional_nullable = k in optional_fields and k in nullable_fields
            is_set = (
                self.__pydantic_fields_set__.intersection({n})
                or k in null_default_fields
            )  # pylint: disable=no-member

            if val is not None and val != UNSET_SENTINEL:
                m[k] = val
            elif val != UNSET_SENTINEL and (
                not k in optional_fields or (optional_nullable and is_set)
            ):
                m[k] = val

        return m
