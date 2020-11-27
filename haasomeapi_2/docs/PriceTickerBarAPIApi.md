# swagger_client.PriceTickerBarAPIApi

All URIs are relative to *http://127.0.0.1:8090*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_ticker**](PriceTickerBarAPIApi.md#add_ticker) | **POST** /PriceTickerBarAPI.php?channel&#x3D;ADD_TICKER | Add a new market to the price ticker bar
[**delete_ticker**](PriceTickerBarAPIApi.md#delete_ticker) | **POST** /PriceTickerBarAPI.php?channel&#x3D;DELETE_TICKER | Deletes the ticker
[**edit_ticker**](PriceTickerBarAPIApi.md#edit_ticker) | **POST** /PriceTickerBarAPI.php?channel&#x3D;EDIT_TICKER | Edits properties of the given price ticker
[**get_tickers**](PriceTickerBarAPIApi.md#get_tickers) | **POST** /PriceTickerBarAPI.php?channel&#x3D;GET_TICKERS | Return the user ist price ticker bar

# **add_ticker**
> PricetickerbarapiAddTickerResponse add_ticker(userid=userid, interfacekey=interfacekey, market=market)

Add a new market to the price ticker bar

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.PriceTickerBarAPIApi()
userid = 'userid_example' # str |  (optional)
interfacekey = 'interfacekey_example' # str |  (optional)
market = 'market_example' # str |  (optional)

try:
    # Add a new market to the price ticker bar
    api_response = api_instance.add_ticker(userid=userid, interfacekey=interfacekey, market=market)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PriceTickerBarAPIApi->add_ticker: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **userid** | **str**|  | [optional] 
 **interfacekey** | **str**|  | [optional] 
 **market** | **str**|  | [optional] 

### Return type

[**PricetickerbarapiAddTickerResponse**](PricetickerbarapiAddTickerResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_ticker**
> PricetickerbarapiDeleteTickerResponse delete_ticker(userid=userid, interfacekey=interfacekey, market=market)

Deletes the ticker

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.PriceTickerBarAPIApi()
userid = 'userid_example' # str |  (optional)
interfacekey = 'interfacekey_example' # str |  (optional)
market = 'market_example' # str |  (optional)

try:
    # Deletes the ticker
    api_response = api_instance.delete_ticker(userid=userid, interfacekey=interfacekey, market=market)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PriceTickerBarAPIApi->delete_ticker: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **userid** | **str**|  | [optional] 
 **interfacekey** | **str**|  | [optional] 
 **market** | **str**|  | [optional] 

### Return type

[**PricetickerbarapiDeleteTickerResponse**](PricetickerbarapiDeleteTickerResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **edit_ticker**
> PricetickerbarapiEditTickerResponse edit_ticker(userid=userid, interfacekey=interfacekey, market=market, interval=interval, style=style)

Edits properties of the given price ticker

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.PriceTickerBarAPIApi()
userid = 'userid_example' # str |  (optional)
interfacekey = 'interfacekey_example' # str |  (optional)
market = 'market_example' # str |  (optional)
interval = 56 # int |  (optional)
style = 56 # int |  (optional)

try:
    # Edits properties of the given price ticker
    api_response = api_instance.edit_ticker(userid=userid, interfacekey=interfacekey, market=market, interval=interval, style=style)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PriceTickerBarAPIApi->edit_ticker: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **userid** | **str**|  | [optional] 
 **interfacekey** | **str**|  | [optional] 
 **market** | **str**|  | [optional] 
 **interval** | **int**|  | [optional] 
 **style** | **int**|  | [optional] 

### Return type

[**PricetickerbarapiEditTickerResponse**](PricetickerbarapiEditTickerResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_tickers**
> PricetickerbarapiGetTickersResponse get_tickers(userid=userid, interfacekey=interfacekey)

Return the user ist price ticker bar

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.PriceTickerBarAPIApi()
userid = 'userid_example' # str |  (optional)
interfacekey = 'interfacekey_example' # str |  (optional)

try:
    # Return the user ist price ticker bar
    api_response = api_instance.get_tickers(userid=userid, interfacekey=interfacekey)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PriceTickerBarAPIApi->get_tickers: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **userid** | **str**|  | [optional] 
 **interfacekey** | **str**|  | [optional] 

### Return type

[**PricetickerbarapiGetTickersResponse**](PricetickerbarapiGetTickersResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

