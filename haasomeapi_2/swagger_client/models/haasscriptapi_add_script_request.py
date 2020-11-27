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

class HaasscriptapiAddScriptRequest(object):
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
        'name': 'str',
        'description': 'str',
        'script': 'str',
        'type': 'int',
        'iscommand': 'bool'
    }

    attribute_map = {
        'userid': 'userid',
        'interfacekey': 'interfacekey',
        'name': 'name',
        'description': 'description',
        'script': 'script',
        'type': 'type',
        'iscommand': 'iscommand'
    }

    def __init__(self, userid=None, interfacekey=None, name=None, description=None, script=None, type=None, iscommand=None):  # noqa: E501
        """HaasscriptapiAddScriptRequest - a model defined in Swagger"""  # noqa: E501
        self._userid = None
        self._interfacekey = None
        self._name = None
        self._description = None
        self._script = None
        self._type = None
        self._iscommand = None
        self.discriminator = None
        self.userid = userid
        self.interfacekey = interfacekey
        self.name = name
        self.description = description
        self.script = script
        self.type = type
        self.iscommand = iscommand

    @property
    def userid(self):
        """Gets the userid of this HaasscriptapiAddScriptRequest.  # noqa: E501

        The userid as obtained at the login  # noqa: E501

        :return: The userid of this HaasscriptapiAddScriptRequest.  # noqa: E501
        :rtype: str
        """
        return self._userid

    @userid.setter
    def userid(self, userid):
        """Sets the userid of this HaasscriptapiAddScriptRequest.

        The userid as obtained at the login  # noqa: E501

        :param userid: The userid of this HaasscriptapiAddScriptRequest.  # noqa: E501
        :type: str
        """
        if userid is None:
            raise ValueError("Invalid value for `userid`, must not be `None`")  # noqa: E501

        self._userid = userid

    @property
    def interfacekey(self):
        """Gets the interfacekey of this HaasscriptapiAddScriptRequest.  # noqa: E501

        The interfacekey as generated at login  # noqa: E501

        :return: The interfacekey of this HaasscriptapiAddScriptRequest.  # noqa: E501
        :rtype: str
        """
        return self._interfacekey

    @interfacekey.setter
    def interfacekey(self, interfacekey):
        """Sets the interfacekey of this HaasscriptapiAddScriptRequest.

        The interfacekey as generated at login  # noqa: E501

        :param interfacekey: The interfacekey of this HaasscriptapiAddScriptRequest.  # noqa: E501
        :type: str
        """
        if interfacekey is None:
            raise ValueError("Invalid value for `interfacekey`, must not be `None`")  # noqa: E501

        self._interfacekey = interfacekey

    @property
    def name(self):
        """Gets the name of this HaasscriptapiAddScriptRequest.  # noqa: E501


        :return: The name of this HaasscriptapiAddScriptRequest.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this HaasscriptapiAddScriptRequest.


        :param name: The name of this HaasscriptapiAddScriptRequest.  # noqa: E501
        :type: str
        """
        if name is None:
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501

        self._name = name

    @property
    def description(self):
        """Gets the description of this HaasscriptapiAddScriptRequest.  # noqa: E501


        :return: The description of this HaasscriptapiAddScriptRequest.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this HaasscriptapiAddScriptRequest.


        :param description: The description of this HaasscriptapiAddScriptRequest.  # noqa: E501
        :type: str
        """
        if description is None:
            raise ValueError("Invalid value for `description`, must not be `None`")  # noqa: E501

        self._description = description

    @property
    def script(self):
        """Gets the script of this HaasscriptapiAddScriptRequest.  # noqa: E501


        :return: The script of this HaasscriptapiAddScriptRequest.  # noqa: E501
        :rtype: str
        """
        return self._script

    @script.setter
    def script(self, script):
        """Sets the script of this HaasscriptapiAddScriptRequest.


        :param script: The script of this HaasscriptapiAddScriptRequest.  # noqa: E501
        :type: str
        """
        if script is None:
            raise ValueError("Invalid value for `script`, must not be `None`")  # noqa: E501

        self._script = script

    @property
    def type(self):
        """Gets the type of this HaasscriptapiAddScriptRequest.  # noqa: E501


        :return: The type of this HaasscriptapiAddScriptRequest.  # noqa: E501
        :rtype: int
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this HaasscriptapiAddScriptRequest.


        :param type: The type of this HaasscriptapiAddScriptRequest.  # noqa: E501
        :type: int
        """
        if type is None:
            raise ValueError("Invalid value for `type`, must not be `None`")  # noqa: E501

        self._type = type

    @property
    def iscommand(self):
        """Gets the iscommand of this HaasscriptapiAddScriptRequest.  # noqa: E501


        :return: The iscommand of this HaasscriptapiAddScriptRequest.  # noqa: E501
        :rtype: bool
        """
        return self._iscommand

    @iscommand.setter
    def iscommand(self, iscommand):
        """Sets the iscommand of this HaasscriptapiAddScriptRequest.


        :param iscommand: The iscommand of this HaasscriptapiAddScriptRequest.  # noqa: E501
        :type: bool
        """
        if iscommand is None:
            raise ValueError("Invalid value for `iscommand`, must not be `None`")  # noqa: E501

        self._iscommand = iscommand

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
        if issubclass(HaasscriptapiAddScriptRequest, dict):
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
        if not isinstance(other, HaasscriptapiAddScriptRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
