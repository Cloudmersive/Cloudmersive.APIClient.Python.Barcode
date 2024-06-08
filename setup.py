# coding: utf-8

"""
    barcodeapi

    

    OpenAPI spec version: v1
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from setuptools import setup, find_packages  # noqa: H301

NAME = "cloudmersive_barcode_api_client"
VERSION = "3.1.0"
# To install the library, run the following
#
# python setup.py install
#
# prerequisite: setuptools
from os import path
this_directory = path.abspath(path.dirname(__file__))
with open(path.join(this_directory, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

REQUIRES = [
    "certifi>=2017.4.17",
    "python-dateutil>=2.1",
    "six>=1.10",
    "urllib3>=1.23"
]
    

setup(
    name=NAME,
    version=VERSION,
    description="barcodeapi",
    author_email="",
    url="https://www.cloudmersive.com/barcode-api",
    keywords=["Swagger", "barcodeapi"],
    install_requires=REQUIRES,
    packages=find_packages(),
    include_package_data=True,
    long_description=long_description,
    long_description_content_type='text/markdown'
    

)
