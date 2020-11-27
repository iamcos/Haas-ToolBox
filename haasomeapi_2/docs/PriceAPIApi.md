# swagger_client.PriceAPIApi

All URIs are relative to *http://127.0.0.1:8090*

Method | HTTP request | Description
------------- | ------------- | -------------
[**all_markets**](PriceAPIApi.md#all_markets) | **POST** /PriceAPI.php?channel&#x3D;ALL_MARKETS | Returns a dictionary of the supported price sources and the markets they support
[**all_pricesources**](PriceAPIApi.md#all_pricesources) | **POST** /PriceAPI.php?channel&#x3D;ALL_PRICESOURCES | Returns a simple list of all the supported pricesources
[**coinlist**](PriceAPIApi.md#coinlist) | **POST** /PriceAPI.php?channel&#x3D;COINLIST | Returns a list of all the coins which are supported
[**deepticks**](PriceAPIApi.md#deepticks) | **POST** /PriceAPI.php?channel&#x3D;DEEPTICKS | Returns about 40,000 ticks of the last minutes
[**fiat_conversions**](PriceAPIApi.md#fiat_conversions) | **POST** /PriceAPI.php?channel&#x3D;FIAT_CONVERSIONS | Returns average a fiat conversion rates
[**get_chart**](PriceAPIApi.md#get_chart) | **POST** /PriceAPI.php?channel&#x3D;GET_CHART | Returns a basic chart with prices
[**get_exchange_price_change**](PriceAPIApi.md#get_exchange_price_change) | **POST** /PriceAPI.php?channel&#x3D;GET_EXCHANGE_PRICE_CHANGE | Returns list of price changes
[**get_history_compare_chart**](PriceAPIApi.md#get_history_compare_chart) | **POST** /PriceAPI.php?channel&#x3D;GET_HISTORY_COMPARE_CHART | Returns a price compare chart
[**get_spread_compare_chart**](PriceAPIApi.md#get_spread_compare_chart) | **POST** /PriceAPI.php?channel&#x3D;GET_SPREAD_COMPARE_CHART | Returns a price spread chart
[**get_volume_compare_chart**](PriceAPIApi.md#get_volume_compare_chart) | **POST** /PriceAPI.php?channel&#x3D;GET_VOLUME_COMPARE_CHART | Returns a volume compare chart
[**lastticks**](PriceAPIApi.md#lastticks) | **POST** /PriceAPI.php?channel&#x3D;LASTTICKS | Returns between 500 and 1440 ticks
[**lasttrades**](PriceAPIApi.md#lasttrades) | **POST** /PriceAPI.php?channel&#x3D;LASTTRADES | Returns the last trades
[**market_snapshot**](PriceAPIApi.md#market_snapshot) | **POST** /PriceAPI.php?channel&#x3D;MARKET_SNAPSHOT | Returns a snapshot of the very last prices (DO NOT USE!)
[**marketlist**](PriceAPIApi.md#marketlist) | **POST** /PriceAPI.php?channel&#x3D;MARKETLIST | Returns a list of all the markets which are supported
[**markets**](PriceAPIApi.md#markets) | **POST** /PriceAPI.php?channel&#x3D;MARKETS | Returns a list of the supported markets
[**new_coins**](PriceAPIApi.md#new_coins) | **POST** /PriceAPI.php?channel&#x3D;NEW_COINS | Returns a list of all the new coins which are supported
[**new_markets**](PriceAPIApi.md#new_markets) | **POST** /PriceAPI.php?channel&#x3D;NEW_MARKETS | Returns a list of all the new markets which are supported
[**orderbook**](PriceAPIApi.md#orderbook) | **POST** /PriceAPI.php?channel&#x3D;ORDERBOOK | Returns the orderbook
[**price**](PriceAPIApi.md#price) | **POST** /PriceAPI.php?channel&#x3D;PRICE | Returns the last price
[**pricepackage**](PriceAPIApi.md#pricepackage) | **POST** /PriceAPI.php?channel&#x3D;PRICEPACKAGE | Returns a full month of price ticks (per minute)
[**pricesources**](PriceAPIApi.md#pricesources) | **POST** /PriceAPI.php?channel&#x3D;PRICESOURCES | Returns a detailed list of all the supported pricesources
[**related_markets**](PriceAPIApi.md#related_markets) | **POST** /PriceAPI.php?channel&#x3D;RELATED_MARKETS | Returns a list of all related markets
[**related_prices**](PriceAPIApi.md#related_prices) | **POST** /PriceAPI.php?channel&#x3D;RELATED_PRICES | Returns a list of all related market prices
[**snapshot**](PriceAPIApi.md#snapshot) | **POST** /PriceAPI.php?channel&#x3D;SNAPSHOT | Returns a snapshot of the very last prices
[**syncticks**](PriceAPIApi.md#syncticks) | **POST** /PriceAPI.php?channel&#x3D;SYNCTICKS | Returns the 10 very last minutes
[**time**](PriceAPIApi.md#time) | **POST** /PriceAPI.php?channel&#x3D;TIME | Returns the servertime (UNIX-UTC)
[**unique_marketlist**](PriceAPIApi.md#unique_marketlist) | **POST** /PriceAPI.php?channel&#x3D;UNIQUE_MARKETLIST | Returns a list of all unique markets which are supported

# **all_markets**
> PriceapiAllMarketsResponse all_markets()

Returns a dictionary of the supported price sources and the markets they support

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.PriceAPIApi()

try:
    # Returns a dictionary of the supported price sources and the markets they support
    api_response = api_instance.all_markets()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PriceAPIApi->all_markets: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**PriceapiAllMarketsResponse**](PriceapiAllMarketsResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **all_pricesources**
> PriceapiAllPricesourcesResponse all_pricesources()

Returns a simple list of all the supported pricesources

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.PriceAPIApi()

try:
    # Returns a simple list of all the supported pricesources
    api_response = api_instance.all_pricesources()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PriceAPIApi->all_pricesources: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**PriceapiAllPricesourcesResponse**](PriceapiAllPricesourcesResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **coinlist**
> PriceapiCoinlistResponse coinlist()

Returns a list of all the coins which are supported

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.PriceAPIApi()

try:
    # Returns a list of all the coins which are supported
    api_response = api_instance.coinlist()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PriceAPIApi->coinlist: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**PriceapiCoinlistResponse**](PriceapiCoinlistResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **deepticks**
> PriceapiDeepticksResponse deepticks(market=market)

Returns about 40,000 ticks of the last minutes

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.PriceAPIApi()
market = 'market_example' # str |  (optional)

try:
    # Returns about 40,000 ticks of the last minutes
    api_response = api_instance.deepticks(market=market)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PriceAPIApi->deepticks: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **market** | **str**|  | [optional] 

### Return type

[**PriceapiDeepticksResponse**](PriceapiDeepticksResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **fiat_conversions**
> PriceapiFiatConversionsResponse fiat_conversions()

Returns average a fiat conversion rates

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.PriceAPIApi()

try:
    # Returns average a fiat conversion rates
    api_response = api_instance.fiat_conversions()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PriceAPIApi->fiat_conversions: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**PriceapiFiatConversionsResponse**](PriceapiFiatConversionsResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_chart**
> PriceapiGetChartResponse get_chart(market=market, interval=interval, style=style)

Returns a basic chart with prices

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.PriceAPIApi()
market = 'market_example' # str |  (optional)
interval = 56 # int |  (optional)
style = 56 # int |  (optional)

try:
    # Returns a basic chart with prices
    api_response = api_instance.get_chart(market=market, interval=interval, style=style)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PriceAPIApi->get_chart: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **market** | **str**|  | [optional] 
 **interval** | **int**|  | [optional] 
 **style** | **int**|  | [optional] 

### Return type

[**PriceapiGetChartResponse**](PriceapiGetChartResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_exchange_price_change**
> PriceapiGetExchangePriceChangeResponse get_exchange_price_change(pricesource=pricesource, hours=hours)

Returns list of price changes

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.PriceAPIApi()
pricesource = 'pricesource_example' # str |  (optional)
hours = 56 # int |  (optional)

try:
    # Returns list of price changes
    api_response = api_instance.get_exchange_price_change(pricesource=pricesource, hours=hours)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PriceAPIApi->get_exchange_price_change: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pricesource** | **str**|  | [optional] 
 **hours** | **int**|  | [optional] 

### Return type

[**PriceapiGetExchangePriceChangeResponse**](PriceapiGetExchangePriceChangeResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_history_compare_chart**
> PriceapiGetHistoryCompareChartResponse get_history_compare_chart(market=market)

Returns a price compare chart

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.PriceAPIApi()
market = 'market_example' # str |  (optional)

try:
    # Returns a price compare chart
    api_response = api_instance.get_history_compare_chart(market=market)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PriceAPIApi->get_history_compare_chart: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **market** | **str**|  | [optional] 

### Return type

[**PriceapiGetHistoryCompareChartResponse**](PriceapiGetHistoryCompareChartResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_spread_compare_chart**
> PriceapiGetSpreadCompareChartResponse get_spread_compare_chart(market=market)

Returns a price spread chart

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.PriceAPIApi()
market = 'market_example' # str |  (optional)

try:
    # Returns a price spread chart
    api_response = api_instance.get_spread_compare_chart(market=market)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PriceAPIApi->get_spread_compare_chart: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **market** | **str**|  | [optional] 

### Return type

[**PriceapiGetSpreadCompareChartResponse**](PriceapiGetSpreadCompareChartResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_volume_compare_chart**
> PriceapiGetVolumeCompareChartResponse get_volume_compare_chart(market=market)

Returns a volume compare chart

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.PriceAPIApi()
market = 'market_example' # str |  (optional)

try:
    # Returns a volume compare chart
    api_response = api_instance.get_volume_compare_chart(market=market)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PriceAPIApi->get_volume_compare_chart: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **market** | **str**|  | [optional] 

### Return type

[**PriceapiGetVolumeCompareChartResponse**](PriceapiGetVolumeCompareChartResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **lastticks**
> PriceapiLastticksResponse lastticks(market=market, interval=interval)

Returns between 500 and 1440 ticks

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.PriceAPIApi()
market = 'market_example' # str |  (optional)
interval = 56 # int |  (optional)

try:
    # Returns between 500 and 1440 ticks
    api_response = api_instance.lastticks(market=market, interval=interval)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PriceAPIApi->lastticks: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **market** | **str**|  | [optional] 
 **interval** | **int**|  | [optional] 

### Return type

[**PriceapiLastticksResponse**](PriceapiLastticksResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **lasttrades**
> PriceapiLasttradesResponse lasttrades(market=market)

Returns the last trades

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.PriceAPIApi()
market = 'market_example' # str |  (optional)

try:
    # Returns the last trades
    api_response = api_instance.lasttrades(market=market)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PriceAPIApi->lasttrades: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **market** | **str**|  | [optional] 

### Return type

[**PriceapiLasttradesResponse**](PriceapiLasttradesResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **market_snapshot**
> PriceapiMarketSnapshotResponse market_snapshot(market=market)

Returns a snapshot of the very last prices (DO NOT USE!)

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.PriceAPIApi()
market = 'market_example' # str |  (optional)

try:
    # Returns a snapshot of the very last prices (DO NOT USE!)
    api_response = api_instance.market_snapshot(market=market)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PriceAPIApi->market_snapshot: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **market** | **str**|  | [optional] 

### Return type

[**PriceapiMarketSnapshotResponse**](PriceapiMarketSnapshotResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **marketlist**
> PriceapiMarketlistResponse marketlist()

Returns a list of all the markets which are supported

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.PriceAPIApi()

try:
    # Returns a list of all the markets which are supported
    api_response = api_instance.marketlist()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PriceAPIApi->marketlist: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**PriceapiMarketlistResponse**](PriceapiMarketlistResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **markets**
> PriceapiMarketsResponse markets(pricesource=pricesource)

Returns a list of the supported markets

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.PriceAPIApi()
pricesource = 'pricesource_example' # str |  (optional)

try:
    # Returns a list of the supported markets
    api_response = api_instance.markets(pricesource=pricesource)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PriceAPIApi->markets: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pricesource** | **str**|  | [optional] 

### Return type

[**PriceapiMarketsResponse**](PriceapiMarketsResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **new_coins**
> PriceapiNewCoinsResponse new_coins()

Returns a list of all the new coins which are supported

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.PriceAPIApi()

try:
    # Returns a list of all the new coins which are supported
    api_response = api_instance.new_coins()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PriceAPIApi->new_coins: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**PriceapiNewCoinsResponse**](PriceapiNewCoinsResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **new_markets**
> PriceapiNewMarketsResponse new_markets()

Returns a list of all the new markets which are supported

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.PriceAPIApi()

try:
    # Returns a list of all the new markets which are supported
    api_response = api_instance.new_markets()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PriceAPIApi->new_markets: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**PriceapiNewMarketsResponse**](PriceapiNewMarketsResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **orderbook**
> PriceapiOrderbookResponse orderbook(market=market)

Returns the orderbook

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.PriceAPIApi()
market = 'market_example' # str |  (optional)

try:
    # Returns the orderbook
    api_response = api_instance.orderbook(market=market)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PriceAPIApi->orderbook: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **market** | **str**|  | [optional] 

### Return type

[**PriceapiOrderbookResponse**](PriceapiOrderbookResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **price**
> PriceapiPriceResponse price(market=market)

Returns the last price

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.PriceAPIApi()
market = 'market_example' # str |  (optional)

try:
    # Returns the last price
    api_response = api_instance.price(market=market)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PriceAPIApi->price: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **market** | **str**|  | [optional] 

### Return type

[**PriceapiPriceResponse**](PriceapiPriceResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **pricepackage**
> PriceapiPricepackageResponse pricepackage(userid=userid, interfacekey=interfacekey, nonce=nonce, market=market, year=year, month=month)

Returns a full month of price ticks (per minute)

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.PriceAPIApi()
userid = 'userid_example' # str |  (optional)
interfacekey = 'interfacekey_example' # str |  (optional)
nonce = swagger_client.Int64() # Int64 |  (optional)
market = 'market_example' # str |  (optional)
year = 56 # int |  (optional)
month = 56 # int |  (optional)

try:
    # Returns a full month of price ticks (per minute)
    api_response = api_instance.pricepackage(userid=userid, interfacekey=interfacekey, nonce=nonce, market=market, year=year, month=month)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PriceAPIApi->pricepackage: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **userid** | **str**|  | [optional] 
 **interfacekey** | **str**|  | [optional] 
 **nonce** | [**Int64**](.md)|  | [optional] 
 **market** | **str**|  | [optional] 
 **year** | **int**|  | [optional] 
 **month** | **int**|  | [optional] 

### Return type

[**PriceapiPricepackageResponse**](PriceapiPricepackageResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **pricesources**
> PriceapiPricesourcesResponse pricesources()

Returns a detailed list of all the supported pricesources

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.PriceAPIApi()

try:
    # Returns a detailed list of all the supported pricesources
    api_response = api_instance.pricesources()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PriceAPIApi->pricesources: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**PriceapiPricesourcesResponse**](PriceapiPricesourcesResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **related_markets**
> PriceapiRelatedMarketsResponse related_markets(market=market)

Returns a list of all related markets

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.PriceAPIApi()
market = 'market_example' # str |  (optional)

try:
    # Returns a list of all related markets
    api_response = api_instance.related_markets(market=market)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PriceAPIApi->related_markets: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **market** | **str**|  | [optional] 

### Return type

[**PriceapiRelatedMarketsResponse**](PriceapiRelatedMarketsResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **related_prices**
> PriceapiRelatedPricesResponse related_prices(market=market)

Returns a list of all related market prices

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.PriceAPIApi()
market = 'market_example' # str |  (optional)

try:
    # Returns a list of all related market prices
    api_response = api_instance.related_prices(market=market)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PriceAPIApi->related_prices: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **market** | **str**|  | [optional] 

### Return type

[**PriceapiRelatedPricesResponse**](PriceapiRelatedPricesResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **snapshot**
> PriceapiSnapshotResponse snapshot(pricesource=pricesource)

Returns a snapshot of the very last prices

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.PriceAPIApi()
pricesource = 'pricesource_example' # str |  (optional)

try:
    # Returns a snapshot of the very last prices
    api_response = api_instance.snapshot(pricesource=pricesource)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PriceAPIApi->snapshot: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pricesource** | **str**|  | [optional] 

### Return type

[**PriceapiSnapshotResponse**](PriceapiSnapshotResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **syncticks**
> PriceapiSyncticksResponse syncticks(market=market)

Returns the 10 very last minutes

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.PriceAPIApi()
market = 'market_example' # str |  (optional)

try:
    # Returns the 10 very last minutes
    api_response = api_instance.syncticks(market=market)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PriceAPIApi->syncticks: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **market** | **str**|  | [optional] 

### Return type

[**PriceapiSyncticksResponse**](PriceapiSyncticksResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **time**
> PriceapiTimeResponse time()

Returns the servertime (UNIX-UTC)

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.PriceAPIApi()

try:
    # Returns the servertime (UNIX-UTC)
    api_response = api_instance.time()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PriceAPIApi->time: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**PriceapiTimeResponse**](PriceapiTimeResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **unique_marketlist**
> PriceapiUniqueMarketlistResponse unique_marketlist()

Returns a list of all unique markets which are supported

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.PriceAPIApi()

try:
    # Returns a list of all unique markets which are supported
    api_response = api_instance.unique_marketlist()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PriceAPIApi->unique_marketlist: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**PriceapiUniqueMarketlistResponse**](PriceapiUniqueMarketlistResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

