# cloudmersive_barcode_api_client.BarcodeLookupApi

All URIs are relative to *https://api.cloudmersive.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**barcode_lookup_ean_lookup**](BarcodeLookupApi.md#barcode_lookup_ean_lookup) | **POST** /barcode/lookup/ean | Lookup EAN barcode value, return product data


# **barcode_lookup_ean_lookup**
> BarcodeLookupResponse barcode_lookup_ean_lookup(value)

Lookup EAN barcode value, return product data

Lookup an input EAN barcode and return key details about the product

### Example
```python
from __future__ import print_function
import time
import cloudmersive_barcode_api_client
from cloudmersive_barcode_api_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: Apikey
configuration = cloudmersive_barcode_api_client.Configuration()
configuration.api_key['Apikey'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Apikey'] = 'Bearer'

# create an instance of the API class
api_instance = cloudmersive_barcode_api_client.BarcodeLookupApi(cloudmersive_barcode_api_client.ApiClient(configuration))
value = 'value_example' # str | Barcode value

try:
    # Lookup EAN barcode value, return product data
    api_response = api_instance.barcode_lookup_ean_lookup(value)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BarcodeLookupApi->barcode_lookup_ean_lookup: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **value** | **str**| Barcode value | 

### Return type

[**BarcodeLookupResponse**](BarcodeLookupResponse.md)

### Authorization

[Apikey](../README.md#Apikey)

### HTTP request headers

 - **Content-Type**: application/json, text/json, application/xml, text/xml, application/x-www-form-urlencoded
 - **Accept**: application/json, text/json, application/xml, text/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

