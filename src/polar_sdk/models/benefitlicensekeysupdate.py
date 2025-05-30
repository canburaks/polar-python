"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from .benefitlicensekeyscreateproperties import (
    BenefitLicenseKeysCreateProperties,
    BenefitLicenseKeysCreatePropertiesTypedDict,
)
from polar_sdk.types import BaseModel, Nullable, OptionalNullable, UNSET, UNSET_SENTINEL
from polar_sdk.utils import validate_const
import pydantic
from pydantic import model_serializer
from pydantic.functional_validators import AfterValidator
from typing import Dict, Literal, Optional, Union
from typing_extensions import Annotated, NotRequired, TypeAliasType, TypedDict


BenefitLicenseKeysUpdateMetadataTypedDict = TypeAliasType(
    "BenefitLicenseKeysUpdateMetadataTypedDict", Union[str, int, float, bool]
)


BenefitLicenseKeysUpdateMetadata = TypeAliasType(
    "BenefitLicenseKeysUpdateMetadata", Union[str, int, float, bool]
)


class BenefitLicenseKeysUpdateTypedDict(TypedDict):
    metadata: NotRequired[Dict[str, BenefitLicenseKeysUpdateMetadataTypedDict]]
    r"""Key-value object allowing you to store additional information.

    The key must be a string with a maximum length of **40 characters**.
    The value must be either:

    * A string with a maximum length of **500 characters**
    * An integer
    * A floating-point number
    * A boolean

    You can store up to **50 key-value pairs**.
    """
    description: NotRequired[Nullable[str]]
    r"""The description of the benefit. Will be displayed on products having this benefit."""
    type: Literal["license_keys"]
    properties: NotRequired[Nullable[BenefitLicenseKeysCreatePropertiesTypedDict]]


class BenefitLicenseKeysUpdate(BaseModel):
    metadata: Optional[Dict[str, BenefitLicenseKeysUpdateMetadata]] = None
    r"""Key-value object allowing you to store additional information.

    The key must be a string with a maximum length of **40 characters**.
    The value must be either:

    * A string with a maximum length of **500 characters**
    * An integer
    * A floating-point number
    * A boolean

    You can store up to **50 key-value pairs**.
    """

    description: OptionalNullable[str] = UNSET
    r"""The description of the benefit. Will be displayed on products having this benefit."""

    TYPE: Annotated[
        Annotated[
            Literal["license_keys"], AfterValidator(validate_const("license_keys"))
        ],
        pydantic.Field(alias="type"),
    ] = "license_keys"

    properties: OptionalNullable[BenefitLicenseKeysCreateProperties] = UNSET

    @model_serializer(mode="wrap")
    def serialize_model(self, handler):
        optional_fields = ["metadata", "description", "properties"]
        nullable_fields = ["description", "properties"]
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
