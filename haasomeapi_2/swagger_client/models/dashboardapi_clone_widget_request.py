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

class DashboardapiCloneWidgetRequest(object):
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
        'widgetid': 'str',
        'x': 'int',
        'y': 'int',
        'z': 'int'
    }

    attribute_map = {
        'userid': 'userid',
        'interfacekey': 'interfacekey',
        'widgetid': 'widgetid',
        'x': 'x',
        'y': 'y',
        'z': 'z'
    }

    def __init__(self, userid=None, interfacekey=None, widgetid=None, x=None, y=None, z=None):  # noqa: E501
        """DashboardapiCloneWidgetRequest - a model defined in Swagger"""  # noqa: E501
        self._userid = None
        self._interfacekey = None
        self._widgetid = None
        self._x = None
        self._y = None
        self._z = None
        self.discriminator = None
        self.userid = userid
        self.interfacekey = interfacekey
        self.widgetid = widgetid
        self.x = x
        self.y = y
        self.z = z

    @property
    def userid(self):
        """Gets the userid of this DashboardapiCloneWidgetRequest.  # noqa: E501

        The userid as obtained at the login  # noqa: E501

        :return: The userid of this DashboardapiCloneWidgetRequest.  # noqa: E501
        :rtype: str
        """
        return self._userid

    @userid.setter
    def userid(self, userid):
        """Sets the userid of this DashboardapiCloneWidgetRequest.

        The userid as obtained at the login  # noqa: E501

        :param userid: The userid of this DashboardapiCloneWidgetRequest.  # noqa: E501
        :type: str
        """
        if userid is None:
            raise ValueError("Invalid value for `userid`, must not be `None`")  # noqa: E501

        self._userid = userid

    @property
    def interfacekey(self):
        """Gets the interfacekey of this DashboardapiCloneWidgetRequest.  # noqa: E501

        The interfacekey as generated at login  # noqa: E501

        :return: The interfacekey of this DashboardapiCloneWidgetRequest.  # noqa: E501
        :rtype: str
        """
        return self._interfacekey

    @interfacekey.setter
    def interfacekey(self, interfacekey):
        """Sets the interfacekey of this DashboardapiCloneWidgetRequest.

        The interfacekey as generated at login  # noqa: E501

        :param interfacekey: The interfacekey of this DashboardapiCloneWidgetRequest.  # noqa: E501
        :type: str
        """
        if interfacekey is None:
            raise ValueError("Invalid value for `interfacekey`, must not be `None`")  # noqa: E501

        self._interfacekey = interfacekey

    @property
    def widgetid(self):
        """Gets the widgetid of this DashboardapiCloneWidgetRequest.  # noqa: E501

        Widget identifier  # noqa: E501

        :return: The widgetid of this DashboardapiCloneWidgetRequest.  # noqa: E501
        :rtype: str
        """
        return self._widgetid

    @widgetid.setter
    def widgetid(self, widgetid):
        """Sets the widgetid of this DashboardapiCloneWidgetRequest.

        Widget identifier  # noqa: E501

        :param widgetid: The widgetid of this DashboardapiCloneWidgetRequest.  # noqa: E501
        :type: str
        """
        if widgetid is None:
            raise ValueError("Invalid value for `widgetid`, must not be `None`")  # noqa: E501

        self._widgetid = widgetid

    @property
    def x(self):
        """Gets the x of this DashboardapiCloneWidgetRequest.  # noqa: E501


        :return: The x of this DashboardapiCloneWidgetRequest.  # noqa: E501
        :rtype: int
        """
        return self._x

    @x.setter
    def x(self, x):
        """Sets the x of this DashboardapiCloneWidgetRequest.


        :param x: The x of this DashboardapiCloneWidgetRequest.  # noqa: E501
        :type: int
        """
        if x is None:
            raise ValueError("Invalid value for `x`, must not be `None`")  # noqa: E501

        self._x = x

    @property
    def y(self):
        """Gets the y of this DashboardapiCloneWidgetRequest.  # noqa: E501


        :return: The y of this DashboardapiCloneWidgetRequest.  # noqa: E501
        :rtype: int
        """
        return self._y

    @y.setter
    def y(self, y):
        """Sets the y of this DashboardapiCloneWidgetRequest.


        :param y: The y of this DashboardapiCloneWidgetRequest.  # noqa: E501
        :type: int
        """
        if y is None:
            raise ValueError("Invalid value for `y`, must not be `None`")  # noqa: E501

        self._y = y

    @property
    def z(self):
        """Gets the z of this DashboardapiCloneWidgetRequest.  # noqa: E501


        :return: The z of this DashboardapiCloneWidgetRequest.  # noqa: E501
        :rtype: int
        """
        return self._z

    @z.setter
    def z(self, z):
        """Sets the z of this DashboardapiCloneWidgetRequest.


        :param z: The z of this DashboardapiCloneWidgetRequest.  # noqa: E501
        :type: int
        """
        if z is None:
            raise ValueError("Invalid value for `z`, must not be `None`")  # noqa: E501

        self._z = z

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
        if issubclass(DashboardapiCloneWidgetRequest, dict):
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
        if not isinstance(other, DashboardapiCloneWidgetRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
