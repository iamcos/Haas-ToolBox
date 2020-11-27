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

class PortfolioapiGetCurrencyChartResponse(object):
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
        'guid': 'str',
        'interval': 'int',
        'status': 'object',
        'charts': 'object',
        'colors': 'object'
    }

    attribute_map = {
        'guid': 'Guid',
        'interval': 'Interval',
        'status': 'Status',
        'charts': 'Charts',
        'colors': 'Colors'
    }

    def __init__(self, guid=None, interval=None, status=None, charts=None, colors=None):  # noqa: E501
        """PortfolioapiGetCurrencyChartResponse - a model defined in Swagger"""  # noqa: E501
        self._guid = None
        self._interval = None
        self._status = None
        self._charts = None
        self._colors = None
        self.discriminator = None
        if guid is not None:
            self.guid = guid
        if interval is not None:
            self.interval = interval
        if status is not None:
            self.status = status
        if charts is not None:
            self.charts = charts
        if colors is not None:
            self.colors = colors

    @property
    def guid(self):
        """Gets the guid of this PortfolioapiGetCurrencyChartResponse.  # noqa: E501


        :return: The guid of this PortfolioapiGetCurrencyChartResponse.  # noqa: E501
        :rtype: str
        """
        return self._guid

    @guid.setter
    def guid(self, guid):
        """Sets the guid of this PortfolioapiGetCurrencyChartResponse.


        :param guid: The guid of this PortfolioapiGetCurrencyChartResponse.  # noqa: E501
        :type: str
        """

        self._guid = guid

    @property
    def interval(self):
        """Gets the interval of this PortfolioapiGetCurrencyChartResponse.  # noqa: E501


        :return: The interval of this PortfolioapiGetCurrencyChartResponse.  # noqa: E501
        :rtype: int
        """
        return self._interval

    @interval.setter
    def interval(self, interval):
        """Sets the interval of this PortfolioapiGetCurrencyChartResponse.


        :param interval: The interval of this PortfolioapiGetCurrencyChartResponse.  # noqa: E501
        :type: int
        """

        self._interval = interval

    @property
    def status(self):
        """Gets the status of this PortfolioapiGetCurrencyChartResponse.  # noqa: E501


        :return: The status of this PortfolioapiGetCurrencyChartResponse.  # noqa: E501
        :rtype: object
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this PortfolioapiGetCurrencyChartResponse.


        :param status: The status of this PortfolioapiGetCurrencyChartResponse.  # noqa: E501
        :type: object
        """

        self._status = status

    @property
    def charts(self):
        """Gets the charts of this PortfolioapiGetCurrencyChartResponse.  # noqa: E501


        :return: The charts of this PortfolioapiGetCurrencyChartResponse.  # noqa: E501
        :rtype: object
        """
        return self._charts

    @charts.setter
    def charts(self, charts):
        """Sets the charts of this PortfolioapiGetCurrencyChartResponse.


        :param charts: The charts of this PortfolioapiGetCurrencyChartResponse.  # noqa: E501
        :type: object
        """

        self._charts = charts

    @property
    def colors(self):
        """Gets the colors of this PortfolioapiGetCurrencyChartResponse.  # noqa: E501


        :return: The colors of this PortfolioapiGetCurrencyChartResponse.  # noqa: E501
        :rtype: object
        """
        return self._colors

    @colors.setter
    def colors(self, colors):
        """Sets the colors of this PortfolioapiGetCurrencyChartResponse.


        :param colors: The colors of this PortfolioapiGetCurrencyChartResponse.  # noqa: E501
        :type: object
        """

        self._colors = colors

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
        if issubclass(PortfolioapiGetCurrencyChartResponse, dict):
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
        if not isinstance(other, PortfolioapiGetCurrencyChartResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
