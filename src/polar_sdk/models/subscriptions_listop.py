"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from .listresource_subscription_ import (
    ListResourceSubscription,
    ListResourceSubscriptionTypedDict,
)
from .subscriptionsortproperty import SubscriptionSortProperty
from polar_sdk.types import BaseModel, Nullable, OptionalNullable, UNSET, UNSET_SENTINEL
from polar_sdk.utils import FieldMetadata, QueryParamMetadata
from pydantic import model_serializer
from typing import Callable, List, Optional, Union
from typing_extensions import Annotated, NotRequired, TypeAliasType, TypedDict


OrganizationIDFilterTypedDict = TypeAliasType(
    "OrganizationIDFilterTypedDict", Union[str, List[str]]
)
r"""Filter by organization ID."""


OrganizationIDFilter = TypeAliasType("OrganizationIDFilter", Union[str, List[str]])
r"""Filter by organization ID."""


ProductIDFilterTypedDict = TypeAliasType(
    "ProductIDFilterTypedDict", Union[str, List[str]]
)
r"""Filter by product ID."""


ProductIDFilter = TypeAliasType("ProductIDFilter", Union[str, List[str]])
r"""Filter by product ID."""


CustomerIDFilterTypedDict = TypeAliasType(
    "CustomerIDFilterTypedDict", Union[str, List[str]]
)
r"""Filter by customer ID."""


CustomerIDFilter = TypeAliasType("CustomerIDFilter", Union[str, List[str]])
r"""Filter by customer ID."""


DiscountIDFilterTypedDict = TypeAliasType(
    "DiscountIDFilterTypedDict", Union[str, List[str]]
)
r"""Filter by discount ID."""


DiscountIDFilter = TypeAliasType("DiscountIDFilter", Union[str, List[str]])
r"""Filter by discount ID."""


class SubscriptionsListRequestTypedDict(TypedDict):
    organization_id: NotRequired[Nullable[OrganizationIDFilterTypedDict]]
    r"""Filter by organization ID."""
    product_id: NotRequired[Nullable[ProductIDFilterTypedDict]]
    r"""Filter by product ID."""
    customer_id: NotRequired[Nullable[CustomerIDFilterTypedDict]]
    r"""Filter by customer ID."""
    discount_id: NotRequired[Nullable[DiscountIDFilterTypedDict]]
    r"""Filter by discount ID."""
    active: NotRequired[Nullable[bool]]
    r"""Filter by active or inactive subscription."""
    page: NotRequired[int]
    r"""Page number, defaults to 1."""
    limit: NotRequired[int]
    r"""Size of a page, defaults to 10. Maximum is 100."""
    sorting: NotRequired[Nullable[List[SubscriptionSortProperty]]]
    r"""Sorting criterion. Several criteria can be used simultaneously and will be applied in order. Add a minus sign `-` before the criteria name to sort by descending order."""


class SubscriptionsListRequest(BaseModel):
    organization_id: Annotated[
        OptionalNullable[OrganizationIDFilter],
        FieldMetadata(query=QueryParamMetadata(style="form", explode=True)),
    ] = UNSET
    r"""Filter by organization ID."""

    product_id: Annotated[
        OptionalNullable[ProductIDFilter],
        FieldMetadata(query=QueryParamMetadata(style="form", explode=True)),
    ] = UNSET
    r"""Filter by product ID."""

    customer_id: Annotated[
        OptionalNullable[CustomerIDFilter],
        FieldMetadata(query=QueryParamMetadata(style="form", explode=True)),
    ] = UNSET
    r"""Filter by customer ID."""

    discount_id: Annotated[
        OptionalNullable[DiscountIDFilter],
        FieldMetadata(query=QueryParamMetadata(style="form", explode=True)),
    ] = UNSET
    r"""Filter by discount ID."""

    active: Annotated[
        OptionalNullable[bool],
        FieldMetadata(query=QueryParamMetadata(style="form", explode=True)),
    ] = UNSET
    r"""Filter by active or inactive subscription."""

    page: Annotated[
        Optional[int],
        FieldMetadata(query=QueryParamMetadata(style="form", explode=True)),
    ] = 1
    r"""Page number, defaults to 1."""

    limit: Annotated[
        Optional[int],
        FieldMetadata(query=QueryParamMetadata(style="form", explode=True)),
    ] = 10
    r"""Size of a page, defaults to 10. Maximum is 100."""

    sorting: Annotated[
        OptionalNullable[List[SubscriptionSortProperty]],
        FieldMetadata(query=QueryParamMetadata(style="form", explode=True)),
    ] = UNSET
    r"""Sorting criterion. Several criteria can be used simultaneously and will be applied in order. Add a minus sign `-` before the criteria name to sort by descending order."""

    @model_serializer(mode="wrap")
    def serialize_model(self, handler):
        optional_fields = [
            "organization_id",
            "product_id",
            "customer_id",
            "discount_id",
            "active",
            "page",
            "limit",
            "sorting",
        ]
        nullable_fields = [
            "organization_id",
            "product_id",
            "customer_id",
            "discount_id",
            "active",
            "sorting",
        ]
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


class SubscriptionsListResponseTypedDict(TypedDict):
    result: ListResourceSubscriptionTypedDict


class SubscriptionsListResponse(BaseModel):
    next: Callable[[], Optional[SubscriptionsListResponse]]

    result: ListResourceSubscription
