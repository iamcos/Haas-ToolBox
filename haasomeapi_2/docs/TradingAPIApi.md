# swagger_client.TradingAPIApi

All URIs are relative to *http://127.0.0.1:8090*

Method | HTTP request | Description
------------- | ------------- | -------------
[**cancel_order**](TradingAPIApi.md#cancel_order) | **POST** /TradingAPI.php?channel&#x3D;CANCEL_ORDER | Cancels a open order
[**max_amount**](TradingAPIApi.md#max_amount) | **POST** /TradingAPI.php?channel&#x3D;MAX_AMOUNT | Calculates the maximum trade amount, price and margin
[**place_order**](TradingAPIApi.md#place_order) | **POST** /TradingAPI.php?channel&#x3D;PLACE_ORDER | Places a order
[**used_margin**](TradingAPIApi.md#used_margin) | **POST** /TradingAPI.php?channel&#x3D;USED_MARGIN | Returns what the used margin is

# **cancel_order**
> TradingapiCancelOrderResponse cancel_order(userid=userid, interfacekey=interfacekey, accountid=accountid, orderid=orderid)

Cancels a open order

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.TradingAPIApi()
userid = 'userid_example' # str |  (optional)
interfacekey = 'interfacekey_example' # str |  (optional)
accountid = 'accountid_example' # str |  (optional)
orderid = 'orderid_example' # str |  (optional)

try:
    # Cancels a open order
    api_response = api_instance.cancel_order(userid=userid, interfacekey=interfacekey, accountid=accountid, orderid=orderid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TradingAPIApi->cancel_order: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **userid** | **str**|  | [optional] 
 **interfacekey** | **str**|  | [optional] 
 **accountid** | **str**|  | [optional] 
 **orderid** | **str**|  | [optional] 

### Return type

[**TradingapiCancelOrderResponse**](TradingapiCancelOrderResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **max_amount**
> TradingapiMaxAmountResponse max_amount(userid=userid, interfacekey=interfacekey, accountid=accountid, market=market, price=price, usedamount=usedamount, amountpercentage=amountpercentage, isbuy=isbuy)

Calculates the maximum trade amount, price and margin

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.TradingAPIApi()
userid = 'userid_example' # str |  (optional)
interfacekey = 'interfacekey_example' # str |  (optional)
accountid = 'accountid_example' # str |  (optional)
market = 'market_example' # str |  (optional)
price = 1.2 # float |  (optional)
usedamount = 1.2 # float |  (optional)
amountpercentage = 1.2 # float |  (optional)
isbuy = true # bool |  (optional)

try:
    # Calculates the maximum trade amount, price and margin
    api_response = api_instance.max_amount(userid=userid, interfacekey=interfacekey, accountid=accountid, market=market, price=price, usedamount=usedamount, amountpercentage=amountpercentage, isbuy=isbuy)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TradingAPIApi->max_amount: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **userid** | **str**|  | [optional] 
 **interfacekey** | **str**|  | [optional] 
 **accountid** | **str**|  | [optional] 
 **market** | **str**|  | [optional] 
 **price** | **float**|  | [optional] 
 **usedamount** | **float**|  | [optional] 
 **amountpercentage** | **float**|  | [optional] 
 **isbuy** | **bool**|  | [optional] 

### Return type

[**TradingapiMaxAmountResponse**](TradingapiMaxAmountResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **place_order**
> TradingapiPlaceOrderResponse place_order(userid=userid, interfacekey=interfacekey, order=order)

Places a order

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.TradingAPIApi()
userid = 'userid_example' # str |  (optional)
interfacekey = 'interfacekey_example' # str |  (optional)
order = NULL # object |  (optional)

try:
    # Places a order
    api_response = api_instance.place_order(userid=userid, interfacekey=interfacekey, order=order)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TradingAPIApi->place_order: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **userid** | **str**|  | [optional] 
 **interfacekey** | **str**|  | [optional] 
 **order** | [**object**](.md)|  | [optional] 

### Return type

[**TradingapiPlaceOrderResponse**](TradingapiPlaceOrderResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **used_margin**
> TradingapiUsedMarginResponse used_margin(userid=userid, interfacekey=interfacekey, drivername=drivername, drivertype=drivertype, market=market, leverage=leverage, price=price, amount=amount)

Returns what the used margin is

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.TradingAPIApi()
userid = 'userid_example' # str |  (optional)
interfacekey = 'interfacekey_example' # str |  (optional)
drivername = 'drivername_example' # str |  (optional)
drivertype = 56 # int |  (optional)
market = 'market_example' # str |  (optional)
leverage = 1.2 # float |  (optional)
price = 1.2 # float |  (optional)
amount = 1.2 # float |  (optional)

try:
    # Returns what the used margin is
    api_response = api_instance.used_margin(userid=userid, interfacekey=interfacekey, drivername=drivername, drivertype=drivertype, market=market, leverage=leverage, price=price, amount=amount)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TradingAPIApi->used_margin: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **userid** | **str**|  | [optional] 
 **interfacekey** | **str**|  | [optional] 
 **drivername** | **str**|  | [optional] 
 **drivertype** | **int**|  | [optional] 
 **market** | **str**|  | [optional] 
 **leverage** | **float**|  | [optional] 
 **price** | **float**|  | [optional] 
 **amount** | **float**|  | [optional] 

### Return type

[**TradingapiUsedMarginResponse**](TradingapiUsedMarginResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

