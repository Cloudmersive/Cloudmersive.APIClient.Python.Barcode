# cloudmersive_barcode_api_client
Barcode APIs let you generate barcode images, and recognize values from images of barcodes.

This Python package provides a native API client for [Cloudmersive Barcode API](https://www.cloudmersive.com/barcode-api)

- API version: v1
- Package version: 2.0.3
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
    # Lookup a barcode value and return product data
    api_response = api_instance.barcode_lookup_ean_lookup(value)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BarcodeLookupApi->barcode_lookup_ean_lookup: %s\n" % e)

```

## Documentation for API Endpoints

All URIs are relative to *https://api.cloudmersive.com*

Class | Method | HTTP request | Description
------------ | ------------- | ------------- | -------------
*BarcodeLookupApi* | [**barcode_lookup_ean_lookup**](docs/BarcodeLookupApi.md#barcode_lookup_ean_lookup) | **POST** /barcode/lookup/ean | Lookup a barcode value and return product data
*BarcodeScanApi* | [**barcode_scan_image**](docs/BarcodeScanApi.md#barcode_scan_image) | **POST** /barcode/scan/image | Scan an image for a barcode and turn the result.  Supported barcode types include AZTEC, CODABAR, CODE_39, CODE_93, CODE_128, DATA_MATRIX, EAN_8, EAN_13, ITF, MAXICODE, PDF_417, QR_CODE, RSS_14, RSS_EXPANDED, UPC_A, UPC_E, All_1D, UPC_EAN_EXTENSION, MSI, PLESSEY, IMB
*GenerateBarcodeApi* | [**generate_barcode_ean13**](docs/GenerateBarcodeApi.md#generate_barcode_ean13) | **POST** /barcode/generate/ean-13 | Validates and generate a EAN-13 barcode as a PNG file, a type of 1D barcode
*GenerateBarcodeApi* | [**generate_barcode_ean8**](docs/GenerateBarcodeApi.md#generate_barcode_ean8) | **POST** /barcode/generate/ean-8 | Validates and generate a EAN-8 barcode as a PNG file, a type of 1D barcode
*GenerateBarcodeApi* | [**generate_barcode_qr_code**](docs/GenerateBarcodeApi.md#generate_barcode_qr_code) | **POST** /barcode/generate/qrcode | Generate a QR code barcode as a PNG file, a type of 2D barcode which can encode free-form text information
*GenerateBarcodeApi* | [**generate_barcode_upca**](docs/GenerateBarcodeApi.md#generate_barcode_upca) | **POST** /barcode/generate/upc-a | Validate and generate a UPC-A barcode as a PNG file, a type of 1D barcode
*GenerateBarcodeApi* | [**generate_barcode_upce**](docs/GenerateBarcodeApi.md#generate_barcode_upce) | **POST** /barcode/generate/upc-e | Validates and generate a UPC-E barcode as a PNG file, a type of 1D barcode


## Documentation For Models

 - [BarcodeLookupResponse](docs/BarcodeLookupResponse.md)
 - [BarcodeScanResult](docs/BarcodeScanResult.md)
 - [ProductMatch](docs/ProductMatch.md)


## Documentation For Authorization


## Apikey

- **Type**: API key
- **API key parameter name**: Apikey
- **Location**: HTTP header


## Author



