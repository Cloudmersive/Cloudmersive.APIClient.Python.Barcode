# cloudmersive_barcode_api_client
Barcode APIs let you generate barcode images, and recognize values from images of barcodes.

This Python package provides a native API client for [Cloudmersive Barcode API](https://www.cloudmersive.com/barcode-api)

- API version: v1
- Package version: 3.2.0
- Build package: io.swagger.codegen.languages.PythonClientCodegen

## Requirements.

Python 2.7 and 3.4+

## Installation & Usage
### pip install

If the python package is hosted on Github, you can install directly from Github

```sh
pip install git+https://github.com/GIT_USER_ID/GIT_REPO_ID.git
```
(you may need to run `pip` with root permission: `sudo pip install git+https://github.com/GIT_USER_ID/GIT_REPO_ID.git`)

Then import the package:
```python
import cloudmersive_barcode_api_client 
```

### Setuptools

Install via [Setuptools](http://pypi.python.org/pypi/setuptools).

```sh
python setup.py install --user
```
(or `sudo python setup.py install` to install the package for all users)

Then import the package:
```python
import cloudmersive_barcode_api_client
```

## Getting Started

Please follow the [installation procedure](#installation--usage) and then run the following:

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

## Documentation for API Endpoints

All URIs are relative to *https://api.cloudmersive.com*

Class | Method | HTTP request | Description
------------ | ------------- | ------------- | -------------
*BarcodeLookupApi* | [**barcode_lookup_ean_lookup**](docs/BarcodeLookupApi.md#barcode_lookup_ean_lookup) | **POST** /barcode/lookup/ean | Lookup EAN barcode value, return product data
*BarcodeScanApi* | [**barcode_scan_image**](docs/BarcodeScanApi.md#barcode_scan_image) | **POST** /barcode/scan/image | Scan and recognize an image of a barcode
*BarcodeScanApi* | [**barcode_scan_image_advanced**](docs/BarcodeScanApi.md#barcode_scan_image_advanced) | **POST** /barcode/scan/image/advanced | Advanced AI scan and recognition of an image of one or more barcodes of any type
*BarcodeScanApi* | [**barcode_scan_image_advanced_qr**](docs/BarcodeScanApi.md#barcode_scan_image_advanced_qr) | **POST** /barcode/scan/image/advanced/qr | Advanced AI scan and recognition of an image of one or more QR barcodes
*GenerateBarcodeApi* | [**generate_barcode_code128**](docs/GenerateBarcodeApi.md#generate_barcode_code128) | **POST** /barcode/generate/code-128 | Generate a EAN-13 code barcode as PNG file
*GenerateBarcodeApi* | [**generate_barcode_ean13**](docs/GenerateBarcodeApi.md#generate_barcode_ean13) | **POST** /barcode/generate/ean-13 | Generate a EAN-13 code barcode as PNG file
*GenerateBarcodeApi* | [**generate_barcode_ean8**](docs/GenerateBarcodeApi.md#generate_barcode_ean8) | **POST** /barcode/generate/ean-8 | Generate a EAN-8 code barcode as PNG file
*GenerateBarcodeApi* | [**generate_barcode_qr_code**](docs/GenerateBarcodeApi.md#generate_barcode_qr_code) | **POST** /barcode/generate/qrcode | Generate a QR code barcode as PNG file
*GenerateBarcodeApi* | [**generate_barcode_upca**](docs/GenerateBarcodeApi.md#generate_barcode_upca) | **POST** /barcode/generate/upc-a | Generate a UPC-A code barcode as PNG file
*GenerateBarcodeApi* | [**generate_barcode_upce**](docs/GenerateBarcodeApi.md#generate_barcode_upce) | **POST** /barcode/generate/upc-e | Generate a UPC-E code barcode as PNG file


## Documentation For Models

 - [BarcodeAdvancedResultItem](docs/BarcodeAdvancedResultItem.md)
 - [BarcodeAdvancedScanResult](docs/BarcodeAdvancedScanResult.md)
 - [BarcodeLookupResponse](docs/BarcodeLookupResponse.md)
 - [BarcodeQRResultItem](docs/BarcodeQRResultItem.md)
 - [BarcodeScanQRAdvancedResult](docs/BarcodeScanQRAdvancedResult.md)
 - [BarcodeScanResult](docs/BarcodeScanResult.md)
 - [ProductMatch](docs/ProductMatch.md)


## Documentation For Authorization


## Apikey

- **Type**: API key
- **API key parameter name**: Apikey
- **Location**: HTTP header


## Author



