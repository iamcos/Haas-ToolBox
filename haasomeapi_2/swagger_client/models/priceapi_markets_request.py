# coding: utf-8

"""
    Haasbot LocalAPI

    This is a rest api swagger for the Haasbot.  # noqa: E501

    OpenAPI spec version: 1.0.0
    Contact: support@haasonline.com
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six

class PriceapiMarketsRequest(object):
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
        'pricesource': 'str'
    }

    attribute_map = {
        'pricesource': 'pricesource'
    }

    def __init__(self, pricesource=None):  # noqa: E501
        """PriceapiMarketsRequest - a model defined in Swagger"""  # noqa: E501
        self._pricesource = None
        self.discriminator = None
        self.pricesource = pricesource

    @property
    def pricesource(self):
        """Gets the pricesource of this PriceapiMarketsRequest.  # noqa: E501

        The code of the pricesource, eg; BITFINEX  # noqa: E501

        :return: The pricesource of this PriceapiMarketsRequest.  # noqa: E501
        :rtype: str
        """
        return self._pricesource

    @pricesource.setter
    def pricesource(self, pricesource):
        """Sets the pricesource of this PriceapiMarketsRequest.

        The code of the pricesource, eg; BITFINEX  # noqa: E501

        :param pricesource: The pricesource of this PriceapiMarketsRequest.  # noqa: E501
        :type: str
        """
        if pricesource is None:
            raise ValueError("Invalid value for `pricesource`, must not be `None`")  # noqa: E501

        self._pricesource = pricesource

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
        if issubclass(PriceapiMarketsRequest, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, PriceapiMarketsRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
