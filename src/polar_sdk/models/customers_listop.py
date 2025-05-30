"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from .customersortproperty import CustomerSortProperty
from .eventsortproperty import EventSortProperty
from .eventsource import EventSource
from .listresource_customer_ import ListResourceCustomer, ListResourceCustomerTypedDict
from .listresource_event_ import ListResourceEvent, ListResourceEventTypedDict
from .listresource_meter_ import ListResourceMeter, ListResourceMeterTypedDict
from .metersortproperty import MeterSortProperty
from datetime import datetime
from polar_sdk.types import BaseModel, Nullable, OptionalNullable, UNSET, UNSET_SENTINEL
from polar_sdk.utils import FieldMetadata, QueryParamMetadata
import pydantic
from pydantic import model_serializer
from typing import Callable, Dict, List, Optional, Union
from typing_extensions import Annotated, NotRequired, TypeAliasType, TypedDict


CustomersListQueryParamOrganizationIDFilterTypedDict = TypeAliasType(
    "CustomersListQueryParamOrganizationIDFilterTypedDict", Union[str, List[str]]
)
r"""Filter by organization ID."""


CustomersListQueryParamOrganizationIDFilter = TypeAliasType(
    "CustomersListQueryParamOrganizationIDFilter", Union[str, List[str]]
)
r"""Filter by organization ID."""


MetadataQueryTypedDict = TypeAliasType(
    "MetadataQueryTypedDict", Union[str, int, bool, List[str], List[int], List[bool]]
)


MetadataQuery = TypeAliasType(
    "MetadataQuery", Union[str, int, bool, List[str], List[int], List[bool]]
)


class CustomersListRequestTypedDict(TypedDict):
    organization_id: NotRequired[
        Nullable[CustomersListQueryParamOrganizationIDFilterTypedDict]
    ]
    r"""Filter by organization ID."""
    email: NotRequired[Nullable[str]]
    r"""Filter by exact email."""
    query: NotRequired[Nullable[str]]
    r"""Filter by name or email."""
    page: NotRequired[int]
    r"""Page number, defaults to 1."""
    limit: NotRequired[int]
    r"""Size of a page, defaults to 10. Maximum is 100."""
    sorting: NotRequired[Nullable[List[CustomerSortProperty]]]
    r"""Sorting criterion. Several criteria can be used simultaneously and will be applied in order. Add a minus sign `-` before the criteria name to sort by descending order."""
    metadata: NotRequired[Nullable[Dict[str, MetadataQueryTypedDict]]]
    r"""Filter by metadata key-value pairs. It uses the `deepObject` style, e.g. `?metadata[key]=value`."""


class CustomersListRequest(BaseModel):
    organization_id: Annotated[
        OptionalNullable[CustomersListQueryParamOrganizationIDFilter],
        FieldMetadata(query=QueryParamMetadata(style="form", explode=True)),
    ] = UNSET
    r"""Filter by organization ID."""

    email: Annotated[
        OptionalNullable[str],
        FieldMetadata(query=QueryParamMetadata(style="form", explode=True)),
    ] = UNSET
    r"""Filter by exact email."""

    query: Annotated[
        OptionalNullable[str],
        FieldMetadata(query=QueryParamMetadata(style="form", explode=True)),
    ] = UNSET
    r"""Filter by name or email."""

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
        OptionalNullable[List[CustomerSortProperty]],
        FieldMetadata(query=QueryParamMetadata(style="form", explode=True)),
    ] = UNSET
    r"""Sorting criterion. Several criteria can be used simultaneously and will be applied in order. Add a minus sign `-` before the criteria name to sort by descending order."""

    metadata: Annotated[
        OptionalNullable[Dict[str, MetadataQuery]],
        FieldMetadata(query=QueryParamMetadata(style="deepObject", explode=True)),
    ] = UNSET
    r"""Filter by metadata key-value pairs. It uses the `deepObject` style, e.g. `?metadata[key]=value`."""

    @model_serializer(mode="wrap")
    def serialize_model(self, handler):
        optional_fields = [
            "organization_id",
            "email",
            "query",
            "page",
            "limit",
            "sorting",
            "metadata",
        ]
        nullable_fields = ["organization_id", "email", "query", "sorting", "metadata"]
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


class CustomersListResponseTypedDict(TypedDict):
    result: ListResourceCustomerTypedDict


class CustomersListResponse(BaseModel):
    next: Callable[[], Optional[CustomersListResponse]]

    result: ListResourceCustomer


EventsListQueryParamOrganizationIDFilterTypedDict = TypeAliasType(
    "EventsListQueryParamOrganizationIDFilterTypedDict", Union[str, List[str]]
)
r"""Filter by organization ID."""


EventsListQueryParamOrganizationIDFilter = TypeAliasType(
    "EventsListQueryParamOrganizationIDFilter", Union[str, List[str]]
)
r"""Filter by organization ID."""


EventsListQueryParamCustomerIDFilterTypedDict = TypeAliasType(
    "EventsListQueryParamCustomerIDFilterTypedDict", Union[str, List[str]]
)
r"""Filter by customer ID."""


EventsListQueryParamCustomerIDFilter = TypeAliasType(
    "EventsListQueryParamCustomerIDFilter", Union[str, List[str]]
)
r"""Filter by customer ID."""


ExternalCustomerIDFilterTypedDict = TypeAliasType(
    "ExternalCustomerIDFilterTypedDict", Union[str, List[str]]
)
r"""Filter by external customer ID."""


ExternalCustomerIDFilter = TypeAliasType(
    "ExternalCustomerIDFilter", Union[str, List[str]]
)
r"""Filter by external customer ID."""


NameFilterTypedDict = TypeAliasType("NameFilterTypedDict", Union[str, List[str]])
r"""Filter by event name."""


NameFilter = TypeAliasType("NameFilter", Union[str, List[str]])
r"""Filter by event name."""


SourceFilterTypedDict = TypeAliasType(
    "SourceFilterTypedDict", Union[EventSource, List[EventSource]]
)
r"""Filter by event source."""


SourceFilter = TypeAliasType("SourceFilter", Union[EventSource, List[EventSource]])
r"""Filter by event source."""


class EventsListRequestTypedDict(TypedDict):
    filter_: NotRequired[Nullable[str]]
    r"""Filter events following filter clauses. JSON string following the same schema a meter filter clause."""
    start_timestamp: NotRequired[Nullable[datetime]]
    r"""Filter events after this timestamp."""
    end_timestamp: NotRequired[Nullable[datetime]]
    r"""Filter events before this timestamp."""
    organization_id: NotRequired[
        Nullable[EventsListQueryParamOrganizationIDFilterTypedDict]
    ]
    r"""Filter by organization ID."""
    customer_id: NotRequired[Nullable[EventsListQueryParamCustomerIDFilterTypedDict]]
    r"""Filter by customer ID."""
    external_customer_id: NotRequired[Nullable[ExternalCustomerIDFilterTypedDict]]
    r"""Filter by external customer ID."""
    meter_id: NotRequired[Nullable[str]]
    r"""Filter by a meter filter clause."""
    name: NotRequired[Nullable[NameFilterTypedDict]]
    r"""Filter by event name."""
    source: NotRequired[Nullable[SourceFilterTypedDict]]
    r"""Filter by event source."""
    page: NotRequired[int]
    r"""Page number, defaults to 1."""
    limit: NotRequired[int]
    r"""Size of a page, defaults to 10. Maximum is 100."""
    sorting: NotRequired[Nullable[List[EventSortProperty]]]
    r"""Sorting criterion. Several criteria can be used simultaneously and will be applied in order. Add a minus sign `-` before the criteria name to sort by descending order."""
    metadata: NotRequired[Nullable[Dict[str, MetadataQueryTypedDict]]]
    r"""Filter by metadata key-value pairs. It uses the `deepObject` style, e.g. `?metadata[key]=value`."""


class EventsListRequest(BaseModel):
    filter_: Annotated[
        OptionalNullable[str],
        pydantic.Field(alias="filter"),
        FieldMetadata(query=QueryParamMetadata(style="form", explode=True)),
    ] = UNSET
    r"""Filter events following filter clauses. JSON string following the same schema a meter filter clause."""

    start_timestamp: Annotated[
        OptionalNullable[datetime],
        FieldMetadata(query=QueryParamMetadata(style="form", explode=True)),
    ] = UNSET
    r"""Filter events after this timestamp."""

    end_timestamp: Annotated[
        OptionalNullable[datetime],
        FieldMetadata(query=QueryParamMetadata(style="form", explode=True)),
    ] = UNSET
    r"""Filter events before this timestamp."""

    organization_id: Annotated[
        OptionalNullable[EventsListQueryParamOrganizationIDFilter],
        FieldMetadata(query=QueryParamMetadata(style="form", explode=True)),
    ] = UNSET
    r"""Filter by organization ID."""

    customer_id: Annotated[
        OptionalNullable[EventsListQueryParamCustomerIDFilter],
        FieldMetadata(query=QueryParamMetadata(style="form", explode=True)),
    ] = UNSET
    r"""Filter by customer ID."""

    external_customer_id: Annotated[
        OptionalNullable[ExternalCustomerIDFilter],
        FieldMetadata(query=QueryParamMetadata(style="form", explode=True)),
    ] = UNSET
    r"""Filter by external customer ID."""

    meter_id: Annotated[
        OptionalNullable[str],
        FieldMetadata(query=QueryParamMetadata(style="form", explode=True)),
    ] = UNSET
    r"""Filter by a meter filter clause."""

    name: Annotated[
        OptionalNullable[NameFilter],
        FieldMetadata(query=QueryParamMetadata(style="form", explode=True)),
    ] = UNSET
    r"""Filter by event name."""

    source: Annotated[
        OptionalNullable[SourceFilter],
        FieldMetadata(query=QueryParamMetadata(style="form", explode=True)),
    ] = UNSET
    r"""Filter by event source."""

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
        OptionalNullable[List[EventSortProperty]],
        FieldMetadata(query=QueryParamMetadata(style="form", explode=True)),
    ] = UNSET
    r"""Sorting criterion. Several criteria can be used simultaneously and will be applied in order. Add a minus sign `-` before the criteria name to sort by descending order."""

    metadata: Annotated[
        OptionalNullable[Dict[str, MetadataQuery]],
        FieldMetadata(query=QueryParamMetadata(style="deepObject", explode=True)),
    ] = UNSET
    r"""Filter by metadata key-value pairs. It uses the `deepObject` style, e.g. `?metadata[key]=value`."""

    @model_serializer(mode="wrap")
    def serialize_model(self, handler):
        optional_fields = [
            "filter",
            "start_timestamp",
            "end_timestamp",
            "organization_id",
            "customer_id",
            "external_customer_id",
            "meter_id",
            "name",
            "source",
            "page",
            "limit",
            "sorting",
            "metadata",
        ]
        nullable_fields = [
            "filter",
            "start_timestamp",
            "end_timestamp",
            "organization_id",
            "customer_id",
            "external_customer_id",
            "meter_id",
            "name",
            "source",
            "sorting",
            "metadata",
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


class EventsListResponseTypedDict(TypedDict):
    result: ListResourceEventTypedDict


class EventsListResponse(BaseModel):
    next: Callable[[], Optional[EventsListResponse]]

    result: ListResourceEvent


MetersListQueryParamOrganizationIDFilterTypedDict = TypeAliasType(
    "MetersListQueryParamOrganizationIDFilterTypedDict", Union[str, List[str]]
)
r"""Filter by organization ID."""


MetersListQueryParamOrganizationIDFilter = TypeAliasType(
    "MetersListQueryParamOrganizationIDFilter", Union[str, List[str]]
)
r"""Filter by organization ID."""


class MetersListRequestTypedDict(TypedDict):
    organization_id: NotRequired[
        Nullable[MetersListQueryParamOrganizationIDFilterTypedDict]
    ]
    r"""Filter by organization ID."""
    query: NotRequired[Nullable[str]]
    r"""Filter by name."""
    page: NotRequired[int]
    r"""Page number, defaults to 1."""
    limit: NotRequired[int]
    r"""Size of a page, defaults to 10. Maximum is 100."""
    sorting: NotRequired[Nullable[List[MeterSortProperty]]]
    r"""Sorting criterion. Several criteria can be used simultaneously and will be applied in order. Add a minus sign `-` before the criteria name to sort by descending order."""
    metadata: NotRequired[Nullable[Dict[str, MetadataQueryTypedDict]]]
    r"""Filter by metadata key-value pairs. It uses the `deepObject` style, e.g. `?metadata[key]=value`."""


class MetersListRequest(BaseModel):
    organization_id: Annotated[
        OptionalNullable[MetersListQueryParamOrganizationIDFilter],
        FieldMetadata(query=QueryParamMetadata(style="form", explode=True)),
    ] = UNSET
    r"""Filter by organization ID."""

    query: Annotated[
        OptionalNullable[str],
        FieldMetadata(query=QueryParamMetadata(style="form", explode=True)),
    ] = UNSET
    r"""Filter by name."""

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
        OptionalNullable[List[MeterSortProperty]],
        FieldMetadata(query=QueryParamMetadata(style="form", explode=True)),
    ] = UNSET
    r"""Sorting criterion. Several criteria can be used simultaneously and will be applied in order. Add a minus sign `-` before the criteria name to sort by descending order."""

    metadata: Annotated[
        OptionalNullable[Dict[str, MetadataQuery]],
        FieldMetadata(query=QueryParamMetadata(style="deepObject", explode=True)),
    ] = UNSET
    r"""Filter by metadata key-value pairs. It uses the `deepObject` style, e.g. `?metadata[key]=value`."""

    @model_serializer(mode="wrap")
    def serialize_model(self, handler):
        optional_fields = [
            "organization_id",
            "query",
            "page",
            "limit",
            "sorting",
            "metadata",
        ]
        nullable_fields = ["organization_id", "query", "sorting", "metadata"]
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


class MetersListResponseTypedDict(TypedDict):
    result: ListResourceMeterTypedDict


class MetersListResponse(BaseModel):
    next: Callable[[], Optional[MetersListResponse]]

    result: ListResourceMeter
