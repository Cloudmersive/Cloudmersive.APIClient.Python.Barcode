# coding: utf-8

"""
    barcodeapi

    Barcode APIs let you generate barcode images, and recognize values from images of barcodes.  # noqa: E501

    OpenAPI spec version: v1
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import re  # noqa: F401

# python 2 and python 3 compatibility library
import six

from cloudmersive_barcode_api_client.api_client import ApiClient


class GenerateBarcodeApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def generate_barcode_ean13(self, value, **kwargs):  # noqa: E501
        """Generate a EAN-13 code barcode as PNG file  # noqa: E501

        Validates and generate a EAN-13 barcode as a PNG file, a type of 1D barcode  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.generate_barcode_ean13(value, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str value: Barcode value to generate from (required)
        :return: str
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.generate_barcode_ean13_with_http_info(value, **kwargs)  # noqa: E501
        else:
            (data) = self.generate_barcode_ean13_with_http_info(value, **kwargs)  # noqa: E501
            return data

    def generate_barcode_ean13_with_http_info(self, value, **kwargs):  # noqa: E501
        """Generate a EAN-13 code barcode as PNG file  # noqa: E501

        Validates and generate a EAN-13 barcode as a PNG file, a type of 1D barcode  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.generate_barcode_ean13_with_http_info(value, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str value: Barcode value to generate from (required)
        :return: str
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['value']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method generate_barcode_ean13" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'value' is set
        if ('value' not in params or
                params['value'] is None):
            raise ValueError("Missing the required parameter `value` when calling `generate_barcode_ean13`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'value' in params:
            body_params = params['value']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/octet-stream'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json', 'text/json', 'application/xml', 'text/xml', 'application/x-www-form-urlencoded'])  # noqa: E501

        # Authentication setting
        auth_settings = ['Apikey']  # noqa: E501

        return self.api_client.call_api(
            '/barcode/generate/ean-13', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='str',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def generate_barcode_ean8(self, value, **kwargs):  # noqa: E501
        """Generate a EAN-8 code barcode as PNG file  # noqa: E501

        Validates and generate a EAN-8 barcode as a PNG file, a type of 1D barcode  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.generate_barcode_ean8(value, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str value: Barcode value to generate from (required)
        :return: str
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.generate_barcode_ean8_with_http_info(value, **kwargs)  # noqa: E501
        else:
            (data) = self.generate_barcode_ean8_with_http_info(value, **kwargs)  # noqa: E501
            return data

    def generate_barcode_ean8_with_http_info(self, value, **kwargs):  # noqa: E501
        """Generate a EAN-8 code barcode as PNG file  # noqa: E501

        Validates and generate a EAN-8 barcode as a PNG file, a type of 1D barcode  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.generate_barcode_ean8_with_http_info(value, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str value: Barcode value to generate from (required)
        :return: str
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['value']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method generate_barcode_ean8" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'value' is set
        if ('value' not in params or
                params['value'] is None):
            raise ValueError("Missing the required parameter `value` when calling `generate_barcode_ean8`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'value' in params:
            body_params = params['value']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/octet-stream'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json', 'text/json', 'application/xml', 'text/xml', 'application/x-www-form-urlencoded'])  # noqa: E501

        # Authentication setting
        auth_settings = ['Apikey']  # noqa: E501

        return self.api_client.call_api(
            '/barcode/generate/ean-8', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='str',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def generate_barcode_qr_code(self, value, **kwargs):  # noqa: E501
        """Generate a QR code barcode as PNG file  # noqa: E501

        Generate a QR code barcode as a PNG file, a type of 2D barcode which can encode free-form text information  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.generate_barcode_qr_code(value, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str value: QR code text to convert into the QR code barcode (required)
        :return: str
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.generate_barcode_qr_code_with_http_info(value, **kwargs)  # noqa: E501
        else:
            (data) = self.generate_barcode_qr_code_with_http_info(value, **kwargs)  # noqa: E501
            return data

    def generate_barcode_qr_code_with_http_info(self, value, **kwargs):  # noqa: E501
        """Generate a QR code barcode as PNG file  # noqa: E501

        Generate a QR code barcode as a PNG file, a type of 2D barcode which can encode free-form text information  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.generate_barcode_qr_code_with_http_info(value, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str value: QR code text to convert into the QR code barcode (required)
        :return: str
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['value']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method generate_barcode_qr_code" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'value' is set
        if ('value' not in params or
                params['value'] is None):
            raise ValueError("Missing the required parameter `value` when calling `generate_barcode_qr_code`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'value' in params:
            body_params = params['value']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/octet-stream'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json', 'text/json', 'application/xml', 'text/xml', 'application/x-www-form-urlencoded'])  # noqa: E501

        # Authentication setting
        auth_settings = ['Apikey']  # noqa: E501

        return self.api_client.call_api(
            '/barcode/generate/qrcode', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='str',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def generate_barcode_upca(self, value, **kwargs):  # noqa: E501
        """Generate a UPC-A code barcode as PNG file  # noqa: E501

        Validate and generate a UPC-A barcode as a PNG file, a type of 1D barcode  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.generate_barcode_upca(value, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str value: UPC-A barcode value to generate from (required)
        :return: str
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.generate_barcode_upca_with_http_info(value, **kwargs)  # noqa: E501
        else:
            (data) = self.generate_barcode_upca_with_http_info(value, **kwargs)  # noqa: E501
            return data

    def generate_barcode_upca_with_http_info(self, value, **kwargs):  # noqa: E501
        """Generate a UPC-A code barcode as PNG file  # noqa: E501

        Validate and generate a UPC-A barcode as a PNG file, a type of 1D barcode  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.generate_barcode_upca_with_http_info(value, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str value: UPC-A barcode value to generate from (required)
        :return: str
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['value']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method generate_barcode_upca" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'value' is set
        if ('value' not in params or
                params['value'] is None):
            raise ValueError("Missing the required parameter `value` when calling `generate_barcode_upca`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'value' in params:
            body_params = params['value']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/octet-stream'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json', 'text/json', 'application/xml', 'text/xml', 'application/x-www-form-urlencoded'])  # noqa: E501

        # Authentication setting
        auth_settings = ['Apikey']  # noqa: E501

        return self.api_client.call_api(
            '/barcode/generate/upc-a', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='str',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def generate_barcode_upce(self, value, **kwargs):  # noqa: E501
        """Generate a UPC-E code barcode as PNG file  # noqa: E501

        Validates and generate a UPC-E barcode as a PNG file, a type of 1D barcode  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.generate_barcode_upce(value, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str value: UPC-E barcode value to generate from (required)
        :return: str
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.generate_barcode_upce_with_http_info(value, **kwargs)  # noqa: E501
        else:
            (data) = self.generate_barcode_upce_with_http_info(value, **kwargs)  # noqa: E501
            return data

    def generate_barcode_upce_with_http_info(self, value, **kwargs):  # noqa: E501
        """Generate a UPC-E code barcode as PNG file  # noqa: E501

        Validates and generate a UPC-E barcode as a PNG file, a type of 1D barcode  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.generate_barcode_upce_with_http_info(value, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str value: UPC-E barcode value to generate from (required)
        :return: str
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['value']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method generate_barcode_upce" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'value' is set
        if ('value' not in params or
                params['value'] is None):
            raise ValueError("Missing the required parameter `value` when calling `generate_barcode_upce`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'value' in params:
            body_params = params['value']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/octet-stream'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json', 'text/json', 'application/xml', 'text/xml', 'application/x-www-form-urlencoded'])  # noqa: E501

        # Authentication setting
        auth_settings = ['Apikey']  # noqa: E501

        return self.api_client.call_api(
            '/barcode/generate/upc-e', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='str',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)
