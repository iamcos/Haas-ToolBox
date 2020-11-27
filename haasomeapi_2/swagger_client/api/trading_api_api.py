# coding: utf-8

"""
    Haasbot LocalAPI

    This is a rest api swagger for the Haasbot.  # noqa: E501

    OpenAPI spec version: 1.0.0
    Contact: support@haasonline.com
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

from __future__ import absolute_import

import re  # noqa: F401

# python 2 and python 3 compatibility library
import six

from swagger_client.api_client import ApiClient


class TradingAPIApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def cancel_order(self, **kwargs):  # noqa: E501
        """Cancels a open order  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.cancel_order(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str userid:
        :param str interfacekey:
        :param str accountid:
        :param str orderid:
        :return: TradingapiCancelOrderResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.cancel_order_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.cancel_order_with_http_info(**kwargs)  # noqa: E501
            return data

    def cancel_order_with_http_info(self, **kwargs):  # noqa: E501
        """Cancels a open order  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.cancel_order_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str userid:
        :param str interfacekey:
        :param str accountid:
        :param str orderid:
        :return: TradingapiCancelOrderResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['userid', 'interfacekey', 'accountid', 'orderid']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method cancel_order" % key
                )
            params[key] = val
        del params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}
        if 'userid' in params:
            form_params.append(('userid', params['userid']))  # noqa: E501
        if 'interfacekey' in params:
            form_params.append(('interfacekey', params['interfacekey']))  # noqa: E501
        if 'accountid' in params:
            form_params.append(('accountid', params['accountid']))  # noqa: E501
        if 'orderid' in params:
            form_params.append(('orderid', params['orderid']))  # noqa: E501

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/x-www-form-urlencoded'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/TradingAPI.php?channel=CANCEL_ORDER', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='TradingapiCancelOrderResponse',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def max_amount(self, **kwargs):  # noqa: E501
        """Calculates the maximum trade amount, price and margin  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.max_amount(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str userid:
        :param str interfacekey:
        :param str accountid:
        :param str market:
        :param float price:
        :param float usedamount:
        :param float amountpercentage:
        :param bool isbuy:
        :return: TradingapiMaxAmountResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.max_amount_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.max_amount_with_http_info(**kwargs)  # noqa: E501
            return data

    def max_amount_with_http_info(self, **kwargs):  # noqa: E501
        """Calculates the maximum trade amount, price and margin  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.max_amount_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str userid:
        :param str interfacekey:
        :param str accountid:
        :param str market:
        :param float price:
        :param float usedamount:
        :param float amountpercentage:
        :param bool isbuy:
        :return: TradingapiMaxAmountResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['userid', 'interfacekey', 'accountid', 'market', 'price', 'usedamount', 'amountpercentage', 'isbuy']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method max_amount" % key
                )
            params[key] = val
        del params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}
        if 'userid' in params:
            form_params.append(('userid', params['userid']))  # noqa: E501
        if 'interfacekey' in params:
            form_params.append(('interfacekey', params['interfacekey']))  # noqa: E501
        if 'accountid' in params:
            form_params.append(('accountid', params['accountid']))  # noqa: E501
        if 'market' in params:
            form_params.append(('market', params['market']))  # noqa: E501
        if 'price' in params:
            form_params.append(('price', params['price']))  # noqa: E501
        if 'usedamount' in params:
            form_params.append(('usedamount', params['usedamount']))  # noqa: E501
        if 'amountpercentage' in params:
            form_params.append(('amountpercentage', params['amountpercentage']))  # noqa: E501
        if 'isbuy' in params:
            form_params.append(('isbuy', params['isbuy']))  # noqa: E501

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/x-www-form-urlencoded'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/TradingAPI.php?channel=MAX_AMOUNT', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='TradingapiMaxAmountResponse',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def place_order(self, **kwargs):  # noqa: E501
        """Places a order  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.place_order(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str userid:
        :param str interfacekey:
        :param object order:
        :return: TradingapiPlaceOrderResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.place_order_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.place_order_with_http_info(**kwargs)  # noqa: E501
            return data

    def place_order_with_http_info(self, **kwargs):  # noqa: E501
        """Places a order  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.place_order_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str userid:
        :param str interfacekey:
        :param object order:
        :return: TradingapiPlaceOrderResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['userid', 'interfacekey', 'order']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method place_order" % key
                )
            params[key] = val
        del params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}
        if 'userid' in params:
            form_params.append(('userid', params['userid']))  # noqa: E501
        if 'interfacekey' in params:
            form_params.append(('interfacekey', params['interfacekey']))  # noqa: E501
        if 'order' in params:
            form_params.append(('order', params['order']))  # noqa: E501

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/x-www-form-urlencoded'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/TradingAPI.php?channel=PLACE_ORDER', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='TradingapiPlaceOrderResponse',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def used_margin(self, **kwargs):  # noqa: E501
        """Returns what the used margin is  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.used_margin(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str userid:
        :param str interfacekey:
        :param str drivername:
        :param int drivertype:
        :param str market:
        :param float leverage:
        :param float price:
        :param float amount:
        :return: TradingapiUsedMarginResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.used_margin_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.used_margin_with_http_info(**kwargs)  # noqa: E501
            return data

    def used_margin_with_http_info(self, **kwargs):  # noqa: E501
        """Returns what the used margin is  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.used_margin_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str userid:
        :param str interfacekey:
        :param str drivername:
        :param int drivertype:
        :param str market:
        :param float leverage:
        :param float price:
        :param float amount:
        :return: TradingapiUsedMarginResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['userid', 'interfacekey', 'drivername', 'drivertype', 'market', 'leverage', 'price', 'amount']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method used_margin" % key
                )
            params[key] = val
        del params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}
        if 'userid' in params:
            form_params.append(('userid', params['userid']))  # noqa: E501
        if 'interfacekey' in params:
            form_params.append(('interfacekey', params['interfacekey']))  # noqa: E501
        if 'drivername' in params:
            form_params.append(('drivername', params['drivername']))  # noqa: E501
        if 'drivertype' in params:
            form_params.append(('drivertype', params['drivertype']))  # noqa: E501
        if 'market' in params:
            form_params.append(('market', params['market']))  # noqa: E501
        if 'leverage' in params:
            form_params.append(('leverage', params['leverage']))  # noqa: E501
        if 'price' in params:
            form_params.append(('price', params['price']))  # noqa: E501
        if 'amount' in params:
            form_params.append(('amount', params['amount']))  # noqa: E501

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/x-www-form-urlencoded'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/TradingAPI.php?channel=USED_MARGIN', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='TradingapiUsedMarginResponse',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)
