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

class BotapiGetChartRequest(object):
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
        'botid': 'str',
        'interval': 'int',
        'style': 'int',
        'showvolume': 'bool',
        'savesettings': 'bool'
    }

    attribute_map = {
        'userid': 'userid',
        'interfacekey': 'interfacekey',
        'botid': 'botid',
        'interval': 'interval',
        'style': 'style',
        'showvolume': 'showvolume',
        'savesettings': 'savesettings'
    }

    def __init__(self, userid=None, interfacekey=None, botid=None, interval=None, style=None, showvolume=None, savesettings=None):  # noqa: E501
        """BotapiGetChartRequest - a model defined in Swagger"""  # noqa: E501
        self._userid = None
        self._interfacekey = None
        self._botid = None
        self._interval = None
        self._style = None
        self._showvolume = None
        self._savesettings = None
        self.discriminator = None
        self.userid = userid
        self.interfacekey = interfacekey
        self.botid = botid
        self.interval = interval
        self.style = style
        self.showvolume = showvolume
        self.savesettings = savesettings

    @property
    def userid(self):
        """Gets the userid of this BotapiGetChartRequest.  # noqa: E501

        The userid as obtained at the login  # noqa: E501

        :return: The userid of this BotapiGetChartRequest.  # noqa: E501
        :rtype: str
        """
        return self._userid

    @userid.setter
    def userid(self, userid):
        """Sets the userid of this BotapiGetChartRequest.

        The userid as obtained at the login  # noqa: E501

        :param userid: The userid of this BotapiGetChartRequest.  # noqa: E501
        :type: str
        """
        if userid is None:
            raise ValueError("Invalid value for `userid`, must not be `None`")  # noqa: E501

        self._userid = userid

    @property
    def interfacekey(self):
        """Gets the interfacekey of this BotapiGetChartRequest.  # noqa: E501

        The interfacekey as generated at login  # noqa: E501

        :return: The interfacekey of this BotapiGetChartRequest.  # noqa: E501
        :rtype: str
        """
        return self._interfacekey

    @interfacekey.setter
    def interfacekey(self, interfacekey):
        """Sets the interfacekey of this BotapiGetChartRequest.

        The interfacekey as generated at login  # noqa: E501

        :param interfacekey: The interfacekey of this BotapiGetChartRequest.  # noqa: E501
        :type: str
        """
        if interfacekey is None:
            raise ValueError("Invalid value for `interfacekey`, must not be `None`")  # noqa: E501

        self._interfacekey = interfacekey

    @property
    def botid(self):
        """Gets the botid of this BotapiGetChartRequest.  # noqa: E501

        Bot identifier  # noqa: E501

        :return: The botid of this BotapiGetChartRequest.  # noqa: E501
        :rtype: str
        """
        return self._botid

    @botid.setter
    def botid(self, botid):
        """Sets the botid of this BotapiGetChartRequest.

        Bot identifier  # noqa: E501

        :param botid: The botid of this BotapiGetChartRequest.  # noqa: E501
        :type: str
        """
        if botid is None:
            raise ValueError("Invalid value for `botid`, must not be `None`")  # noqa: E501

        self._botid = botid

    @property
    def interval(self):
        """Gets the interval of this BotapiGetChartRequest.  # noqa: E501


        :return: The interval of this BotapiGetChartRequest.  # noqa: E501
        :rtype: int
        """
        return self._interval

    @interval.setter
    def interval(self, interval):
        """Sets the interval of this BotapiGetChartRequest.


        :param interval: The interval of this BotapiGetChartRequest.  # noqa: E501
        :type: int
        """
        if interval is None:
            raise ValueError("Invalid value for `interval`, must not be `None`")  # noqa: E501

        self._interval = interval

    @property
    def style(self):
        """Gets the style of this BotapiGetChartRequest.  # noqa: E501


        :return: The style of this BotapiGetChartRequest.  # noqa: E501
        :rtype: int
        """
        return self._style

    @style.setter
    def style(self, style):
        """Sets the style of this BotapiGetChartRequest.


        :param style: The style of this BotapiGetChartRequest.  # noqa: E501
        :type: int
        """
        if style is None:
            raise ValueError("Invalid value for `style`, must not be `None`")  # noqa: E501

        self._style = style

    @property
    def showvolume(self):
        """Gets the showvolume of this BotapiGetChartRequest.  # noqa: E501


        :return: The showvolume of this BotapiGetChartRequest.  # noqa: E501
        :rtype: bool
        """
        return self._showvolume

    @showvolume.setter
    def showvolume(self, showvolume):
        """Sets the showvolume of this BotapiGetChartRequest.


        :param showvolume: The showvolume of this BotapiGetChartRequest.  # noqa: E501
        :type: bool
        """
        if showvolume is None:
            raise ValueError("Invalid value for `showvolume`, must not be `None`")  # noqa: E501

        self._showvolume = showvolume

    @property
    def savesettings(self):
        """Gets the savesettings of this BotapiGetChartRequest.  # noqa: E501


        :return: The savesettings of this BotapiGetChartRequest.  # noqa: E501
        :rtype: bool
        """
        return self._savesettings

    @savesettings.setter
    def savesettings(self, savesettings):
        """Sets the savesettings of this BotapiGetChartRequest.


        :param savesettings: The savesettings of this BotapiGetChartRequest.  # noqa: E501
        :type: bool
        """
        if savesettings is None:
            raise ValueError("Invalid value for `savesettings`, must not be `None`")  # noqa: E501

        self._savesettings = savesettings

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
        if issubclass(BotapiGetChartRequest, dict):
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
        if not isinstance(other, BotapiGetChartRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
