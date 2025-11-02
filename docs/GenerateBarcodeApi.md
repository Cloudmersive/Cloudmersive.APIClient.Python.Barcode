# cloudmersive_barcode_api_client.GenerateBarcodeApi

All URIs are relative to *https://api.cloudmersive.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**generate_barcode_code128**](GenerateBarcodeApi.md#generate_barcode_code128) | **POST** /barcode/generate/code-128 | Generate a EAN-13 code barcode as PNG file
[**generate_barcode_ean13**](GenerateBarcodeApi.md#generate_barcode_ean13) | **POST** /barcode/generate/ean-13 | Generate a EAN-13 code barcode as PNG file
[**generate_barcode_ean8**](GenerateBarcodeApi.md#generate_barcode_ean8) | **POST** /barcode/generate/ean-8 | Generate a EAN-8 code barcode as PNG file
[**generate_barcode_qr_code**](GenerateBarcodeApi.md#generate_barcode_qr_code) | **POST** /barcode/generate/qrcode | Generate a QR code barcode as PNG file
[**generate_barcode_upca**](GenerateBarcodeApi.md#generate_barcode_upca) | **POST** /barcode/generate/upc-a | Generate a UPC-A code barcode as PNG file
[**generate_barcode_upce**](GenerateBarcodeApi.md#generate_barcode_upce) | **POST** /barcode/generate/upc-e | Generate a UPC-E code barcode as PNG file


# **generate_barcode_code128**
> str generate_barcode_code128(value, width=width, height=height, include_label=include_label)

Generate a EAN-13 code barcode as PNG file

Validates and generate a EAN-13 barcode as a PNG file, a type of 1D barcode

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
api_instance = cloudmersive_barcode_api_client.GenerateBarcodeApi(cloudmersive_barcode_api_client.ApiClient(configuration))
value = 'value_example' # str | Barcode value to generate from
width = 56 # int | Optional: width of the barcode in pixels.  Minimum value of 10. (optional)
height = 56 # int | Optional: width of the barcode in pixels.  Minimum value of 10. (optional)
include_label = true # bool | Optional: show text label on the image of the barcode value, default is true. (optional)

try:
    # Generate a EAN-13 code barcode as PNG file
    api_response = api_instance.generate_barcode_code128(value, width=width, height=height, include_label=include_label)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling GenerateBarcodeApi->generate_barcode_code128: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **value** | **str**| Barcode value to generate from | 
 **width** | **int**| Optional: width of the barcode in pixels.  Minimum value of 10. | [optional] 
 **height** | **int**| Optional: width of the barcode in pixels.  Minimum value of 10. | [optional] 
 **include_label** | **bool**| Optional: show text label on the image of the barcode value, default is true. | [optional] 

### Return type

**str**

### Authorization

[Apikey](../README.md#Apikey)

### HTTP request headers

 - **Content-Type**: application/json, text/json, application/xml, text/xml, application/x-www-form-urlencoded
 - **Accept**: application/octet-stream

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **generate_barcode_ean13**
> str generate_barcode_ean13(value, width=width, height=height, include_label=include_label)

Generate a EAN-13 code barcode as PNG file

Validates and generate a EAN-13 barcode as a PNG file, a type of 1D barcode

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
api_instance = cloudmersive_barcode_api_client.GenerateBarcodeApi(cloudmersive_barcode_api_client.ApiClient(configuration))
value = 'value_example' # str | Barcode value to generate from
width = 56 # int | Optional: width of the barcode in pixels.  Minimum value of 10. (optional)
height = 56 # int | Optional: width of the barcode in pixels.  Minimum value of 10. (optional)
include_label = true # bool | Optional: show text label on the image of the barcode value, default is true. (optional)

try:
    # Generate a EAN-13 code barcode as PNG file
    api_response = api_instance.generate_barcode_ean13(value, width=width, height=height, include_label=include_label)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling GenerateBarcodeApi->generate_barcode_ean13: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **value** | **str**| Barcode value to generate from | 
 **width** | **int**| Optional: width of the barcode in pixels.  Minimum value of 10. | [optional] 
 **height** | **int**| Optional: width of the barcode in pixels.  Minimum value of 10. | [optional] 
 **include_label** | **bool**| Optional: show text label on the image of the barcode value, default is true. | [optional] 

### Return type

**str**

### Authorization

[Apikey](../README.md#Apikey)

### HTTP request headers

 - **Content-Type**: application/json, text/json, application/xml, text/xml, application/x-www-form-urlencoded
 - **Accept**: application/octet-stream

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **generate_barcode_ean8**
> str generate_barcode_ean8(value, width=width, height=height, include_label=include_label)

Generate a EAN-8 code barcode as PNG file

Validates and generate a EAN-8 barcode as a PNG file, a type of 1D barcode

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
api_instance = cloudmersive_barcode_api_client.GenerateBarcodeApi(cloudmersive_barcode_api_client.ApiClient(configuration))
value = 'value_example' # str | Barcode value to generate from
width = 56 # int | Optional: width of the barcode in pixels.  Minimum value of 10. (optional)
height = 56 # int | Optional: width of the barcode in pixels.  Minimum value of 10. (optional)
include_label = true # bool | Optional: show text label on the image of the barcode value, default is true. (optional)

try:
    # Generate a EAN-8 code barcode as PNG file
    api_response = api_instance.generate_barcode_ean8(value, width=width, height=height, include_label=include_label)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling GenerateBarcodeApi->generate_barcode_ean8: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **value** | **str**| Barcode value to generate from | 
 **width** | **int**| Optional: width of the barcode in pixels.  Minimum value of 10. | [optional] 
 **height** | **int**| Optional: width of the barcode in pixels.  Minimum value of 10. | [optional] 
 **include_label** | **bool**| Optional: show text label on the image of the barcode value, default is true. | [optional] 

### Return type

**str**

### Authorization

[Apikey](../README.md#Apikey)

### HTTP request headers

 - **Content-Type**: application/json, text/json, application/xml, text/xml, application/x-www-form-urlencoded
 - **Accept**: application/octet-stream

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **generate_barcode_qr_code**
> str generate_barcode_qr_code(value, width=width, height=height)

Generate a QR code barcode as PNG file

Generate a QR code barcode as a PNG file, a type of 2D barcode which can encode free-form text information

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
api_instance = cloudmersive_barcode_api_client.GenerateBarcodeApi(cloudmersive_barcode_api_client.ApiClient(configuration))
value = 'value_example' # str | QR code text to convert into the QR code barcode
width = 56 # int | Optional: width of the barcode in pixels.  Minimum value of 10. (optional)
height = 56 # int | Optional: width of the barcode in pixels.  Minimum value of 10. (optional)

try:
    # Generate a QR code barcode as PNG file
    api_response = api_instance.generate_barcode_qr_code(value, width=width, height=height)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling GenerateBarcodeApi->generate_barcode_qr_code: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **value** | **str**| QR code text to convert into the QR code barcode | 
 **width** | **int**| Optional: width of the barcode in pixels.  Minimum value of 10. | [optional] 
 **height** | **int**| Optional: width of the barcode in pixels.  Minimum value of 10. | [optional] 

### Return type

**str**

### Authorization

[Apikey](../README.md#Apikey)

### HTTP request headers

 - **Content-Type**: application/json, text/json, application/xml, text/xml, application/x-www-form-urlencoded
 - **Accept**: application/octet-stream

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **generate_barcode_upca**
> str generate_barcode_upca(value, width=width, height=height, include_label=include_label)

Generate a UPC-A code barcode as PNG file

Validate and generate a UPC-A barcode as a PNG file, a type of 1D barcode

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
api_instance = cloudmersive_barcode_api_client.GenerateBarcodeApi(cloudmersive_barcode_api_client.ApiClient(configuration))
value = 'value_example' # str | UPC-A barcode value to generate from
width = 56 # int | Optional: width of the barcode in pixels.  Minimum value of 10. (optional)
height = 56 # int | Optional: width of the barcode in pixels.  Minimum value of 10. (optional)
include_label = true # bool | Optional: show text label on the image of the barcode value, default is true. (optional)

try:
    # Generate a UPC-A code barcode as PNG file
    api_response = api_instance.generate_barcode_upca(value, width=width, height=height, include_label=include_label)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling GenerateBarcodeApi->generate_barcode_upca: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **value** | **str**| UPC-A barcode value to generate from | 
 **width** | **int**| Optional: width of the barcode in pixels.  Minimum value of 10. | [optional] 
 **height** | **int**| Optional: width of the barcode in pixels.  Minimum value of 10. | [optional] 
 **include_label** | **bool**| Optional: show text label on the image of the barcode value, default is true. | [optional] 

### Return type

**str**

### Authorization

[Apikey](../README.md#Apikey)

### HTTP request headers

 - **Content-Type**: application/json, text/json, application/xml, text/xml, application/x-www-form-urlencoded
 - **Accept**: application/octet-stream

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **generate_barcode_upce**
> str generate_barcode_upce(value, width=width, height=height, include_label=include_label)

Generate a UPC-E code barcode as PNG file

Validates and generate a UPC-E barcode as a PNG file, a type of 1D barcode

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
api_instance = cloudmersive_barcode_api_client.GenerateBarcodeApi(cloudmersive_barcode_api_client.ApiClient(configuration))
value = 'value_example' # str | UPC-E barcode value to generate from
width = 56 # int | Optional: width of the barcode in pixels.  Minimum value of 10. (optional)
height = 56 # int | Optional: width of the barcode in pixels.  Minimum value of 10. (optional)
include_label = true # bool | Optional: show text label on the image of the barcode value, default is true. (optional)

try:
    # Generate a UPC-E code barcode as PNG file
    api_response = api_instance.generate_barcode_upce(value, width=width, height=height, include_label=include_label)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling GenerateBarcodeApi->generate_barcode_upce: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **value** | **str**| UPC-E barcode value to generate from | 
 **width** | **int**| Optional: width of the barcode in pixels.  Minimum value of 10. | [optional] 
 **height** | **int**| Optional: width of the barcode in pixels.  Minimum value of 10. | [optional] 
 **include_label** | **bool**| Optional: show text label on the image of the barcode value, default is true. | [optional] 

### Return type

**str**

### Authorization

[Apikey](../README.md#Apikey)

### HTTP request headers

 - **Content-Type**: application/json, text/json, application/xml, text/xml, application/x-www-form-urlencoded
 - **Accept**: application/octet-stream

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

