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

class AccountapiAddAccountResponse(object):
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
        'user_id': 'str',
        'account_id': 'str',
        'name': 'str',
        'exchange_code': 'str',
        'exchange_type': 'int',
        'status': 'object',
        'is_simulated': 'bool',
        'is_test_net': 'bool',
        'is_public': 'bool',
        'wallet_mode': 'object',
        'position_mode': 'int',
        'market_settings': 'object'
    }

    attribute_map = {
        'user_id': 'UserId',
        'account_id': 'AccountId',
        'name': 'Name',
        'exchange_code': 'ExchangeCode',
        'exchange_type': 'ExchangeType',
        'status': 'Status',
        'is_simulated': 'IsSimulated',
        'is_test_net': 'IsTestNet',
        'is_public': 'IsPublic',
        'wallet_mode': 'WalletMode',
        'position_mode': 'PositionMode',
        'market_settings': 'MarketSettings'
    }

    def __init__(self, user_id=None, account_id=None, name=None, exchange_code=None, exchange_type=None, status=None, is_simulated=None, is_test_net=None, is_public=None, wallet_mode=None, position_mode=None, market_settings=None):  # noqa: E501
        """AccountapiAddAccountResponse - a model defined in Swagger"""  # noqa: E501
        self._user_id = None
        self._account_id = None
        self._name = None
        self._exchange_code = None
        self._exchange_type = None
        self._status = None
        self._is_simulated = None
        self._is_test_net = None
        self._is_public = None
        self._wallet_mode = None
        self._position_mode = None
        self._market_settings = None
        self.discriminator = None
        if user_id is not None:
            self.user_id = user_id
        if account_id is not None:
            self.account_id = account_id
        if name is not None:
            self.name = name
        if exchange_code is not None:
            self.exchange_code = exchange_code
        if exchange_type is not None:
            self.exchange_type = exchange_type
        if status is not None:
            self.status = status
        if is_simulated is not None:
            self.is_simulated = is_simulated
        if is_test_net is not None:
            self.is_test_net = is_test_net
        if is_public is not None:
            self.is_public = is_public
        if wallet_mode is not None:
            self.wallet_mode = wallet_mode
        if position_mode is not None:
            self.position_mode = position_mode
        if market_settings is not None:
            self.market_settings = market_settings

    @property
    def user_id(self):
        """Gets the user_id of this AccountapiAddAccountResponse.  # noqa: E501


        :return: The user_id of this AccountapiAddAccountResponse.  # noqa: E501
        :rtype: str
        """
        return self._user_id

    @user_id.setter
    def user_id(self, user_id):
        """Sets the user_id of this AccountapiAddAccountResponse.


        :param user_id: The user_id of this AccountapiAddAccountResponse.  # noqa: E501
        :type: str
        """

        self._user_id = user_id

    @property
    def account_id(self):
        """Gets the account_id of this AccountapiAddAccountResponse.  # noqa: E501


        :return: The account_id of this AccountapiAddAccountResponse.  # noqa: E501
        :rtype: str
        """
        return self._account_id

    @account_id.setter
    def account_id(self, account_id):
        """Sets the account_id of this AccountapiAddAccountResponse.


        :param account_id: The account_id of this AccountapiAddAccountResponse.  # noqa: E501
        :type: str
        """

        self._account_id = account_id

    @property
    def name(self):
        """Gets the name of this AccountapiAddAccountResponse.  # noqa: E501


        :return: The name of this AccountapiAddAccountResponse.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this AccountapiAddAccountResponse.


        :param name: The name of this AccountapiAddAccountResponse.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def exchange_code(self):
        """Gets the exchange_code of this AccountapiAddAccountResponse.  # noqa: E501


        :return: The exchange_code of this AccountapiAddAccountResponse.  # noqa: E501
        :rtype: str
        """
        return self._exchange_code

    @exchange_code.setter
    def exchange_code(self, exchange_code):
        """Sets the exchange_code of this AccountapiAddAccountResponse.


        :param exchange_code: The exchange_code of this AccountapiAddAccountResponse.  # noqa: E501
        :type: str
        """

        self._exchange_code = exchange_code

    @property
    def exchange_type(self):
        """Gets the exchange_type of this AccountapiAddAccountResponse.  # noqa: E501


        :return: The exchange_type of this AccountapiAddAccountResponse.  # noqa: E501
        :rtype: int
        """
        return self._exchange_type

    @exchange_type.setter
    def exchange_type(self, exchange_type):
        """Sets the exchange_type of this AccountapiAddAccountResponse.


        :param exchange_type: The exchange_type of this AccountapiAddAccountResponse.  # noqa: E501
        :type: int
        """

        self._exchange_type = exchange_type

    @property
    def status(self):
        """Gets the status of this AccountapiAddAccountResponse.  # noqa: E501


        :return: The status of this AccountapiAddAccountResponse.  # noqa: E501
        :rtype: object
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this AccountapiAddAccountResponse.


        :param status: The status of this AccountapiAddAccountResponse.  # noqa: E501
        :type: object
        """

        self._status = status

    @property
    def is_simulated(self):
        """Gets the is_simulated of this AccountapiAddAccountResponse.  # noqa: E501


        :return: The is_simulated of this AccountapiAddAccountResponse.  # noqa: E501
        :rtype: bool
        """
        return self._is_simulated

    @is_simulated.setter
    def is_simulated(self, is_simulated):
        """Sets the is_simulated of this AccountapiAddAccountResponse.


        :param is_simulated: The is_simulated of this AccountapiAddAccountResponse.  # noqa: E501
        :type: bool
        """

        self._is_simulated = is_simulated

    @property
    def is_test_net(self):
        """Gets the is_test_net of this AccountapiAddAccountResponse.  # noqa: E501


        :return: The is_test_net of this AccountapiAddAccountResponse.  # noqa: E501
        :rtype: bool
        """
        return self._is_test_net

    @is_test_net.setter
    def is_test_net(self, is_test_net):
        """Sets the is_test_net of this AccountapiAddAccountResponse.


        :param is_test_net: The is_test_net of this AccountapiAddAccountResponse.  # noqa: E501
        :type: bool
        """

        self._is_test_net = is_test_net

    @property
    def is_public(self):
        """Gets the is_public of this AccountapiAddAccountResponse.  # noqa: E501


        :return: The is_public of this AccountapiAddAccountResponse.  # noqa: E501
        :rtype: bool
        """
        return self._is_public

    @is_public.setter
    def is_public(self, is_public):
        """Sets the is_public of this AccountapiAddAccountResponse.


        :param is_public: The is_public of this AccountapiAddAccountResponse.  # noqa: E501
        :type: bool
        """

        self._is_public = is_public

    @property
    def wallet_mode(self):
        """Gets the wallet_mode of this AccountapiAddAccountResponse.  # noqa: E501


        :return: The wallet_mode of this AccountapiAddAccountResponse.  # noqa: E501
        :rtype: object
        """
        return self._wallet_mode

    @wallet_mode.setter
    def wallet_mode(self, wallet_mode):
        """Sets the wallet_mode of this AccountapiAddAccountResponse.


        :param wallet_mode: The wallet_mode of this AccountapiAddAccountResponse.  # noqa: E501
        :type: object
        """

        self._wallet_mode = wallet_mode

    @property
    def position_mode(self):
        """Gets the position_mode of this AccountapiAddAccountResponse.  # noqa: E501


        :return: The position_mode of this AccountapiAddAccountResponse.  # noqa: E501
        :rtype: int
        """
        return self._position_mode

    @position_mode.setter
    def position_mode(self, position_mode):
        """Sets the position_mode of this AccountapiAddAccountResponse.


        :param position_mode: The position_mode of this AccountapiAddAccountResponse.  # noqa: E501
        :type: int
        """

        self._position_mode = position_mode

    @property
    def market_settings(self):
        """Gets the market_settings of this AccountapiAddAccountResponse.  # noqa: E501


        :return: The market_settings of this AccountapiAddAccountResponse.  # noqa: E501
        :rtype: object
        """
        return self._market_settings

    @market_settings.setter
    def market_settings(self, market_settings):
        """Sets the market_settings of this AccountapiAddAccountResponse.


        :param market_settings: The market_settings of this AccountapiAddAccountResponse.  # noqa: E501
        :type: object
        """

        self._market_settings = market_settings

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
        if issubclass(AccountapiAddAccountResponse, dict):
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
        if not isinstance(other, AccountapiAddAccountResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
