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

class PortfolioapiGetPortfolioAccountChartRequest(object):
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
        'userid': 'str',
        'interfacekey': 'str',
        'currency': 'str',
        'interval': 'int',
        'style': 'object'
    }

    attribute_map = {
        'userid': 'userid',
        'interfacekey': 'interfacekey',
        'currency': 'currency',
        'interval': 'interval',
        'style': 'style'
    }

    def __init__(self, userid=None, interfacekey=None, currency=None, interval=None, style=None):  # noqa: E501
        """PortfolioapiGetPortfolioAccountChartRequest - a model defined in Swagger"""  # noqa: E501
        self._userid = None
        self._interfacekey = None
        self._currency = None
        self._interval = None
        self._style = None
        self.discriminator = None
        self.userid = userid
        self.interfacekey = interfacekey
        self.currency = currency
        self.interval = interval
        self.style = style

    @property
    def userid(self):
        """Gets the userid of this PortfolioapiGetPortfolioAccountChartRequest.  # noqa: E501

        The userid as obtained at the login  # noqa: E501

        :return: The userid of this PortfolioapiGetPortfolioAccountChartRequest.  # noqa: E501
        :rtype: str
        """
        return self._userid

    @userid.setter
    def userid(self, userid):
        """Sets the userid of this PortfolioapiGetPortfolioAccountChartRequest.

        The userid as obtained at the login  # noqa: E501

        :param userid: The userid of this PortfolioapiGetPortfolioAccountChartRequest.  # noqa: E501
        :type: str
        """
        if userid is None:
            raise ValueError("Invalid value for `userid`, must not be `None`")  # noqa: E501

        self._userid = userid

    @property
    def interfacekey(self):
        """Gets the interfacekey of this PortfolioapiGetPortfolioAccountChartRequest.  # noqa: E501

        The interfacekey as generated at login  # noqa: E501

        :return: The interfacekey of this PortfolioapiGetPortfolioAccountChartRequest.  # noqa: E501
        :rtype: str
        """
        return self._interfacekey

    @interfacekey.setter
    def interfacekey(self, interfacekey):
        """Sets the interfacekey of this PortfolioapiGetPortfolioAccountChartRequest.

        The interfacekey as generated at login  # noqa: E501

        :param interfacekey: The interfacekey of this PortfolioapiGetPortfolioAccountChartRequest.  # noqa: E501
        :type: str
        """
        if interfacekey is None:
            raise ValueError("Invalid value for `interfacekey`, must not be `None`")  # noqa: E501

        self._interfacekey = interfacekey

    @property
    def currency(self):
        """Gets the currency of this PortfolioapiGetPortfolioAccountChartRequest.  # noqa: E501

        The code of the currency, eg; BTC  # noqa: E501

        :return: The currency of this PortfolioapiGetPortfolioAccountChartRequest.  # noqa: E501
        :rtype: str
        """
        return self._currency

    @currency.setter
    def currency(self, currency):
        """Sets the currency of this PortfolioapiGetPortfolioAccountChartRequest.

        The code of the currency, eg; BTC  # noqa: E501

        :param currency: The currency of this PortfolioapiGetPortfolioAccountChartRequest.  # noqa: E501
        :type: str
        """
        if currency is None:
            raise ValueError("Invalid value for `currency`, must not be `None`")  # noqa: E501

        self._currency = currency

    @property
    def interval(self):
        """Gets the interval of this PortfolioapiGetPortfolioAccountChartRequest.  # noqa: E501


        :return: The interval of this PortfolioapiGetPortfolioAccountChartRequest.  # noqa: E501
        :rtype: int
        """
        return self._interval

    @interval.setter
    def interval(self, interval):
        """Sets the interval of this PortfolioapiGetPortfolioAccountChartRequest.


        :param interval: The interval of this PortfolioapiGetPortfolioAccountChartRequest.  # noqa: E501
        :type: int
        """
        if interval is None:
            raise ValueError("Invalid value for `interval`, must not be `None`")  # noqa: E501

        self._interval = interval

    @property
    def style(self):
        """Gets the style of this PortfolioapiGetPortfolioAccountChartRequest.  # noqa: E501


        :return: The style of this PortfolioapiGetPortfolioAccountChartRequest.  # noqa: E501
        :rtype: object
        """
        return self._style

    @style.setter
    def style(self, style):
        """Sets the style of this PortfolioapiGetPortfolioAccountChartRequest.


        :param style: The style of this PortfolioapiGetPortfolioAccountChartRequest.  # noqa: E501
        :type: object
        """
        if style is None:
            raise ValueError("Invalid value for `style`, must not be `None`")  # noqa: E501

        self._style = style

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
        if issubclass(PortfolioapiGetPortfolioAccountChartRequest, dict):
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
        if not isinstance(other, PortfolioapiGetPortfolioAccountChartRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
