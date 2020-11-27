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

class PriceapiOrderbookResponse(object):
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
        'ask': 'object',
        'bid': 'object'
    }

    attribute_map = {
        'ask': 'Ask',
        'bid': 'Bid'
    }

    def __init__(self, ask=None, bid=None):  # noqa: E501
        """PriceapiOrderbookResponse - a model defined in Swagger"""  # noqa: E501
        self._ask = None
        self._bid = None
        self.discriminator = None
        if ask is not None:
            self.ask = ask
        if bid is not None:
            self.bid = bid

    @property
    def ask(self):
        """Gets the ask of this PriceapiOrderbookResponse.  # noqa: E501


        :return: The ask of this PriceapiOrderbookResponse.  # noqa: E501
        :rtype: object
        """
        return self._ask

    @ask.setter
    def ask(self, ask):
        """Sets the ask of this PriceapiOrderbookResponse.


        :param ask: The ask of this PriceapiOrderbookResponse.  # noqa: E501
        :type: object
        """

        self._ask = ask

    @property
    def bid(self):
        """Gets the bid of this PriceapiOrderbookResponse.  # noqa: E501


        :return: The bid of this PriceapiOrderbookResponse.  # noqa: E501
        :rtype: object
        """
        return self._bid

    @bid.setter
    def bid(self, bid):
        """Sets the bid of this PriceapiOrderbookResponse.


        :param bid: The bid of this PriceapiOrderbookResponse.  # noqa: E501
        :type: object
        """

        self._bid = bid

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
        if issubclass(PriceapiOrderbookResponse, dict):
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
        if not isinstance(other, PriceapiOrderbookResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
