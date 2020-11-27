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

class InterfaceapiMarketTaInfoResponse(object):
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
        'timestamp': 'int',
        'market': 'str',
        'trend_indicators': 'object',
        'side_ways_indicators': 'object'
    }

    attribute_map = {
        'timestamp': 'Timestamp',
        'market': 'Market',
        'trend_indicators': 'TrendIndicators',
        'side_ways_indicators': 'SideWaysIndicators'
    }

    def __init__(self, timestamp=None, market=None, trend_indicators=None, side_ways_indicators=None):  # noqa: E501
        """InterfaceapiMarketTaInfoResponse - a model defined in Swagger"""  # noqa: E501
        self._timestamp = None
        self._market = None
        self._trend_indicators = None
        self._side_ways_indicators = None
        self.discriminator = None
        if timestamp is not None:
            self.timestamp = timestamp
        if market is not None:
            self.market = market
        if trend_indicators is not None:
            self.trend_indicators = trend_indicators
        if side_ways_indicators is not None:
            self.side_ways_indicators = side_ways_indicators

    @property
    def timestamp(self):
        """Gets the timestamp of this InterfaceapiMarketTaInfoResponse.  # noqa: E501


        :return: The timestamp of this InterfaceapiMarketTaInfoResponse.  # noqa: E501
        :rtype: int
        """
        return self._timestamp

    @timestamp.setter
    def timestamp(self, timestamp):
        """Sets the timestamp of this InterfaceapiMarketTaInfoResponse.


        :param timestamp: The timestamp of this InterfaceapiMarketTaInfoResponse.  # noqa: E501
        :type: int
        """

        self._timestamp = timestamp

    @property
    def market(self):
        """Gets the market of this InterfaceapiMarketTaInfoResponse.  # noqa: E501


        :return: The market of this InterfaceapiMarketTaInfoResponse.  # noqa: E501
        :rtype: str
        """
        return self._market

    @market.setter
    def market(self, market):
        """Sets the market of this InterfaceapiMarketTaInfoResponse.


        :param market: The market of this InterfaceapiMarketTaInfoResponse.  # noqa: E501
        :type: str
        """

        self._market = market

    @property
    def trend_indicators(self):
        """Gets the trend_indicators of this InterfaceapiMarketTaInfoResponse.  # noqa: E501


        :return: The trend_indicators of this InterfaceapiMarketTaInfoResponse.  # noqa: E501
        :rtype: object
        """
        return self._trend_indicators

    @trend_indicators.setter
    def trend_indicators(self, trend_indicators):
        """Sets the trend_indicators of this InterfaceapiMarketTaInfoResponse.


        :param trend_indicators: The trend_indicators of this InterfaceapiMarketTaInfoResponse.  # noqa: E501
        :type: object
        """

        self._trend_indicators = trend_indicators

    @property
    def side_ways_indicators(self):
        """Gets the side_ways_indicators of this InterfaceapiMarketTaInfoResponse.  # noqa: E501


        :return: The side_ways_indicators of this InterfaceapiMarketTaInfoResponse.  # noqa: E501
        :rtype: object
        """
        return self._side_ways_indicators

    @side_ways_indicators.setter
    def side_ways_indicators(self, side_ways_indicators):
        """Sets the side_ways_indicators of this InterfaceapiMarketTaInfoResponse.


        :param side_ways_indicators: The side_ways_indicators of this InterfaceapiMarketTaInfoResponse.  # noqa: E501
        :type: object
        """

        self._side_ways_indicators = side_ways_indicators

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
        if issubclass(InterfaceapiMarketTaInfoResponse, dict):
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
        if not isinstance(other, InterfaceapiMarketTaInfoResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
