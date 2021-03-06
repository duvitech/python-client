# coding: utf-8

"""
    Curaegis Egress API

    Curaegis egress data API  # noqa: E501

    OpenAPI spec version: v1
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import re  # noqa: F401

# python 2 and python 3 compatibility library
import six

from swagger_client.api_client import ApiClient


class ResourcesApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def resourcelog_get_by_date_range(self, id, resource, basedate, enddate, **kwargs):  # noqa: E501
        """resourcelog_get_by_date_range  # noqa: E501

        Get resource timeseries log by user id and date range  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.resourcelog_get_by_date_range(id, resource, basedate, enddate, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str id: 3P7JCB (required)
        :param str resource: the resource path (required)
        :param str basedate: the range start date, in the format yyyy-MM-dd or today (required)
        :param str enddate: the end date of the range (required)
        :return: InlineResponse2003
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.resourcelog_get_by_date_range_with_http_info(id, resource, basedate, enddate, **kwargs)  # noqa: E501
        else:
            (data) = self.resourcelog_get_by_date_range_with_http_info(id, resource, basedate, enddate, **kwargs)  # noqa: E501
            return data

    def resourcelog_get_by_date_range_with_http_info(self, id, resource, basedate, enddate, **kwargs):  # noqa: E501
        """resourcelog_get_by_date_range  # noqa: E501

        Get resource timeseries log by user id and date range  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.resourcelog_get_by_date_range_with_http_info(id, resource, basedate, enddate, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str id: 3P7JCB (required)
        :param str resource: the resource path (required)
        :param str basedate: the range start date, in the format yyyy-MM-dd or today (required)
        :param str enddate: the end date of the range (required)
        :return: InlineResponse2003
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['id', 'resource', 'basedate', 'enddate']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method resourcelog_get_by_date_range" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'id' is set
        if ('id' not in params or
                params['id'] is None):
            raise ValueError("Missing the required parameter `id` when calling `resourcelog_get_by_date_range`")  # noqa: E501
        # verify the required parameter 'resource' is set
        if ('resource' not in params or
                params['resource'] is None):
            raise ValueError("Missing the required parameter `resource` when calling `resourcelog_get_by_date_range`")  # noqa: E501
        # verify the required parameter 'basedate' is set
        if ('basedate' not in params or
                params['basedate'] is None):
            raise ValueError("Missing the required parameter `basedate` when calling `resourcelog_get_by_date_range`")  # noqa: E501
        # verify the required parameter 'enddate' is set
        if ('enddate' not in params or
                params['enddate'] is None):
            raise ValueError("Missing the required parameter `enddate` when calling `resourcelog_get_by_date_range`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'id' in params:
            path_params['id'] = params['id']  # noqa: E501
        if 'resource' in params:
            path_params['resource'] = params['resource']  # noqa: E501
        if 'basedate' in params:
            path_params['basedate'] = params['basedate']  # noqa: E501
        if 'enddate' in params:
            path_params['enddate'] = params['enddate']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['ApiKeyAuth']  # noqa: E501

        return self.api_client.call_api(
            '/{id}/activities/{resource}/range/{basedate}/{enddate}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='InlineResponse2003',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def resourcelog_get_by_id(self, id, resource, _date, period, **kwargs):  # noqa: E501
        """resourcelog_get_by_id  # noqa: E501

        Get resource log by user id and date  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.resourcelog_get_by_id(id, resource, _date, period, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str id: 3P7JCB (required)
        :param str resource: the resource path (required)
        :param str _date: the end date of the period specified in the format yyyy-MM-dd or today (required)
        :param str period: The range for which data will be returned. Options are 1d, 7d, 30d, 1w, 1m (required)
        :return: InlineResponse2003
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.resourcelog_get_by_id_with_http_info(id, resource, _date, period, **kwargs)  # noqa: E501
        else:
            (data) = self.resourcelog_get_by_id_with_http_info(id, resource, _date, period, **kwargs)  # noqa: E501
            return data

    def resourcelog_get_by_id_with_http_info(self, id, resource, _date, period, **kwargs):  # noqa: E501
        """resourcelog_get_by_id  # noqa: E501

        Get resource log by user id and date  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.resourcelog_get_by_id_with_http_info(id, resource, _date, period, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str id: 3P7JCB (required)
        :param str resource: the resource path (required)
        :param str _date: the end date of the period specified in the format yyyy-MM-dd or today (required)
        :param str period: The range for which data will be returned. Options are 1d, 7d, 30d, 1w, 1m (required)
        :return: InlineResponse2003
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['id', 'resource', '_date', 'period']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method resourcelog_get_by_id" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'id' is set
        if ('id' not in params or
                params['id'] is None):
            raise ValueError("Missing the required parameter `id` when calling `resourcelog_get_by_id`")  # noqa: E501
        # verify the required parameter 'resource' is set
        if ('resource' not in params or
                params['resource'] is None):
            raise ValueError("Missing the required parameter `resource` when calling `resourcelog_get_by_id`")  # noqa: E501
        # verify the required parameter '_date' is set
        if ('_date' not in params or
                params['_date'] is None):
            raise ValueError("Missing the required parameter `_date` when calling `resourcelog_get_by_id`")  # noqa: E501
        # verify the required parameter 'period' is set
        if ('period' not in params or
                params['period'] is None):
            raise ValueError("Missing the required parameter `period` when calling `resourcelog_get_by_id`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'id' in params:
            path_params['id'] = params['id']  # noqa: E501
        if 'resource' in params:
            path_params['resource'] = params['resource']  # noqa: E501
        if '_date' in params:
            path_params['date'] = params['_date']  # noqa: E501
        if 'period' in params:
            path_params['period'] = params['period']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['ApiKeyAuth']  # noqa: E501

        return self.api_client.call_api(
            '/{id}/activities/{resource}/date/{date}/{period}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='InlineResponse2003',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)
