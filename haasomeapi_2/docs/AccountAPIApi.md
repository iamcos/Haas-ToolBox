# swagger_client.AccountAPIApi

All URIs are relative to *http://127.0.0.1:8090*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_account**](AccountAPIApi.md#add_account) | **POST** /AccountAPI.php?channel&#x3D;ADD_ACCOUNT | Adds a new real account
[**add_simulated_account**](AccountAPIApi.md#add_simulated_account) | **POST** /AccountAPI.php?channel&#x3D;ADD_SIMULATED_ACCOUNT | Adds a new simulated account
[**adjust_leverage_settings**](AccountAPIApi.md#adjust_leverage_settings) | **POST** /AccountAPI.php?channel&#x3D;ADJUST_LEVERAGE_SETTINGS | Sets new properties to a leverage configuration
[**delete_account**](AccountAPIApi.md#delete_account) | **POST** /AccountAPI.php?channel&#x3D;DELETE_ACCOUNT | Deletes the given account and all its history
[**edit_account_keys**](AccountAPIApi.md#edit_account_keys) | **POST** /AccountAPI.php?channel&#x3D;EDIT_ACCOUNT_KEYS | Updates the real account its API keys
[**edit_account_visabilty**](AccountAPIApi.md#edit_account_visabilty) | **POST** /AccountAPI.php?channel&#x3D;EDIT_ACCOUNT_VISABILTY | Changes the account its public visability
[**get_account_data**](AccountAPIApi.md#get_account_data) | **POST** /AccountAPI.php?channel&#x3D;GET_ACCOUNT_DATA | Returns all the details of the given account (wallet, orders, positions)
[**get_accounts**](AccountAPIApi.md#get_accounts) | **POST** /AccountAPI.php?channel&#x3D;GET_ACCOUNTS | Returns a list of all real and simulated accounts
[**get_all_orders**](AccountAPIApi.md#get_all_orders) | **POST** /AccountAPI.php?channel&#x3D;GET_ALL_ORDERS | Returns all the user its open orders of all accounts
[**get_all_positions**](AccountAPIApi.md#get_all_positions) | **POST** /AccountAPI.php?channel&#x3D;GET_ALL_POSITIONS | Returns all the user its open positions of all accounts
[**get_all_trades**](AccountAPIApi.md#get_all_trades) | **POST** /AccountAPI.php?channel&#x3D;GET_ALL_TRADES | Returns all the recent historical trades of all the accounts
[**get_all_wallets**](AccountAPIApi.md#get_all_wallets) | **POST** /AccountAPI.php?channel&#x3D;GET_ALL_WALLETS | Returns all the user its wallets of all accounts
[**get_leverage_settings**](AccountAPIApi.md#get_leverage_settings) | **POST** /AccountAPI.php?channel&#x3D;GET_LEVERAGE_SETTINGS | Returns the leverage settings as setup on the API (per market)
[**get_orders**](AccountAPIApi.md#get_orders) | **POST** /AccountAPI.php?channel&#x3D;GET_ORDERS | Returns the open orders of the given account
[**get_positions**](AccountAPIApi.md#get_positions) | **POST** /AccountAPI.php?channel&#x3D;GET_POSITIONS | Returns the open positions of the given account
[**get_trades**](AccountAPIApi.md#get_trades) | **POST** /AccountAPI.php?channel&#x3D;GET_TRADES | Returns the historical trades of the given account
[**get_wallet**](AccountAPIApi.md#get_wallet) | **POST** /AccountAPI.php?channel&#x3D;GET_WALLET | Returns the wallet of the given account
[**rename_account**](AccountAPIApi.md#rename_account) | **POST** /AccountAPI.php?channel&#x3D;RENAME_ACCOUNT | Renames the given account
[**set_wallet_amount_simulated**](AccountAPIApi.md#set_wallet_amount_simulated) | **POST** /AccountAPI.php?channel&#x3D;SET_WALLET_AMOUNT_SIMULATED | Sets a new coin amount to a simulated wallet
[**test_account**](AccountAPIApi.md#test_account) | **POST** /AccountAPI.php?channel&#x3D;TEST_ACCOUNT | Adds a new testnet account

# **add_account**
> AccountapiAddAccountResponse add_account(userid=userid, interfacekey=interfacekey, name=name, drivercode=drivercode, drivertype=drivertype, publickey=publickey, privatekey=privatekey, extrakey=extrakey, istestnet=istestnet)

Adds a new real account

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.AccountAPIApi()
userid = 'userid_example' # str |  (optional)
interfacekey = 'interfacekey_example' # str |  (optional)
name = 'name_example' # str |  (optional)
drivercode = 'drivercode_example' # str |  (optional)
drivertype = 56 # int |  (optional)
publickey = 'publickey_example' # str |  (optional)
privatekey = 'privatekey_example' # str |  (optional)
extrakey = 'extrakey_example' # str |  (optional)
istestnet = true # bool |  (optional)

try:
    # Adds a new real account
    api_response = api_instance.add_account(userid=userid, interfacekey=interfacekey, name=name, drivercode=drivercode, drivertype=drivertype, publickey=publickey, privatekey=privatekey, extrakey=extrakey, istestnet=istestnet)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AccountAPIApi->add_account: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **userid** | **str**|  | [optional] 
 **interfacekey** | **str**|  | [optional] 
 **name** | **str**|  | [optional] 
 **drivercode** | **str**|  | [optional] 
 **drivertype** | **int**|  | [optional] 
 **publickey** | **str**|  | [optional] 
 **privatekey** | **str**|  | [optional] 
 **extrakey** | **str**|  | [optional] 
 **istestnet** | **bool**|  | [optional] 

### Return type

[**AccountapiAddAccountResponse**](AccountapiAddAccountResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **add_simulated_account**
> AccountapiAddSimulatedAccountResponse add_simulated_account(userid=userid, interfacekey=interfacekey, name=name, drivercode=drivercode, drivertype=drivertype)

Adds a new simulated account

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.AccountAPIApi()
userid = 'userid_example' # str |  (optional)
interfacekey = 'interfacekey_example' # str |  (optional)
name = 'name_example' # str |  (optional)
drivercode = 'drivercode_example' # str |  (optional)
drivertype = 56 # int |  (optional)

try:
    # Adds a new simulated account
    api_response = api_instance.add_simulated_account(userid=userid, interfacekey=interfacekey, name=name, drivercode=drivercode, drivertype=drivertype)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AccountAPIApi->add_simulated_account: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **userid** | **str**|  | [optional] 
 **interfacekey** | **str**|  | [optional] 
 **name** | **str**|  | [optional] 
 **drivercode** | **str**|  | [optional] 
 **drivertype** | **int**|  | [optional] 

### Return type

[**AccountapiAddSimulatedAccountResponse**](AccountapiAddSimulatedAccountResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **adjust_leverage_settings**
> AccountapiAdjustLeverageSettingsResponse adjust_leverage_settings(userid=userid, interfacekey=interfacekey, accountid=accountid, market=market, positionside=positionside, positionmode=positionmode, marginmode=marginmode, leverage=leverage)

Sets new properties to a leverage configuration

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.AccountAPIApi()
userid = 'userid_example' # str |  (optional)
interfacekey = 'interfacekey_example' # str |  (optional)
accountid = 'accountid_example' # str |  (optional)
market = 'market_example' # str |  (optional)
positionside = 56 # int |  (optional)
positionmode = 56 # int |  (optional)
marginmode = NULL # object |  (optional)
leverage = 1.2 # float |  (optional)

try:
    # Sets new properties to a leverage configuration
    api_response = api_instance.adjust_leverage_settings(userid=userid, interfacekey=interfacekey, accountid=accountid, market=market, positionside=positionside, positionmode=positionmode, marginmode=marginmode, leverage=leverage)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AccountAPIApi->adjust_leverage_settings: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **userid** | **str**|  | [optional] 
 **interfacekey** | **str**|  | [optional] 
 **accountid** | **str**|  | [optional] 
 **market** | **str**|  | [optional] 
 **positionside** | **int**|  | [optional] 
 **positionmode** | **int**|  | [optional] 
 **marginmode** | [**object**](.md)|  | [optional] 
 **leverage** | **float**|  | [optional] 

### Return type

[**AccountapiAdjustLeverageSettingsResponse**](AccountapiAdjustLeverageSettingsResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_account**
> AccountapiDeleteAccountResponse delete_account(userid=userid, interfacekey=interfacekey, accountid=accountid)

Deletes the given account and all its history

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.AccountAPIApi()
userid = 'userid_example' # str |  (optional)
interfacekey = 'interfacekey_example' # str |  (optional)
accountid = 'accountid_example' # str |  (optional)

try:
    # Deletes the given account and all its history
    api_response = api_instance.delete_account(userid=userid, interfacekey=interfacekey, accountid=accountid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AccountAPIApi->delete_account: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **userid** | **str**|  | [optional] 
 **interfacekey** | **str**|  | [optional] 
 **accountid** | **str**|  | [optional] 

### Return type

[**AccountapiDeleteAccountResponse**](AccountapiDeleteAccountResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **edit_account_keys**
> AccountapiEditAccountKeysResponse edit_account_keys(userid=userid, interfacekey=interfacekey, accountid=accountid, publickey=publickey, privatekey=privatekey, extrakey=extrakey)

Updates the real account its API keys

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.AccountAPIApi()
userid = 'userid_example' # str |  (optional)
interfacekey = 'interfacekey_example' # str |  (optional)
accountid = 'accountid_example' # str |  (optional)
publickey = 'publickey_example' # str |  (optional)
privatekey = 'privatekey_example' # str |  (optional)
extrakey = 'extrakey_example' # str |  (optional)

try:
    # Updates the real account its API keys
    api_response = api_instance.edit_account_keys(userid=userid, interfacekey=interfacekey, accountid=accountid, publickey=publickey, privatekey=privatekey, extrakey=extrakey)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AccountAPIApi->edit_account_keys: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **userid** | **str**|  | [optional] 
 **interfacekey** | **str**|  | [optional] 
 **accountid** | **str**|  | [optional] 
 **publickey** | **str**|  | [optional] 
 **privatekey** | **str**|  | [optional] 
 **extrakey** | **str**|  | [optional] 

### Return type

[**AccountapiEditAccountKeysResponse**](AccountapiEditAccountKeysResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **edit_account_visabilty**
> AccountapiEditAccountVisabiltyResponse edit_account_visabilty(userid=userid, interfacekey=interfacekey, accountid=accountid, publicvisible=publicvisible)

Changes the account its public visability

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.AccountAPIApi()
userid = 'userid_example' # str |  (optional)
interfacekey = 'interfacekey_example' # str |  (optional)
accountid = 'accountid_example' # str |  (optional)
publicvisible = true # bool |  (optional)

try:
    # Changes the account its public visability
    api_response = api_instance.edit_account_visabilty(userid=userid, interfacekey=interfacekey, accountid=accountid, publicvisible=publicvisible)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AccountAPIApi->edit_account_visabilty: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **userid** | **str**|  | [optional] 
 **interfacekey** | **str**|  | [optional] 
 **accountid** | **str**|  | [optional] 
 **publicvisible** | **bool**|  | [optional] 

### Return type

[**AccountapiEditAccountVisabiltyResponse**](AccountapiEditAccountVisabiltyResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_account_data**
> AccountapiGetAccountDataResponse get_account_data(userid=userid, interfacekey=interfacekey, accountid=accountid)

Returns all the details of the given account (wallet, orders, positions)

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.AccountAPIApi()
userid = 'userid_example' # str |  (optional)
interfacekey = 'interfacekey_example' # str |  (optional)
accountid = 'accountid_example' # str |  (optional)

try:
    # Returns all the details of the given account (wallet, orders, positions)
    api_response = api_instance.get_account_data(userid=userid, interfacekey=interfacekey, accountid=accountid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AccountAPIApi->get_account_data: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **userid** | **str**|  | [optional] 
 **interfacekey** | **str**|  | [optional] 
 **accountid** | **str**|  | [optional] 

### Return type

[**AccountapiGetAccountDataResponse**](AccountapiGetAccountDataResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_accounts**
> AccountapiGetAccountsResponse get_accounts(userid=userid, interfacekey=interfacekey)

Returns a list of all real and simulated accounts

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.AccountAPIApi()
userid = 'userid_example' # str |  (optional)
interfacekey = 'interfacekey_example' # str |  (optional)

try:
    # Returns a list of all real and simulated accounts
    api_response = api_instance.get_accounts(userid=userid, interfacekey=interfacekey)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AccountAPIApi->get_accounts: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **userid** | **str**|  | [optional] 
 **interfacekey** | **str**|  | [optional] 

### Return type

[**AccountapiGetAccountsResponse**](AccountapiGetAccountsResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_all_orders**
> AccountapiGetAllOrdersResponse get_all_orders(userid=userid, interfacekey=interfacekey)

Returns all the user its open orders of all accounts

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.AccountAPIApi()
userid = 'userid_example' # str |  (optional)
interfacekey = 'interfacekey_example' # str |  (optional)

try:
    # Returns all the user its open orders of all accounts
    api_response = api_instance.get_all_orders(userid=userid, interfacekey=interfacekey)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AccountAPIApi->get_all_orders: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **userid** | **str**|  | [optional] 
 **interfacekey** | **str**|  | [optional] 

### Return type

[**AccountapiGetAllOrdersResponse**](AccountapiGetAllOrdersResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_all_positions**
> AccountapiGetAllPositionsResponse get_all_positions(userid=userid, interfacekey=interfacekey)

Returns all the user its open positions of all accounts

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.AccountAPIApi()
userid = 'userid_example' # str |  (optional)
interfacekey = 'interfacekey_example' # str |  (optional)

try:
    # Returns all the user its open positions of all accounts
    api_response = api_instance.get_all_positions(userid=userid, interfacekey=interfacekey)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AccountAPIApi->get_all_positions: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **userid** | **str**|  | [optional] 
 **interfacekey** | **str**|  | [optional] 

### Return type

[**AccountapiGetAllPositionsResponse**](AccountapiGetAllPositionsResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_all_trades**
> AccountapiGetAllTradesResponse get_all_trades(userid=userid, interfacekey=interfacekey)

Returns all the recent historical trades of all the accounts

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.AccountAPIApi()
userid = 'userid_example' # str |  (optional)
interfacekey = 'interfacekey_example' # str |  (optional)

try:
    # Returns all the recent historical trades of all the accounts
    api_response = api_instance.get_all_trades(userid=userid, interfacekey=interfacekey)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AccountAPIApi->get_all_trades: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **userid** | **str**|  | [optional] 
 **interfacekey** | **str**|  | [optional] 

### Return type

[**AccountapiGetAllTradesResponse**](AccountapiGetAllTradesResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_all_wallets**
> AccountapiGetAllWalletsResponse get_all_wallets(userid=userid, interfacekey=interfacekey)

Returns all the user its wallets of all accounts

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.AccountAPIApi()
userid = 'userid_example' # str |  (optional)
interfacekey = 'interfacekey_example' # str |  (optional)

try:
    # Returns all the user its wallets of all accounts
    api_response = api_instance.get_all_wallets(userid=userid, interfacekey=interfacekey)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AccountAPIApi->get_all_wallets: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **userid** | **str**|  | [optional] 
 **interfacekey** | **str**|  | [optional] 

### Return type

[**AccountapiGetAllWalletsResponse**](AccountapiGetAllWalletsResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_leverage_settings**
> AccountapiGetLeverageSettingsResponse get_leverage_settings(userid=userid, interfacekey=interfacekey, accountid=accountid, market=market)

Returns the leverage settings as setup on the API (per market)

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.AccountAPIApi()
userid = 'userid_example' # str |  (optional)
interfacekey = 'interfacekey_example' # str |  (optional)
accountid = 'accountid_example' # str |  (optional)
market = 'market_example' # str |  (optional)

try:
    # Returns the leverage settings as setup on the API (per market)
    api_response = api_instance.get_leverage_settings(userid=userid, interfacekey=interfacekey, accountid=accountid, market=market)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AccountAPIApi->get_leverage_settings: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **userid** | **str**|  | [optional] 
 **interfacekey** | **str**|  | [optional] 
 **accountid** | **str**|  | [optional] 
 **market** | **str**|  | [optional] 

### Return type

[**AccountapiGetLeverageSettingsResponse**](AccountapiGetLeverageSettingsResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_orders**
> AccountapiGetOrdersResponse get_orders(userid=userid, interfacekey=interfacekey, accountid=accountid)

Returns the open orders of the given account

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.AccountAPIApi()
userid = 'userid_example' # str |  (optional)
interfacekey = 'interfacekey_example' # str |  (optional)
accountid = 'accountid_example' # str |  (optional)

try:
    # Returns the open orders of the given account
    api_response = api_instance.get_orders(userid=userid, interfacekey=interfacekey, accountid=accountid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AccountAPIApi->get_orders: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **userid** | **str**|  | [optional] 
 **interfacekey** | **str**|  | [optional] 
 **accountid** | **str**|  | [optional] 

### Return type

[**AccountapiGetOrdersResponse**](AccountapiGetOrdersResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_positions**
> AccountapiGetPositionsResponse get_positions(userid=userid, interfacekey=interfacekey, accountid=accountid)

Returns the open positions of the given account

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.AccountAPIApi()
userid = 'userid_example' # str |  (optional)
interfacekey = 'interfacekey_example' # str |  (optional)
accountid = 'accountid_example' # str |  (optional)

try:
    # Returns the open positions of the given account
    api_response = api_instance.get_positions(userid=userid, interfacekey=interfacekey, accountid=accountid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AccountAPIApi->get_positions: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **userid** | **str**|  | [optional] 
 **interfacekey** | **str**|  | [optional] 
 **accountid** | **str**|  | [optional] 

### Return type

[**AccountapiGetPositionsResponse**](AccountapiGetPositionsResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_trades**
> AccountapiGetTradesResponse get_trades(userid=userid, interfacekey=interfacekey, accountid=accountid)

Returns the historical trades of the given account

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.AccountAPIApi()
userid = 'userid_example' # str |  (optional)
interfacekey = 'interfacekey_example' # str |  (optional)
accountid = 'accountid_example' # str |  (optional)

try:
    # Returns the historical trades of the given account
    api_response = api_instance.get_trades(userid=userid, interfacekey=interfacekey, accountid=accountid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AccountAPIApi->get_trades: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **userid** | **str**|  | [optional] 
 **interfacekey** | **str**|  | [optional] 
 **accountid** | **str**|  | [optional] 

### Return type

[**AccountapiGetTradesResponse**](AccountapiGetTradesResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_wallet**
> AccountapiGetWalletResponse get_wallet(userid=userid, interfacekey=interfacekey, accountid=accountid)

Returns the wallet of the given account

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.AccountAPIApi()
userid = 'userid_example' # str |  (optional)
interfacekey = 'interfacekey_example' # str |  (optional)
accountid = 'accountid_example' # str |  (optional)

try:
    # Returns the wallet of the given account
    api_response = api_instance.get_wallet(userid=userid, interfacekey=interfacekey, accountid=accountid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AccountAPIApi->get_wallet: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **userid** | **str**|  | [optional] 
 **interfacekey** | **str**|  | [optional] 
 **accountid** | **str**|  | [optional] 

### Return type

[**AccountapiGetWalletResponse**](AccountapiGetWalletResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **rename_account**
> AccountapiRenameAccountResponse rename_account(userid=userid, interfacekey=interfacekey, accountid=accountid, name=name)

Renames the given account

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.AccountAPIApi()
userid = 'userid_example' # str |  (optional)
interfacekey = 'interfacekey_example' # str |  (optional)
accountid = 'accountid_example' # str |  (optional)
name = 'name_example' # str |  (optional)

try:
    # Renames the given account
    api_response = api_instance.rename_account(userid=userid, interfacekey=interfacekey, accountid=accountid, name=name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AccountAPIApi->rename_account: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **userid** | **str**|  | [optional] 
 **interfacekey** | **str**|  | [optional] 
 **accountid** | **str**|  | [optional] 
 **name** | **str**|  | [optional] 

### Return type

[**AccountapiRenameAccountResponse**](AccountapiRenameAccountResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **set_wallet_amount_simulated**
> AccountapiSetWalletAmountSimulatedResponse set_wallet_amount_simulated(userid=userid, interfacekey=interfacekey, accountid=accountid, market=market, coin=coin, amount=amount)

Sets a new coin amount to a simulated wallet

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.AccountAPIApi()
userid = 'userid_example' # str |  (optional)
interfacekey = 'interfacekey_example' # str |  (optional)
accountid = 'accountid_example' # str |  (optional)
market = 'market_example' # str |  (optional)
coin = 'coin_example' # str |  (optional)
amount = 1.2 # float |  (optional)

try:
    # Sets a new coin amount to a simulated wallet
    api_response = api_instance.set_wallet_amount_simulated(userid=userid, interfacekey=interfacekey, accountid=accountid, market=market, coin=coin, amount=amount)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AccountAPIApi->set_wallet_amount_simulated: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **userid** | **str**|  | [optional] 
 **interfacekey** | **str**|  | [optional] 
 **accountid** | **str**|  | [optional] 
 **market** | **str**|  | [optional] 
 **coin** | **str**|  | [optional] 
 **amount** | **float**|  | [optional] 

### Return type

[**AccountapiSetWalletAmountSimulatedResponse**](AccountapiSetWalletAmountSimulatedResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **test_account**
> AccountapiTestAccountResponse test_account(userid=userid, interfacekey=interfacekey, drivercode=drivercode, drivertype=drivertype, publickey=publickey, privatekey=privatekey, extrakey=extrakey, istestnet=istestnet)

Adds a new testnet account

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.AccountAPIApi()
userid = 'userid_example' # str |  (optional)
interfacekey = 'interfacekey_example' # str |  (optional)
drivercode = 'drivercode_example' # str |  (optional)
drivertype = 56 # int |  (optional)
publickey = 'publickey_example' # str |  (optional)
privatekey = 'privatekey_example' # str |  (optional)
extrakey = 'extrakey_example' # str |  (optional)
istestnet = true # bool |  (optional)

try:
    # Adds a new testnet account
    api_response = api_instance.test_account(userid=userid, interfacekey=interfacekey, drivercode=drivercode, drivertype=drivertype, publickey=publickey, privatekey=privatekey, extrakey=extrakey, istestnet=istestnet)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AccountAPIApi->test_account: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **userid** | **str**|  | [optional] 
 **interfacekey** | **str**|  | [optional] 
 **drivercode** | **str**|  | [optional] 
 **drivertype** | **int**|  | [optional] 
 **publickey** | **str**|  | [optional] 
 **privatekey** | **str**|  | [optional] 
 **extrakey** | **str**|  | [optional] 
 **istestnet** | **bool**|  | [optional] 

### Return type

[**AccountapiTestAccountResponse**](AccountapiTestAccountResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

