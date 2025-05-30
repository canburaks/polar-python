"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from .discountduration import DiscountDuration
from .discounttype import DiscountType
from polar_sdk.types import BaseModel, Nullable, UNSET_SENTINEL
from pydantic import model_serializer
from typing_extensions import TypedDict


class CheckoutDiscountFixedRepeatDurationTypedDict(TypedDict):
    r"""Schema for a fixed amount discount that is applied on every invoice
    for a certain number of months.
    """

    duration: DiscountDuration
    duration_in_months: int
    type: DiscountType
    amount: int
    currency: str
    id: str
    r"""The ID of the object."""
    name: str
    code: Nullable[str]


class CheckoutDiscountFixedRepeatDuration(BaseModel):
    r"""Schema for a fixed amount discount that is applied on every invoice
    for a certain number of months.
    """

    duration: DiscountDuration

    duration_in_months: int

    type: DiscountType

    amount: int

    currency: str

    id: str
    r"""The ID of the object."""

    name: str

    code: Nullable[str]

    @model_serializer(mode="wrap")
    def serialize_model(self, handler):
        optional_fields = []
        nullable_fields = ["code"]
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
