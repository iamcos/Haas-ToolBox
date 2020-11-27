# swagger_client.ExchangeAPIApi

All URIs are relative to *http://127.0.0.1:8090*

Method | HTTP request | Description
------------- | ------------- | -------------
[**cancel_order**](ExchangeAPIApi.md#cancel_order) | **POST** /ExchangeAPI.php?channel&#x3D;CANCEL_ORDER | Cancels a order at the exchange
[**get_openorders**](ExchangeAPIApi.md#get_openorders) | **POST** /ExchangeAPI.php?channel&#x3D;GET_OPENORDERS | Returns all open orders
[**get_positions**](ExchangeAPIApi.md#get_positions) | **POST** /ExchangeAPI.php?channel&#x3D;GET_POSITIONS | Returns the open positions
[**get_wallet**](ExchangeAPIApi.md#get_wallet) | **POST** /ExchangeAPI.php?channel&#x3D;GET_WALLET | Returns the wallet
[**place_order**](ExchangeAPIApi.md#place_order) | **POST** /ExchangeAPI.php?channel&#x3D;PLACE_ORDER | Places a order at the exchange

# **cancel_order**
> ExchangeapiCancelOrderResponse cancel_order(userid=userid, interfacekey=interfacekey, driver=driver, publickey=publickey, privatekey=privatekey, username=username, nonce=nonce, market=market, orderid=orderid, isbuyorder=isbuyorder)

Cancels a order at the exchange

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ExchangeAPIApi()
userid = 'userid_example' # str |  (optional)
interfacekey = 'interfacekey_example' # str |  (optional)
driver = 'driver_example' # str |  (optional)
publickey = 'publickey_example' # str |  (optional)
privatekey = 'privatekey_example' # str |  (optional)
username = 'username_example' # str |  (optional)
nonce = swagger_client.Int64() # Int64 |  (optional)
market = 'market_example' # str |  (optional)
orderid = 'orderid_example' # str |  (optional)
isbuyorder = true # bool |  (optional)

try:
    # Cancels a order at the exchange
    api_response = api_instance.cancel_order(userid=userid, interfacekey=interfacekey, driver=driver, publickey=publickey, privatekey=privatekey, username=username, nonce=nonce, market=market, orderid=orderid, isbuyorder=isbuyorder)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ExchangeAPIApi->cancel_order: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **userid** | **str**|  | [optional] 
 **interfacekey** | **str**|  | [optional] 
 **driver** | **str**|  | [optional] 
 **publickey** | **str**|  | [optional] 
 **privatekey** | **str**|  | [optional] 
 **username** | **str**|  | [optional] 
 **nonce** | [**Int64**](.md)|  | [optional] 
 **market** | **str**|  | [optional] 
 **orderid** | **str**|  | [optional] 
 **isbuyorder** | **bool**|  | [optional] 

### Return type

[**ExchangeapiCancelOrderResponse**](ExchangeapiCancelOrderResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_openorders**
> ExchangeapiGetOpenordersResponse get_openorders(userid=userid, interfacekey=interfacekey, driver=driver, publickey=publickey, privatekey=privatekey, username=username, nonce=nonce)

Returns all open orders

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ExchangeAPIApi()
userid = 'userid_example' # str |  (optional)
interfacekey = 'interfacekey_example' # str |  (optional)
driver = 'driver_example' # str |  (optional)
publickey = 'publickey_example' # str |  (optional)
privatekey = 'privatekey_example' # str |  (optional)
username = 'username_example' # str |  (optional)
nonce = swagger_client.Int64() # Int64 |  (optional)

try:
    # Returns all open orders
    api_response = api_instance.get_openorders(userid=userid, interfacekey=interfacekey, driver=driver, publickey=publickey, privatekey=privatekey, username=username, nonce=nonce)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ExchangeAPIApi->get_openorders: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **userid** | **str**|  | [optional] 
 **interfacekey** | **str**|  | [optional] 
 **driver** | **str**|  | [optional] 
 **publickey** | **str**|  | [optional] 
 **privatekey** | **str**|  | [optional] 
 **username** | **str**|  | [optional] 
 **nonce** | [**Int64**](.md)|  | [optional] 

### Return type

[**ExchangeapiGetOpenordersResponse**](ExchangeapiGetOpenordersResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_positions**
> ExchangeapiGetPositionsResponse get_positions(userid=userid, interfacekey=interfacekey, driver=driver, publickey=publickey, privatekey=privatekey, username=username, nonce=nonce)

Returns the open positions

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ExchangeAPIApi()
userid = 'userid_example' # str |  (optional)
interfacekey = 'interfacekey_example' # str |  (optional)
driver = 'driver_example' # str |  (optional)
publickey = 'publickey_example' # str |  (optional)
privatekey = 'privatekey_example' # str |  (optional)
username = 'username_example' # str |  (optional)
nonce = swagger_client.Int64() # Int64 |  (optional)

try:
    # Returns the open positions
    api_response = api_instance.get_positions(userid=userid, interfacekey=interfacekey, driver=driver, publickey=publickey, privatekey=privatekey, username=username, nonce=nonce)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ExchangeAPIApi->get_positions: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **userid** | **str**|  | [optional] 
 **interfacekey** | **str**|  | [optional] 
 **driver** | **str**|  | [optional] 
 **publickey** | **str**|  | [optional] 
 **privatekey** | **str**|  | [optional] 
 **username** | **str**|  | [optional] 
 **nonce** | [**Int64**](.md)|  | [optional] 

### Return type

[**ExchangeapiGetPositionsResponse**](ExchangeapiGetPositionsResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_wallet**
> ExchangeapiGetWalletResponse get_wallet(userid=userid, interfacekey=interfacekey, driver=driver, publickey=publickey, privatekey=privatekey, username=username, nonce=nonce)

Returns the wallet

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ExchangeAPIApi()
userid = 'userid_example' # str |  (optional)
interfacekey = 'interfacekey_example' # str |  (optional)
driver = 'driver_example' # str |  (optional)
publickey = 'publickey_example' # str |  (optional)
privatekey = 'privatekey_example' # str |  (optional)
username = 'username_example' # str |  (optional)
nonce = swagger_client.Int64() # Int64 |  (optional)

try:
    # Returns the wallet
    api_response = api_instance.get_wallet(userid=userid, interfacekey=interfacekey, driver=driver, publickey=publickey, privatekey=privatekey, username=username, nonce=nonce)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ExchangeAPIApi->get_wallet: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **userid** | **str**|  | [optional] 
 **interfacekey** | **str**|  | [optional] 
 **driver** | **str**|  | [optional] 
 **publickey** | **str**|  | [optional] 
 **privatekey** | **str**|  | [optional] 
 **username** | **str**|  | [optional] 
 **nonce** | [**Int64**](.md)|  | [optional] 

### Return type

[**ExchangeapiGetWalletResponse**](ExchangeapiGetWalletResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **place_order**
> ExchangeapiPlaceOrderResponse place_order(userid=userid, interfacekey=interfacekey, driver=driver, publickey=publickey, privatekey=privatekey, username=username, nonce=nonce, market=market, direction=direction, price=price, amount=amount, ismarketorder=ismarketorder, leverage=leverage, template=template)

Places a order at the exchange

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ExchangeAPIApi()
userid = 'userid_example' # str |  (optional)
interfacekey = 'interfacekey_example' # str |  (optional)
driver = 'driver_example' # str |  (optional)
publickey = 'publickey_example' # str |  (optional)
privatekey = 'privatekey_example' # str |  (optional)
username = 'username_example' # str |  (optional)
nonce = swagger_client.Int64() # Int64 |  (optional)
market = 'market_example' # str |  (optional)
direction = 56 # int |  (optional)
price = 1.2 # float |  (optional)
amount = 1.2 # float |  (optional)
ismarketorder = true # bool |  (optional)
leverage = 1.2 # float |  (optional)
template = 'template_example' # str |  (optional)

try:
    # Places a order at the exchange
    api_response = api_instance.place_order(userid=userid, interfacekey=interfacekey, driver=driver, publickey=publickey, privatekey=privatekey, username=username, nonce=nonce, market=market, direction=direction, price=price, amount=amount, ismarketorder=ismarketorder, leverage=leverage, template=template)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ExchangeAPIApi->place_order: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **userid** | **str**|  | [optional] 
 **interfacekey** | **str**|  | [optional] 
 **driver** | **str**|  | [optional] 
 **publickey** | **str**|  | [optional] 
 **privatekey** | **str**|  | [optional] 
 **username** | **str**|  | [optional] 
 **nonce** | [**Int64**](.md)|  | [optional] 
 **market** | **str**|  | [optional] 
 **direction** | **int**|  | [optional] 
 **price** | **float**|  | [optional] 
 **amount** | **float**|  | [optional] 
 **ismarketorder** | **bool**|  | [optional] 
 **leverage** | **float**|  | [optional] 
 **template** | **str**|  | [optional] 

### Return type

[**ExchangeapiPlaceOrderResponse**](ExchangeapiPlaceOrderResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

