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

class ExternalwalletapiGetWalletResponse(object):
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
        'id': 'str',
        'user_id': 'str',
        'name': 'str',
        'address': 'str',
        'coin': 'str',
        'final_balance': 'float',
        'btc_balance': 'float',
        'usd_balance': 'float',
        'last_update': 'int',
        'price_source': 'str'
    }

    attribute_map = {
        'id': 'Id',
        'user_id': 'UserId',
        'name': 'Name',
        'address': 'Address',
        'coin': 'Coin',
        'final_balance': 'FinalBalance',
        'btc_balance': 'BtcBalance',
        'usd_balance': 'UsdBalance',
        'last_update': 'LastUpdate',
        'price_source': 'PriceSource'
    }

    def __init__(self, id=None, user_id=None, name=None, address=None, coin=None, final_balance=None, btc_balance=None, usd_balance=None, last_update=None, price_source=None):  # noqa: E501
        """ExternalwalletapiGetWalletResponse - a model defined in Swagger"""  # noqa: E501
        self._id = None
        self._user_id = None
        self._name = None
        self._address = None
        self._coin = None
        self._final_balance = None
        self._btc_balance = None
        self._usd_balance = None
        self._last_update = None
        self._price_source = None
        self.discriminator = None
        if id is not None:
            self.id = id
        if user_id is not None:
            self.user_id = user_id
        if name is not None:
            self.name = name
        if address is not None:
            self.address = address
        if coin is not None:
            self.coin = coin
        if final_balance is not None:
            self.final_balance = final_balance
        if btc_balance is not None:
            self.btc_balance = btc_balance
        if usd_balance is not None:
            self.usd_balance = usd_balance
        if last_update is not None:
            self.last_update = last_update
        if price_source is not None:
            self.price_source = price_source

    @property
    def id(self):
        """Gets the id of this ExternalwalletapiGetWalletResponse.  # noqa: E501


        :return: The id of this ExternalwalletapiGetWalletResponse.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this ExternalwalletapiGetWalletResponse.


        :param id: The id of this ExternalwalletapiGetWalletResponse.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def user_id(self):
        """Gets the user_id of this ExternalwalletapiGetWalletResponse.  # noqa: E501


        :return: The user_id of this ExternalwalletapiGetWalletResponse.  # noqa: E501
        :rtype: str
        """
        return self._user_id

    @user_id.setter
    def user_id(self, user_id):
        """Sets the user_id of this ExternalwalletapiGetWalletResponse.


        :param user_id: The user_id of this ExternalwalletapiGetWalletResponse.  # noqa: E501
        :type: str
        """

        self._user_id = user_id

    @property
    def name(self):
        """Gets the name of this ExternalwalletapiGetWalletResponse.  # noqa: E501


        :return: The name of this ExternalwalletapiGetWalletResponse.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this ExternalwalletapiGetWalletResponse.


        :param name: The name of this ExternalwalletapiGetWalletResponse.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def address(self):
        """Gets the address of this ExternalwalletapiGetWalletResponse.  # noqa: E501


        :return: The address of this ExternalwalletapiGetWalletResponse.  # noqa: E501
        :rtype: str
        """
        return self._address

    @address.setter
    def address(self, address):
        """Sets the address of this ExternalwalletapiGetWalletResponse.


        :param address: The address of this ExternalwalletapiGetWalletResponse.  # noqa: E501
        :type: str
        """

        self._address = address

    @property
    def coin(self):
        """Gets the coin of this ExternalwalletapiGetWalletResponse.  # noqa: E501


        :return: The coin of this ExternalwalletapiGetWalletResponse.  # noqa: E501
        :rtype: str
        """
        return self._coin

    @coin.setter
    def coin(self, coin):
        """Sets the coin of this ExternalwalletapiGetWalletResponse.


        :param coin: The coin of this ExternalwalletapiGetWalletResponse.  # noqa: E501
        :type: str
        """

        self._coin = coin

    @property
    def final_balance(self):
        """Gets the final_balance of this ExternalwalletapiGetWalletResponse.  # noqa: E501


        :return: The final_balance of this ExternalwalletapiGetWalletResponse.  # noqa: E501
        :rtype: float
        """
        return self._final_balance

    @final_balance.setter
    def final_balance(self, final_balance):
        """Sets the final_balance of this ExternalwalletapiGetWalletResponse.


        :param final_balance: The final_balance of this ExternalwalletapiGetWalletResponse.  # noqa: E501
        :type: float
        """

        self._final_balance = final_balance

    @property
    def btc_balance(self):
        """Gets the btc_balance of this ExternalwalletapiGetWalletResponse.  # noqa: E501


        :return: The btc_balance of this ExternalwalletapiGetWalletResponse.  # noqa: E501
        :rtype: float
        """
        return self._btc_balance

    @btc_balance.setter
    def btc_balance(self, btc_balance):
        """Sets the btc_balance of this ExternalwalletapiGetWalletResponse.


        :param btc_balance: The btc_balance of this ExternalwalletapiGetWalletResponse.  # noqa: E501
        :type: float
        """

        self._btc_balance = btc_balance

    @property
    def usd_balance(self):
        """Gets the usd_balance of this ExternalwalletapiGetWalletResponse.  # noqa: E501


        :return: The usd_balance of this ExternalwalletapiGetWalletResponse.  # noqa: E501
        :rtype: float
        """
        return self._usd_balance

    @usd_balance.setter
    def usd_balance(self, usd_balance):
        """Sets the usd_balance of this ExternalwalletapiGetWalletResponse.


        :param usd_balance: The usd_balance of this ExternalwalletapiGetWalletResponse.  # noqa: E501
        :type: float
        """

        self._usd_balance = usd_balance

    @property
    def last_update(self):
        """Gets the last_update of this ExternalwalletapiGetWalletResponse.  # noqa: E501


        :return: The last_update of this ExternalwalletapiGetWalletResponse.  # noqa: E501
        :rtype: int
        """
        return self._last_update

    @last_update.setter
    def last_update(self, last_update):
        """Sets the last_update of this ExternalwalletapiGetWalletResponse.


        :param last_update: The last_update of this ExternalwalletapiGetWalletResponse.  # noqa: E501
        :type: int
        """

        self._last_update = last_update

    @property
    def price_source(self):
        """Gets the price_source of this ExternalwalletapiGetWalletResponse.  # noqa: E501


        :return: The price_source of this ExternalwalletapiGetWalletResponse.  # noqa: E501
        :rtype: str
        """
        return self._price_source

    @price_source.setter
    def price_source(self, price_source):
        """Sets the price_source of this ExternalwalletapiGetWalletResponse.


        :param price_source: The price_source of this ExternalwalletapiGetWalletResponse.  # noqa: E501
        :type: str
        """

        self._price_source = price_source

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
        if issubclass(ExternalwalletapiGetWalletResponse, dict):
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
        if not isinstance(other, ExternalwalletapiGetWalletResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
