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

class PortfolioapiGetCoinBalanceResponse(object):
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
        'currency': 'str',
        'amount': 'float',
        'value': 'float',
        'average_price': 'float',
        'currency_balances': 'object',
        'history': 'object',
        'color': 'str'
    }

    attribute_map = {
        'timestamp': 'Timestamp',
        'currency': 'Currency',
        'amount': 'Amount',
        'value': 'Value',
        'average_price': 'AveragePrice',
        'currency_balances': 'CurrencyBalances',
        'history': 'History',
        'color': 'Color'
    }

    def __init__(self, timestamp=None, currency=None, amount=None, value=None, average_price=None, currency_balances=None, history=None, color=None):  # noqa: E501
        """PortfolioapiGetCoinBalanceResponse - a model defined in Swagger"""  # noqa: E501
        self._timestamp = None
        self._currency = None
        self._amount = None
        self._value = None
        self._average_price = None
        self._currency_balances = None
        self._history = None
        self._color = None
        self.discriminator = None
        if timestamp is not None:
            self.timestamp = timestamp
        if currency is not None:
            self.currency = currency
        if amount is not None:
            self.amount = amount
        if value is not None:
            self.value = value
        if average_price is not None:
            self.average_price = average_price
        if currency_balances is not None:
            self.currency_balances = currency_balances
        if history is not None:
            self.history = history
        if color is not None:
            self.color = color

    @property
    def timestamp(self):
        """Gets the timestamp of this PortfolioapiGetCoinBalanceResponse.  # noqa: E501


        :return: The timestamp of this PortfolioapiGetCoinBalanceResponse.  # noqa: E501
        :rtype: int
        """
        return self._timestamp

    @timestamp.setter
    def timestamp(self, timestamp):
        """Sets the timestamp of this PortfolioapiGetCoinBalanceResponse.


        :param timestamp: The timestamp of this PortfolioapiGetCoinBalanceResponse.  # noqa: E501
        :type: int
        """

        self._timestamp = timestamp

    @property
    def currency(self):
        """Gets the currency of this PortfolioapiGetCoinBalanceResponse.  # noqa: E501


        :return: The currency of this PortfolioapiGetCoinBalanceResponse.  # noqa: E501
        :rtype: str
        """
        return self._currency

    @currency.setter
    def currency(self, currency):
        """Sets the currency of this PortfolioapiGetCoinBalanceResponse.


        :param currency: The currency of this PortfolioapiGetCoinBalanceResponse.  # noqa: E501
        :type: str
        """

        self._currency = currency

    @property
    def amount(self):
        """Gets the amount of this PortfolioapiGetCoinBalanceResponse.  # noqa: E501


        :return: The amount of this PortfolioapiGetCoinBalanceResponse.  # noqa: E501
        :rtype: float
        """
        return self._amount

    @amount.setter
    def amount(self, amount):
        """Sets the amount of this PortfolioapiGetCoinBalanceResponse.


        :param amount: The amount of this PortfolioapiGetCoinBalanceResponse.  # noqa: E501
        :type: float
        """

        self._amount = amount

    @property
    def value(self):
        """Gets the value of this PortfolioapiGetCoinBalanceResponse.  # noqa: E501


        :return: The value of this PortfolioapiGetCoinBalanceResponse.  # noqa: E501
        :rtype: float
        """
        return self._value

    @value.setter
    def value(self, value):
        """Sets the value of this PortfolioapiGetCoinBalanceResponse.


        :param value: The value of this PortfolioapiGetCoinBalanceResponse.  # noqa: E501
        :type: float
        """

        self._value = value

    @property
    def average_price(self):
        """Gets the average_price of this PortfolioapiGetCoinBalanceResponse.  # noqa: E501


        :return: The average_price of this PortfolioapiGetCoinBalanceResponse.  # noqa: E501
        :rtype: float
        """
        return self._average_price

    @average_price.setter
    def average_price(self, average_price):
        """Sets the average_price of this PortfolioapiGetCoinBalanceResponse.


        :param average_price: The average_price of this PortfolioapiGetCoinBalanceResponse.  # noqa: E501
        :type: float
        """

        self._average_price = average_price

    @property
    def currency_balances(self):
        """Gets the currency_balances of this PortfolioapiGetCoinBalanceResponse.  # noqa: E501


        :return: The currency_balances of this PortfolioapiGetCoinBalanceResponse.  # noqa: E501
        :rtype: object
        """
        return self._currency_balances

    @currency_balances.setter
    def currency_balances(self, currency_balances):
        """Sets the currency_balances of this PortfolioapiGetCoinBalanceResponse.


        :param currency_balances: The currency_balances of this PortfolioapiGetCoinBalanceResponse.  # noqa: E501
        :type: object
        """

        self._currency_balances = currency_balances

    @property
    def history(self):
        """Gets the history of this PortfolioapiGetCoinBalanceResponse.  # noqa: E501


        :return: The history of this PortfolioapiGetCoinBalanceResponse.  # noqa: E501
        :rtype: object
        """
        return self._history

    @history.setter
    def history(self, history):
        """Sets the history of this PortfolioapiGetCoinBalanceResponse.


        :param history: The history of this PortfolioapiGetCoinBalanceResponse.  # noqa: E501
        :type: object
        """

        self._history = history

    @property
    def color(self):
        """Gets the color of this PortfolioapiGetCoinBalanceResponse.  # noqa: E501


        :return: The color of this PortfolioapiGetCoinBalanceResponse.  # noqa: E501
        :rtype: str
        """
        return self._color

    @color.setter
    def color(self, color):
        """Sets the color of this PortfolioapiGetCoinBalanceResponse.


        :param color: The color of this PortfolioapiGetCoinBalanceResponse.  # noqa: E501
        :type: str
        """

        self._color = color

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
        if issubclass(PortfolioapiGetCoinBalanceResponse, dict):
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
        if not isinstance(other, PortfolioapiGetCoinBalanceResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
