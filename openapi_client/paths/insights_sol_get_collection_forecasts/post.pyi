# coding: utf-8

"""


    Generated by: https://openapi-generator.tech
"""

from dataclasses import dataclass
import typing_extensions
import urllib3
from urllib3._collections import HTTPHeaderDict

from openapi_client import api_client, exceptions
from datetime import date, datetime  # noqa: F401
import decimal  # noqa: F401
import functools  # noqa: F401
import io  # noqa: F401
import re  # noqa: F401
import typing  # noqa: F401
import typing_extensions  # noqa: F401
import uuid  # noqa: F401

import frozendict  # noqa: F401

from openapi_client import schemas  # noqa: F401

# body param


class SchemaForRequestBodyApplicationJson(
    schemas.DictSchema
):


    class MetaOapg:
        required = {
            "collection_tag",
        }
        
        class properties:
            collection_tag = schemas.StrSchema
            
            
            class percentiles(
                schemas.ListSchema
            ):
            
            
                class MetaOapg:
                    items = schemas.IntSchema
            
                def __new__(
                    cls,
                    _arg: typing.Union[typing.Tuple[typing.Union[MetaOapg.items, decimal.Decimal, int, ]], typing.List[typing.Union[MetaOapg.items, decimal.Decimal, int, ]]],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'percentiles':
                    return super().__new__(
                        cls,
                        _arg,
                        _configuration=_configuration,
                    )
            
                def __getitem__(self, i: int) -> MetaOapg.items:
                    return super().__getitem__(i)
            
            
            class voltype(
                schemas.EnumBase,
                schemas.StrSchema
            ):
                
                @schemas.classproperty
                def ARC(cls):
                    return cls("arc")
                
                @schemas.classproperty
                def GAR(cls):
                    return cls("gar")
                
                @schemas.classproperty
                def HAR(cls):
                    return cls("har")
            horizon = schemas.IntSchema
            frequency = schemas.StrSchema
            
            
            class dist(
                schemas.EnumBase,
                schemas.StrSchema
            ):
                
                @schemas.classproperty
                def NORM(cls):
                    return cls("norm")
                
                @schemas.classproperty
                def T(cls):
                    return cls("t")
            start_date = schemas.StrSchema
            end_date = schemas.StrSchema
            return_price_forecasts = schemas.BoolSchema
            alpha = schemas.NumberSchema
            
            
            class rept_curr(
                schemas.EnumBase,
                schemas.StrSchema
            ):
                
                @schemas.classproperty
                def SOL(cls):
                    return cls("sol")
                
                @schemas.classproperty
                def USD(cls):
                    return cls("usd")
            exclude_wash = schemas.BoolSchema
            
            
            class arch_params(
                schemas.DictSchema
            ):
            
            
                class MetaOapg:
                    
                    class properties:
                        mean = schemas.StrSchema
                        lags = schemas.IntSchema
                        vol = schemas.StrSchema
                        p = schemas.IntSchema
                        
                        
                        class dist(
                            schemas.EnumBase,
                            schemas.StrSchema
                        ):
                            
                            @schemas.classproperty
                            def NORM(cls):
                                return cls("norm")
                            
                            @schemas.classproperty
                            def T(cls):
                                return cls("t")
                        __annotations__ = {
                            "mean": mean,
                            "lags": lags,
                            "vol": vol,
                            "p": p,
                            "dist": dist,
                        }
                
                @typing.overload
                def __getitem__(self, name: typing_extensions.Literal["mean"]) -> MetaOapg.properties.mean: ...
                
                @typing.overload
                def __getitem__(self, name: typing_extensions.Literal["lags"]) -> MetaOapg.properties.lags: ...
                
                @typing.overload
                def __getitem__(self, name: typing_extensions.Literal["vol"]) -> MetaOapg.properties.vol: ...
                
                @typing.overload
                def __getitem__(self, name: typing_extensions.Literal["p"]) -> MetaOapg.properties.p: ...
                
                @typing.overload
                def __getitem__(self, name: typing_extensions.Literal["dist"]) -> MetaOapg.properties.dist: ...
                
                @typing.overload
                def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
                
                def __getitem__(self, name: typing.Union[typing_extensions.Literal["mean", "lags", "vol", "p", "dist", ], str]):
                    # dict_instance[name] accessor
                    return super().__getitem__(name)
                
                
                @typing.overload
                def get_item_oapg(self, name: typing_extensions.Literal["mean"]) -> typing.Union[MetaOapg.properties.mean, schemas.Unset]: ...
                
                @typing.overload
                def get_item_oapg(self, name: typing_extensions.Literal["lags"]) -> typing.Union[MetaOapg.properties.lags, schemas.Unset]: ...
                
                @typing.overload
                def get_item_oapg(self, name: typing_extensions.Literal["vol"]) -> typing.Union[MetaOapg.properties.vol, schemas.Unset]: ...
                
                @typing.overload
                def get_item_oapg(self, name: typing_extensions.Literal["p"]) -> typing.Union[MetaOapg.properties.p, schemas.Unset]: ...
                
                @typing.overload
                def get_item_oapg(self, name: typing_extensions.Literal["dist"]) -> typing.Union[MetaOapg.properties.dist, schemas.Unset]: ...
                
                @typing.overload
                def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
                
                def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["mean", "lags", "vol", "p", "dist", ], str]):
                    return super().get_item_oapg(name)
                
            
                def __new__(
                    cls,
                    *_args: typing.Union[dict, frozendict.frozendict, ],
                    mean: typing.Union[MetaOapg.properties.mean, str, schemas.Unset] = schemas.unset,
                    lags: typing.Union[MetaOapg.properties.lags, decimal.Decimal, int, schemas.Unset] = schemas.unset,
                    vol: typing.Union[MetaOapg.properties.vol, str, schemas.Unset] = schemas.unset,
                    p: typing.Union[MetaOapg.properties.p, decimal.Decimal, int, schemas.Unset] = schemas.unset,
                    dist: typing.Union[MetaOapg.properties.dist, str, schemas.Unset] = schemas.unset,
                    _configuration: typing.Optional[schemas.Configuration] = None,
                    **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
                ) -> 'arch_params':
                    return super().__new__(
                        cls,
                        *_args,
                        mean=mean,
                        lags=lags,
                        vol=vol,
                        p=p,
                        dist=dist,
                        _configuration=_configuration,
                        **kwargs,
                    )
            __annotations__ = {
                "collection_tag": collection_tag,
                "percentiles": percentiles,
                "voltype": voltype,
                "horizon": horizon,
                "frequency": frequency,
                "dist": dist,
                "start_date": start_date,
                "end_date": end_date,
                "return_price_forecasts": return_price_forecasts,
                "alpha": alpha,
                "rept_curr": rept_curr,
                "exclude_wash": exclude_wash,
                "arch_params": arch_params,
            }
    
    collection_tag: MetaOapg.properties.collection_tag
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["collection_tag"]) -> MetaOapg.properties.collection_tag: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["percentiles"]) -> MetaOapg.properties.percentiles: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["voltype"]) -> MetaOapg.properties.voltype: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["horizon"]) -> MetaOapg.properties.horizon: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["frequency"]) -> MetaOapg.properties.frequency: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["dist"]) -> MetaOapg.properties.dist: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["start_date"]) -> MetaOapg.properties.start_date: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["end_date"]) -> MetaOapg.properties.end_date: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["return_price_forecasts"]) -> MetaOapg.properties.return_price_forecasts: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["alpha"]) -> MetaOapg.properties.alpha: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["rept_curr"]) -> MetaOapg.properties.rept_curr: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["exclude_wash"]) -> MetaOapg.properties.exclude_wash: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["arch_params"]) -> MetaOapg.properties.arch_params: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["collection_tag", "percentiles", "voltype", "horizon", "frequency", "dist", "start_date", "end_date", "return_price_forecasts", "alpha", "rept_curr", "exclude_wash", "arch_params", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["collection_tag"]) -> MetaOapg.properties.collection_tag: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["percentiles"]) -> typing.Union[MetaOapg.properties.percentiles, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["voltype"]) -> typing.Union[MetaOapg.properties.voltype, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["horizon"]) -> typing.Union[MetaOapg.properties.horizon, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["frequency"]) -> typing.Union[MetaOapg.properties.frequency, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["dist"]) -> typing.Union[MetaOapg.properties.dist, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["start_date"]) -> typing.Union[MetaOapg.properties.start_date, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["end_date"]) -> typing.Union[MetaOapg.properties.end_date, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["return_price_forecasts"]) -> typing.Union[MetaOapg.properties.return_price_forecasts, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["alpha"]) -> typing.Union[MetaOapg.properties.alpha, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["rept_curr"]) -> typing.Union[MetaOapg.properties.rept_curr, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["exclude_wash"]) -> typing.Union[MetaOapg.properties.exclude_wash, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["arch_params"]) -> typing.Union[MetaOapg.properties.arch_params, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["collection_tag", "percentiles", "voltype", "horizon", "frequency", "dist", "start_date", "end_date", "return_price_forecasts", "alpha", "rept_curr", "exclude_wash", "arch_params", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *_args: typing.Union[dict, frozendict.frozendict, ],
        collection_tag: typing.Union[MetaOapg.properties.collection_tag, str, ],
        percentiles: typing.Union[MetaOapg.properties.percentiles, list, tuple, schemas.Unset] = schemas.unset,
        voltype: typing.Union[MetaOapg.properties.voltype, str, schemas.Unset] = schemas.unset,
        horizon: typing.Union[MetaOapg.properties.horizon, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        frequency: typing.Union[MetaOapg.properties.frequency, str, schemas.Unset] = schemas.unset,
        dist: typing.Union[MetaOapg.properties.dist, str, schemas.Unset] = schemas.unset,
        start_date: typing.Union[MetaOapg.properties.start_date, str, schemas.Unset] = schemas.unset,
        end_date: typing.Union[MetaOapg.properties.end_date, str, schemas.Unset] = schemas.unset,
        return_price_forecasts: typing.Union[MetaOapg.properties.return_price_forecasts, bool, schemas.Unset] = schemas.unset,
        alpha: typing.Union[MetaOapg.properties.alpha, decimal.Decimal, int, float, schemas.Unset] = schemas.unset,
        rept_curr: typing.Union[MetaOapg.properties.rept_curr, str, schemas.Unset] = schemas.unset,
        exclude_wash: typing.Union[MetaOapg.properties.exclude_wash, bool, schemas.Unset] = schemas.unset,
        arch_params: typing.Union[MetaOapg.properties.arch_params, dict, frozendict.frozendict, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'SchemaForRequestBodyApplicationJson':
        return super().__new__(
            cls,
            *_args,
            collection_tag=collection_tag,
            percentiles=percentiles,
            voltype=voltype,
            horizon=horizon,
            frequency=frequency,
            dist=dist,
            start_date=start_date,
            end_date=end_date,
            return_price_forecasts=return_price_forecasts,
            alpha=alpha,
            rept_curr=rept_curr,
            exclude_wash=exclude_wash,
            arch_params=arch_params,
            _configuration=_configuration,
            **kwargs,
        )


request_body_any_type = api_client.RequestBody(
    content={
        'application/json': api_client.MediaType(
            schema=SchemaForRequestBodyApplicationJson),
    },
)


@dataclass
class ApiResponseFor200(api_client.ApiResponse):
    response: urllib3.HTTPResponse
    body: typing.Union[
        schemas.Unset,
    ]
    headers: schemas.Unset = schemas.unset


_response_for_200 = api_client.OpenApiResponse(
    response_cls=ApiResponseFor200,
    content={
        'application/json': api_client.MediaType(),
    },
)


@dataclass
class ApiResponseFor400(api_client.ApiResponse):
    response: urllib3.HTTPResponse
    body: schemas.Unset = schemas.unset
    headers: schemas.Unset = schemas.unset


_response_for_400 = api_client.OpenApiResponse(
    response_cls=ApiResponseFor400,
)


@dataclass
class ApiResponseFor403(api_client.ApiResponse):
    response: urllib3.HTTPResponse
    body: schemas.Unset = schemas.unset
    headers: schemas.Unset = schemas.unset


_response_for_403 = api_client.OpenApiResponse(
    response_cls=ApiResponseFor403,
)
_all_accept_content_types = (
    'application/json',
)


class BaseApi(api_client.Api):
    @typing.overload
    def _get_sol_collection_forecasts_oapg(
        self,
        content_type: typing_extensions.Literal["application/json"] = ...,
        body: typing.Union[SchemaForRequestBodyApplicationJson, dict, frozendict.frozendict, schemas.Unset] = schemas.unset,
        accept_content_types: typing.Tuple[str] = _all_accept_content_types,
        stream: bool = False,
        timeout: typing.Optional[typing.Union[int, typing.Tuple]] = None,
        skip_deserialization: typing_extensions.Literal[False] = ...,
    ) -> typing.Union[
        ApiResponseFor200,
    ]: ...

    @typing.overload
    def _get_sol_collection_forecasts_oapg(
        self,
        content_type: str = ...,
        body: typing.Union[SchemaForRequestBodyApplicationJson, dict, frozendict.frozendict, schemas.Unset] = schemas.unset,
        accept_content_types: typing.Tuple[str] = _all_accept_content_types,
        stream: bool = False,
        timeout: typing.Optional[typing.Union[int, typing.Tuple]] = None,
        skip_deserialization: typing_extensions.Literal[False] = ...,
    ) -> typing.Union[
        ApiResponseFor200,
    ]: ...


    @typing.overload
    def _get_sol_collection_forecasts_oapg(
        self,
        skip_deserialization: typing_extensions.Literal[True],
        content_type: str = ...,
        body: typing.Union[SchemaForRequestBodyApplicationJson, dict, frozendict.frozendict, schemas.Unset] = schemas.unset,
        accept_content_types: typing.Tuple[str] = _all_accept_content_types,
        stream: bool = False,
        timeout: typing.Optional[typing.Union[int, typing.Tuple]] = None,
    ) -> api_client.ApiResponseWithoutDeserialization: ...

    @typing.overload
    def _get_sol_collection_forecasts_oapg(
        self,
        content_type: str = ...,
        body: typing.Union[SchemaForRequestBodyApplicationJson, dict, frozendict.frozendict, schemas.Unset] = schemas.unset,
        accept_content_types: typing.Tuple[str] = _all_accept_content_types,
        stream: bool = False,
        timeout: typing.Optional[typing.Union[int, typing.Tuple]] = None,
        skip_deserialization: bool = ...,
    ) -> typing.Union[
        ApiResponseFor200,
        api_client.ApiResponseWithoutDeserialization,
    ]: ...

    def _get_sol_collection_forecasts_oapg(
        self,
        content_type: str = 'application/json',
        body: typing.Union[SchemaForRequestBodyApplicationJson, dict, frozendict.frozendict, schemas.Unset] = schemas.unset,
        accept_content_types: typing.Tuple[str] = _all_accept_content_types,
        stream: bool = False,
        timeout: typing.Optional[typing.Union[int, typing.Tuple]] = None,
        skip_deserialization: bool = False,
    ):
        """
        Price Forecast by Collection
        :param skip_deserialization: If true then api_response.response will be set but
            api_response.body and api_response.headers will not be deserialized into schema
            class instances
        """
        used_path = path.value

        _headers = HTTPHeaderDict()
        # TODO add cookie handling
        if accept_content_types:
            for accept_content_type in accept_content_types:
                _headers.add('Accept', accept_content_type)

        _fields = None
        _body = None
        if body is not schemas.unset:
            serialized_data = request_body_any_type.serialize(body, content_type)
            _headers.add('Content-Type', content_type)
            if 'fields' in serialized_data:
                _fields = serialized_data['fields']
            elif 'body' in serialized_data:
                _body = serialized_data['body']
        response = self.api_client.call_api(
            resource_path=used_path,
            method='post'.upper(),
            headers=_headers,
            fields=_fields,
            body=_body,
            auth_settings=_auth,
            stream=stream,
            timeout=timeout,
        )

        if skip_deserialization:
            api_response = api_client.ApiResponseWithoutDeserialization(response=response)
        else:
            response_for_status = _status_code_to_response.get(str(response.status))
            if response_for_status:
                api_response = response_for_status.deserialize(response, self.api_client.configuration)
            else:
                api_response = api_client.ApiResponseWithoutDeserialization(response=response)

        if not 200 <= response.status <= 299:
            raise exceptions.ApiException(
                status=response.status,
                reason=response.reason,
                api_response=api_response
            )

        return api_response


class GetSolCollectionForecasts(BaseApi):
    # this class is used by api classes that refer to endpoints with operationId fn names

    @typing.overload
    def get_sol_collection_forecasts(
        self,
        content_type: typing_extensions.Literal["application/json"] = ...,
        body: typing.Union[SchemaForRequestBodyApplicationJson, dict, frozendict.frozendict, schemas.Unset] = schemas.unset,
        accept_content_types: typing.Tuple[str] = _all_accept_content_types,
        stream: bool = False,
        timeout: typing.Optional[typing.Union[int, typing.Tuple]] = None,
        skip_deserialization: typing_extensions.Literal[False] = ...,
    ) -> typing.Union[
        ApiResponseFor200,
    ]: ...

    @typing.overload
    def get_sol_collection_forecasts(
        self,
        content_type: str = ...,
        body: typing.Union[SchemaForRequestBodyApplicationJson, dict, frozendict.frozendict, schemas.Unset] = schemas.unset,
        accept_content_types: typing.Tuple[str] = _all_accept_content_types,
        stream: bool = False,
        timeout: typing.Optional[typing.Union[int, typing.Tuple]] = None,
        skip_deserialization: typing_extensions.Literal[False] = ...,
    ) -> typing.Union[
        ApiResponseFor200,
    ]: ...


    @typing.overload
    def get_sol_collection_forecasts(
        self,
        skip_deserialization: typing_extensions.Literal[True],
        content_type: str = ...,
        body: typing.Union[SchemaForRequestBodyApplicationJson, dict, frozendict.frozendict, schemas.Unset] = schemas.unset,
        accept_content_types: typing.Tuple[str] = _all_accept_content_types,
        stream: bool = False,
        timeout: typing.Optional[typing.Union[int, typing.Tuple]] = None,
    ) -> api_client.ApiResponseWithoutDeserialization: ...

    @typing.overload
    def get_sol_collection_forecasts(
        self,
        content_type: str = ...,
        body: typing.Union[SchemaForRequestBodyApplicationJson, dict, frozendict.frozendict, schemas.Unset] = schemas.unset,
        accept_content_types: typing.Tuple[str] = _all_accept_content_types,
        stream: bool = False,
        timeout: typing.Optional[typing.Union[int, typing.Tuple]] = None,
        skip_deserialization: bool = ...,
    ) -> typing.Union[
        ApiResponseFor200,
        api_client.ApiResponseWithoutDeserialization,
    ]: ...

    def get_sol_collection_forecasts(
        self,
        content_type: str = 'application/json',
        body: typing.Union[SchemaForRequestBodyApplicationJson, dict, frozendict.frozendict, schemas.Unset] = schemas.unset,
        accept_content_types: typing.Tuple[str] = _all_accept_content_types,
        stream: bool = False,
        timeout: typing.Optional[typing.Union[int, typing.Tuple]] = None,
        skip_deserialization: bool = False,
    ):
        return self._get_sol_collection_forecasts_oapg(
            body=body,
            content_type=content_type,
            accept_content_types=accept_content_types,
            stream=stream,
            timeout=timeout,
            skip_deserialization=skip_deserialization
        )


class ApiForpost(BaseApi):
    # this class is used by api classes that refer to endpoints by path and http method names

    @typing.overload
    def post(
        self,
        content_type: typing_extensions.Literal["application/json"] = ...,
        body: typing.Union[SchemaForRequestBodyApplicationJson, dict, frozendict.frozendict, schemas.Unset] = schemas.unset,
        accept_content_types: typing.Tuple[str] = _all_accept_content_types,
        stream: bool = False,
        timeout: typing.Optional[typing.Union[int, typing.Tuple]] = None,
        skip_deserialization: typing_extensions.Literal[False] = ...,
    ) -> typing.Union[
        ApiResponseFor200,
    ]: ...

    @typing.overload
    def post(
        self,
        content_type: str = ...,
        body: typing.Union[SchemaForRequestBodyApplicationJson, dict, frozendict.frozendict, schemas.Unset] = schemas.unset,
        accept_content_types: typing.Tuple[str] = _all_accept_content_types,
        stream: bool = False,
        timeout: typing.Optional[typing.Union[int, typing.Tuple]] = None,
        skip_deserialization: typing_extensions.Literal[False] = ...,
    ) -> typing.Union[
        ApiResponseFor200,
    ]: ...


    @typing.overload
    def post(
        self,
        skip_deserialization: typing_extensions.Literal[True],
        content_type: str = ...,
        body: typing.Union[SchemaForRequestBodyApplicationJson, dict, frozendict.frozendict, schemas.Unset] = schemas.unset,
        accept_content_types: typing.Tuple[str] = _all_accept_content_types,
        stream: bool = False,
        timeout: typing.Optional[typing.Union[int, typing.Tuple]] = None,
    ) -> api_client.ApiResponseWithoutDeserialization: ...

    @typing.overload
    def post(
        self,
        content_type: str = ...,
        body: typing.Union[SchemaForRequestBodyApplicationJson, dict, frozendict.frozendict, schemas.Unset] = schemas.unset,
        accept_content_types: typing.Tuple[str] = _all_accept_content_types,
        stream: bool = False,
        timeout: typing.Optional[typing.Union[int, typing.Tuple]] = None,
        skip_deserialization: bool = ...,
    ) -> typing.Union[
        ApiResponseFor200,
        api_client.ApiResponseWithoutDeserialization,
    ]: ...

    def post(
        self,
        content_type: str = 'application/json',
        body: typing.Union[SchemaForRequestBodyApplicationJson, dict, frozendict.frozendict, schemas.Unset] = schemas.unset,
        accept_content_types: typing.Tuple[str] = _all_accept_content_types,
        stream: bool = False,
        timeout: typing.Optional[typing.Union[int, typing.Tuple]] = None,
        skip_deserialization: bool = False,
    ):
        return self._get_sol_collection_forecasts_oapg(
            body=body,
            content_type=content_type,
            accept_content_types=accept_content_types,
            stream=stream,
            timeout=timeout,
            skip_deserialization=skip_deserialization
        )

