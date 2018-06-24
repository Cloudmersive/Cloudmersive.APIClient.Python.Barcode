# coding: utf-8

"""
    barcodeapi

    Barcode APIs let you generate barcode images, and recognize values from images of barcodes.  # noqa: E501

    OpenAPI spec version: v1
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six

from cloudmersive_barcode_api_client.models.product_match import ProductMatch  # noqa: F401,E501


class BarcodeLookupResponse(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'successful': 'bool',
        'matches': 'list[ProductMatch]'
    }

    attribute_map = {
        'successful': 'Successful',
        'matches': 'Matches'
    }

    def __init__(self, successful=None, matches=None):  # noqa: E501
        """BarcodeLookupResponse - a model defined in Swagger"""  # noqa: E501

        self._successful = None
        self._matches = None
        self.discriminator = None

        if successful is not None:
            self.successful = successful
        if matches is not None:
            self.matches = matches

    @property
    def successful(self):
        """Gets the successful of this BarcodeLookupResponse.  # noqa: E501


        :return: The successful of this BarcodeLookupResponse.  # noqa: E501
        :rtype: bool
        """
        return self._successful

    @successful.setter
    def successful(self, successful):
        """Sets the successful of this BarcodeLookupResponse.


        :param successful: The successful of this BarcodeLookupResponse.  # noqa: E501
        :type: bool
        """

        self._successful = successful

    @property
    def matches(self):
        """Gets the matches of this BarcodeLookupResponse.  # noqa: E501


        :return: The matches of this BarcodeLookupResponse.  # noqa: E501
        :rtype: list[ProductMatch]
        """
        return self._matches

    @matches.setter
    def matches(self, matches):
        """Sets the matches of this BarcodeLookupResponse.


        :param matches: The matches of this BarcodeLookupResponse.  # noqa: E501
        :type: list[ProductMatch]
        """

        self._matches = matches

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, BarcodeLookupResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
