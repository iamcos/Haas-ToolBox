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

class AccountapiGetLeverageSettingsResponse(object):
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
        'long_leverage': 'float',
        'short_leverage': 'float',
        'margin_mode': 'object'
    }

    attribute_map = {
        'long_leverage': 'LongLeverage',
        'short_leverage': 'ShortLeverage',
        'margin_mode': 'MarginMode'
    }

    def __init__(self, long_leverage=None, short_leverage=None, margin_mode=None):  # noqa: E501
        """AccountapiGetLeverageSettingsResponse - a model defined in Swagger"""  # noqa: E501
        self._long_leverage = None
        self._short_leverage = None
        self._margin_mode = None
        self.discriminator = None
        if long_leverage is not None:
            self.long_leverage = long_leverage
        if short_leverage is not None:
            self.short_leverage = short_leverage
        if margin_mode is not None:
            self.margin_mode = margin_mode

    @property
    def long_leverage(self):
        """Gets the long_leverage of this AccountapiGetLeverageSettingsResponse.  # noqa: E501


        :return: The long_leverage of this AccountapiGetLeverageSettingsResponse.  # noqa: E501
        :rtype: float
        """
        return self._long_leverage

    @long_leverage.setter
    def long_leverage(self, long_leverage):
        """Sets the long_leverage of this AccountapiGetLeverageSettingsResponse.


        :param long_leverage: The long_leverage of this AccountapiGetLeverageSettingsResponse.  # noqa: E501
        :type: float
        """

        self._long_leverage = long_leverage

    @property
    def short_leverage(self):
        """Gets the short_leverage of this AccountapiGetLeverageSettingsResponse.  # noqa: E501


        :return: The short_leverage of this AccountapiGetLeverageSettingsResponse.  # noqa: E501
        :rtype: float
        """
        return self._short_leverage

    @short_leverage.setter
    def short_leverage(self, short_leverage):
        """Sets the short_leverage of this AccountapiGetLeverageSettingsResponse.


        :param short_leverage: The short_leverage of this AccountapiGetLeverageSettingsResponse.  # noqa: E501
        :type: float
        """

        self._short_leverage = short_leverage

    @property
    def margin_mode(self):
        """Gets the margin_mode of this AccountapiGetLeverageSettingsResponse.  # noqa: E501


        :return: The margin_mode of this AccountapiGetLeverageSettingsResponse.  # noqa: E501
        :rtype: object
        """
        return self._margin_mode

    @margin_mode.setter
    def margin_mode(self, margin_mode):
        """Sets the margin_mode of this AccountapiGetLeverageSettingsResponse.


        :param margin_mode: The margin_mode of this AccountapiGetLeverageSettingsResponse.  # noqa: E501
        :type: object
        """

        self._margin_mode = margin_mode

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
        if issubclass(AccountapiGetLeverageSettingsResponse, dict):
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
        if not isinstance(other, AccountapiGetLeverageSettingsResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
