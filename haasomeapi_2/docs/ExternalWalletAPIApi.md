# swagger_client.ExternalWalletAPIApi

All URIs are relative to *http://127.0.0.1:8090*

Method | HTTP request | Description
------------- | ------------- | -------------
[**edit_wallet**](ExternalWalletAPIApi.md#edit_wallet) | **POST** /ExternalWalletAPI.php?channel&#x3D;EDIT_WALLET | Edits the wallet its properties
[**get_wallet**](ExternalWalletAPIApi.md#get_wallet) | **POST** /ExternalWalletAPI.php?channel&#x3D;GET_WALLET | Returns the wallet
[**get_wallets**](ExternalWalletAPIApi.md#get_wallets) | **POST** /ExternalWalletAPI.php?channel&#x3D;GET_WALLETS | Returns a list of the user its wallets
[**register_wallet**](ExternalWalletAPIApi.md#register_wallet) | **POST** /ExternalWalletAPI.php?channel&#x3D;REGISTER_WALLET | Add a new wallet to the user its list
[**remove_wallet**](ExternalWalletAPIApi.md#remove_wallet) | **POST** /ExternalWalletAPI.php?channel&#x3D;REMOVE_WALLET | Delete/remove a wallet from the list of registered wallets
[**supported_currencies**](ExternalWalletAPIApi.md#supported_currencies) | **POST** /ExternalWalletAPI.php?channel&#x3D;SUPPORTED_CURRENCIES | Returns a list of all the supported currencies
[**update_wallet**](ExternalWalletAPIApi.md#update_wallet) | **POST** /ExternalWalletAPI.php?channel&#x3D;UPDATE_WALLET | Executes a forced update to refresh the wallet data

# **edit_wallet**
> ExternalwalletapiEditWalletResponse edit_wallet(userid=userid, interfacekey=interfacekey, walletid=walletid, currency=currency, adres=adres, name=name)

Edits the wallet its properties

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ExternalWalletAPIApi()
userid = 'userid_example' # str |  (optional)
interfacekey = 'interfacekey_example' # str |  (optional)
walletid = 'walletid_example' # str |  (optional)
currency = 'currency_example' # str |  (optional)
adres = 'adres_example' # str |  (optional)
name = 'name_example' # str |  (optional)

try:
    # Edits the wallet its properties
    api_response = api_instance.edit_wallet(userid=userid, interfacekey=interfacekey, walletid=walletid, currency=currency, adres=adres, name=name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ExternalWalletAPIApi->edit_wallet: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **userid** | **str**|  | [optional] 
 **interfacekey** | **str**|  | [optional] 
 **walletid** | **str**|  | [optional] 
 **currency** | **str**|  | [optional] 
 **adres** | **str**|  | [optional] 
 **name** | **str**|  | [optional] 

### Return type

[**ExternalwalletapiEditWalletResponse**](ExternalwalletapiEditWalletResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_wallet**
> ExternalwalletapiGetWalletResponse get_wallet(userid=userid, interfacekey=interfacekey, walletid=walletid)

Returns the wallet

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ExternalWalletAPIApi()
userid = 'userid_example' # str |  (optional)
interfacekey = 'interfacekey_example' # str |  (optional)
walletid = 'walletid_example' # str |  (optional)

try:
    # Returns the wallet
    api_response = api_instance.get_wallet(userid=userid, interfacekey=interfacekey, walletid=walletid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ExternalWalletAPIApi->get_wallet: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **userid** | **str**|  | [optional] 
 **interfacekey** | **str**|  | [optional] 
 **walletid** | **str**|  | [optional] 

### Return type

[**ExternalwalletapiGetWalletResponse**](ExternalwalletapiGetWalletResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_wallets**
> ExternalwalletapiGetWalletsResponse get_wallets(userid=userid, interfacekey=interfacekey)

Returns a list of the user its wallets

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ExternalWalletAPIApi()
userid = 'userid_example' # str |  (optional)
interfacekey = 'interfacekey_example' # str |  (optional)

try:
    # Returns a list of the user its wallets
    api_response = api_instance.get_wallets(userid=userid, interfacekey=interfacekey)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ExternalWalletAPIApi->get_wallets: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **userid** | **str**|  | [optional] 
 **interfacekey** | **str**|  | [optional] 

### Return type

[**ExternalwalletapiGetWalletsResponse**](ExternalwalletapiGetWalletsResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **register_wallet**
> ExternalwalletapiRegisterWalletResponse register_wallet(userid=userid, interfacekey=interfacekey, currency=currency, adres=adres, name=name)

Add a new wallet to the user its list

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ExternalWalletAPIApi()
userid = 'userid_example' # str |  (optional)
interfacekey = 'interfacekey_example' # str |  (optional)
currency = 'currency_example' # str |  (optional)
adres = 'adres_example' # str |  (optional)
name = 'name_example' # str |  (optional)

try:
    # Add a new wallet to the user its list
    api_response = api_instance.register_wallet(userid=userid, interfacekey=interfacekey, currency=currency, adres=adres, name=name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ExternalWalletAPIApi->register_wallet: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **userid** | **str**|  | [optional] 
 **interfacekey** | **str**|  | [optional] 
 **currency** | **str**|  | [optional] 
 **adres** | **str**|  | [optional] 
 **name** | **str**|  | [optional] 

### Return type

[**ExternalwalletapiRegisterWalletResponse**](ExternalwalletapiRegisterWalletResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **remove_wallet**
> ExternalwalletapiRemoveWalletResponse remove_wallet(userid=userid, interfacekey=interfacekey, walletid=walletid)

Delete/remove a wallet from the list of registered wallets

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ExternalWalletAPIApi()
userid = 'userid_example' # str |  (optional)
interfacekey = 'interfacekey_example' # str |  (optional)
walletid = 'walletid_example' # str |  (optional)

try:
    # Delete/remove a wallet from the list of registered wallets
    api_response = api_instance.remove_wallet(userid=userid, interfacekey=interfacekey, walletid=walletid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ExternalWalletAPIApi->remove_wallet: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **userid** | **str**|  | [optional] 
 **interfacekey** | **str**|  | [optional] 
 **walletid** | **str**|  | [optional] 

### Return type

[**ExternalwalletapiRemoveWalletResponse**](ExternalwalletapiRemoveWalletResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **supported_currencies**
> ExternalwalletapiSupportedCurrenciesResponse supported_currencies(userid=userid, interfacekey=interfacekey)

Returns a list of all the supported currencies

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ExternalWalletAPIApi()
userid = 'userid_example' # str |  (optional)
interfacekey = 'interfacekey_example' # str |  (optional)

try:
    # Returns a list of all the supported currencies
    api_response = api_instance.supported_currencies(userid=userid, interfacekey=interfacekey)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ExternalWalletAPIApi->supported_currencies: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **userid** | **str**|  | [optional] 
 **interfacekey** | **str**|  | [optional] 

### Return type

[**ExternalwalletapiSupportedCurrenciesResponse**](ExternalwalletapiSupportedCurrenciesResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_wallet**
> ExternalwalletapiUpdateWalletResponse update_wallet(userid=userid, interfacekey=interfacekey, walletid=walletid)

Executes a forced update to refresh the wallet data

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ExternalWalletAPIApi()
userid = 'userid_example' # str |  (optional)
interfacekey = 'interfacekey_example' # str |  (optional)
walletid = 'walletid_example' # str |  (optional)

try:
    # Executes a forced update to refresh the wallet data
    api_response = api_instance.update_wallet(userid=userid, interfacekey=interfacekey, walletid=walletid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ExternalWalletAPIApi->update_wallet: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **userid** | **str**|  | [optional] 
 **interfacekey** | **str**|  | [optional] 
 **walletid** | **str**|  | [optional] 

### Return type

[**ExternalwalletapiUpdateWalletResponse**](ExternalwalletapiUpdateWalletResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

