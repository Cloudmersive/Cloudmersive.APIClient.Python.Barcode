# cloudmersive_barcode_api_client.BarcodeScanApi

All URIs are relative to *https://api.cloudmersive.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**barcode_scan_image**](BarcodeScanApi.md#barcode_scan_image) | **POST** /barcode/scan/image | Scan and recognize an image of a barcode
[**barcode_scan_image_advanced**](BarcodeScanApi.md#barcode_scan_image_advanced) | **POST** /barcode/scan/image/advanced | Advanced AI scan and recognition of an image of one or more barcodes of any type
[**barcode_scan_image_advanced_qr**](BarcodeScanApi.md#barcode_scan_image_advanced_qr) | **POST** /barcode/scan/image/advanced/qr | Advanced AI scan and recognition of an image of one or more QR barcodes


# **barcode_scan_image**
> BarcodeScanResult barcode_scan_image(image_file)

Scan and recognize an image of a barcode

Scan an image or photo of a barcode and return the result.  Supported barcode types include AZTEC, CODABAR, CODE_39, CODE_93, CODE_128, DATA_MATRIX, EAN_8, EAN_13, ITF, MAXICODE, PDF_417, QR_CODE, RSS_14, RSS_EXPANDED, UPC_A, UPC_E, All_1D, UPC_EAN_EXTENSION, MSI, PLESSEY, IMB

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
api_instance = cloudmersive_barcode_api_client.BarcodeScanApi(cloudmersive_barcode_api_client.ApiClient(configuration))
image_file = '/path/to/file.txt' # file | Image file to perform the operation on.  Common file formats such as PNG, JPEG are supported.

try:
    # Scan and recognize an image of a barcode
    api_response = api_instance.barcode_scan_image(image_file)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BarcodeScanApi->barcode_scan_image: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **image_file** | **file**| Image file to perform the operation on.  Common file formats such as PNG, JPEG are supported. | 

### Return type

[**BarcodeScanResult**](BarcodeScanResult.md)

### Authorization

[Apikey](../README.md#Apikey)

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: application/json, text/json, application/xml, text/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **barcode_scan_image_advanced**
> BarcodeAdvancedScanResult barcode_scan_image_advanced(image_file)

Advanced AI scan and recognition of an image of one or more barcodes of any type

Scan an image or photo of a barcode and return the result with enhanced accuracy, particularlly for low quality inputs using Advanced AI.  Supported barcode types include AZTEC, CODABAR, CODE_39, CODE_93, CODE_128, DATA_MATRIX, EAN_8, EAN_13, ITF, MAXICODE, PDF_417, QR_CODE, RSS_14, RSS_EXPANDED, UPC_A, UPC_E, All_1D, UPC_EAN_EXTENSION, MSI, PLESSEY, IMB.  Uses large model AI.  Consumes 100 API calls per image page.  For Managed Instance and Private Cloud requires GPU infrastructure.  Supports PNG, PDF and JPEG input file formats.

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
api_instance = cloudmersive_barcode_api_client.BarcodeScanApi(cloudmersive_barcode_api_client.ApiClient(configuration))
image_file = '/path/to/file.txt' # file | Image file to perform the operation on.  Common file formats such as PNG, JPEG are supported.

try:
    # Advanced AI scan and recognition of an image of one or more barcodes of any type
    api_response = api_instance.barcode_scan_image_advanced(image_file)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BarcodeScanApi->barcode_scan_image_advanced: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **image_file** | **file**| Image file to perform the operation on.  Common file formats such as PNG, JPEG are supported. | 

### Return type

[**BarcodeAdvancedScanResult**](BarcodeAdvancedScanResult.md)

### Authorization

[Apikey](../README.md#Apikey)

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: application/json, text/json, application/xml, text/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **barcode_scan_image_advanced_qr**
> BarcodeScanQRAdvancedResult barcode_scan_image_advanced_qr(image_file, preprocessing=preprocessing, recognition_mode=recognition_mode)

Advanced AI scan and recognition of an image of one or more QR barcodes

Scan an image or photo of a QR barcode and return the result.  Uses AI deep learning to read blurry or low resultion QR barcodes.  Supports PNG, PDF and JPEG input file formats.

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
api_instance = cloudmersive_barcode_api_client.BarcodeScanApi(cloudmersive_barcode_api_client.ApiClient(configuration))
image_file = '/path/to/file.txt' # file | Image file to perform the operation on.  Common file formats such as PNG, JPEG are supported.
preprocessing = 'preprocessing_example' # str | Optional, preprocessing mode, default is 'Auto'.  Possible values are None (no preprocessing of the image), and Auto (automatic image enhancement of the image - including automatic unrotation of the image - before OCR is applied; this is recommended).  Set this to 'None' if you do not want to use automatic image unrotation and enhancement. (optional)
recognition_mode = 'recognition_mode_example' # str | Optional, recognitionMode mode, default is 'Advanced'.  Possible values are Advanced, and Advanced2 which provides the most advanced available barcode recognition. (optional)

try:
    # Advanced AI scan and recognition of an image of one or more QR barcodes
    api_response = api_instance.barcode_scan_image_advanced_qr(image_file, preprocessing=preprocessing, recognition_mode=recognition_mode)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BarcodeScanApi->barcode_scan_image_advanced_qr: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **image_file** | **file**| Image file to perform the operation on.  Common file formats such as PNG, JPEG are supported. | 
 **preprocessing** | **str**| Optional, preprocessing mode, default is &#39;Auto&#39;.  Possible values are None (no preprocessing of the image), and Auto (automatic image enhancement of the image - including automatic unrotation of the image - before OCR is applied; this is recommended).  Set this to &#39;None&#39; if you do not want to use automatic image unrotation and enhancement. | [optional] 
 **recognition_mode** | **str**| Optional, recognitionMode mode, default is &#39;Advanced&#39;.  Possible values are Advanced, and Advanced2 which provides the most advanced available barcode recognition. | [optional] 

### Return type

[**BarcodeScanQRAdvancedResult**](BarcodeScanQRAdvancedResult.md)

### Authorization

[Apikey](../README.md#Apikey)

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: application/json, text/json, application/xml, text/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

