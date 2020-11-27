# swagger_client.PortfolioAPIApi

All URIs are relative to *http://127.0.0.1:8090*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_account_balance**](PortfolioAPIApi.md#get_account_balance) | **POST** /PortfolioAPI.php?channel&#x3D;GET_ACCOUNT_BALANCE | Returns the portofolio per account
[**get_account_chart**](PortfolioAPIApi.md#get_account_chart) | **POST** /PortfolioAPI.php?channel&#x3D;GET_ACCOUNT_CHART | Returns the chart for the account
[**get_balance**](PortfolioAPIApi.md#get_balance) | **POST** /PortfolioAPI.php?channel&#x3D;GET_BALANCE | Returns the wallet and total balance
[**get_coin_balance**](PortfolioAPIApi.md#get_coin_balance) | **POST** /PortfolioAPI.php?channel&#x3D;GET_COIN_BALANCE | Returns the portofolio per coin
[**get_currency_chart**](PortfolioAPIApi.md#get_currency_chart) | **POST** /PortfolioAPI.php?channel&#x3D;GET_CURRENCY_CHART | Returns the chart for the currencies
[**get_portfolio_account_chart**](PortfolioAPIApi.md#get_portfolio_account_chart) | **POST** /PortfolioAPI.php?channel&#x3D;GET_PORTFOLIO_ACCOUNT_CHART | Returns the chart for the portofolio
[**get_portfolio_balance**](PortfolioAPIApi.md#get_portfolio_balance) | **POST** /PortfolioAPI.php?channel&#x3D;GET_PORTFOLIO_BALANCE | Returns the portofolio
[**get_portfolio_coins_chart**](PortfolioAPIApi.md#get_portfolio_coins_chart) | **POST** /PortfolioAPI.php?channel&#x3D;GET_PORTFOLIO_COINS_CHART | Returns the chart for the coins

# **get_account_balance**
> PortfolioapiGetAccountBalanceResponse get_account_balance(userid=userid, interfacekey=interfacekey, accountid=accountid, currency=currency, timestamp=timestamp)

Returns the portofolio per account

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.PortfolioAPIApi()
userid = 'userid_example' # str |  (optional)
interfacekey = 'interfacekey_example' # str |  (optional)
accountid = 'accountid_example' # str |  (optional)
currency = 'currency_example' # str |  (optional)
timestamp = 56 # int |  (optional)

try:
    # Returns the portofolio per account
    api_response = api_instance.get_account_balance(userid=userid, interfacekey=interfacekey, accountid=accountid, currency=currency, timestamp=timestamp)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PortfolioAPIApi->get_account_balance: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **userid** | **str**|  | [optional] 
 **interfacekey** | **str**|  | [optional] 
 **accountid** | **str**|  | [optional] 
 **currency** | **str**|  | [optional] 
 **timestamp** | **int**|  | [optional] 

### Return type

[**PortfolioapiGetAccountBalanceResponse**](PortfolioapiGetAccountBalanceResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_account_chart**
> PortfolioapiGetAccountChartResponse get_account_chart(userid=userid, interfacekey=interfacekey, accountid=accountid, currency=currency, interval=interval, style=style)

Returns the chart for the account

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.PortfolioAPIApi()
userid = 'userid_example' # str |  (optional)
interfacekey = 'interfacekey_example' # str |  (optional)
accountid = 'accountid_example' # str |  (optional)
currency = 'currency_example' # str |  (optional)
interval = 56 # int |  (optional)
style = NULL # object |  (optional)

try:
    # Returns the chart for the account
    api_response = api_instance.get_account_chart(userid=userid, interfacekey=interfacekey, accountid=accountid, currency=currency, interval=interval, style=style)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PortfolioAPIApi->get_account_chart: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **userid** | **str**|  | [optional] 
 **interfacekey** | **str**|  | [optional] 
 **accountid** | **str**|  | [optional] 
 **currency** | **str**|  | [optional] 
 **interval** | **int**|  | [optional] 
 **style** | [**object**](.md)|  | [optional] 

### Return type

[**PortfolioapiGetAccountChartResponse**](PortfolioapiGetAccountChartResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_balance**
> PortfolioapiGetBalanceResponse get_balance(userid=userid, interfacekey=interfacekey, currency=currency, accountid=accountid)

Returns the wallet and total balance

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.PortfolioAPIApi()
userid = 'userid_example' # str |  (optional)
interfacekey = 'interfacekey_example' # str |  (optional)
currency = 'currency_example' # str |  (optional)
accountid = 'accountid_example' # str |  (optional)

try:
    # Returns the wallet and total balance
    api_response = api_instance.get_balance(userid=userid, interfacekey=interfacekey, currency=currency, accountid=accountid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PortfolioAPIApi->get_balance: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **userid** | **str**|  | [optional] 
 **interfacekey** | **str**|  | [optional] 
 **currency** | **str**|  | [optional] 
 **accountid** | **str**|  | [optional] 

### Return type

[**PortfolioapiGetBalanceResponse**](PortfolioapiGetBalanceResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_coin_balance**
> PortfolioapiGetCoinBalanceResponse get_coin_balance(userid=userid, interfacekey=interfacekey, coin=coin, currency=currency, timestamp=timestamp)

Returns the portofolio per coin

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.PortfolioAPIApi()
userid = 'userid_example' # str |  (optional)
interfacekey = 'interfacekey_example' # str |  (optional)
coin = 'coin_example' # str |  (optional)
currency = 'currency_example' # str |  (optional)
timestamp = 56 # int |  (optional)

try:
    # Returns the portofolio per coin
    api_response = api_instance.get_coin_balance(userid=userid, interfacekey=interfacekey, coin=coin, currency=currency, timestamp=timestamp)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PortfolioAPIApi->get_coin_balance: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **userid** | **str**|  | [optional] 
 **interfacekey** | **str**|  | [optional] 
 **coin** | **str**|  | [optional] 
 **currency** | **str**|  | [optional] 
 **timestamp** | **int**|  | [optional] 

### Return type

[**PortfolioapiGetCoinBalanceResponse**](PortfolioapiGetCoinBalanceResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_currency_chart**
> PortfolioapiGetCurrencyChartResponse get_currency_chart(userid=userid, interfacekey=interfacekey, coin=coin, currency=currency, interval=interval, style=style)

Returns the chart for the currencies

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.PortfolioAPIApi()
userid = 'userid_example' # str |  (optional)
interfacekey = 'interfacekey_example' # str |  (optional)
coin = 'coin_example' # str |  (optional)
currency = 'currency_example' # str |  (optional)
interval = 56 # int |  (optional)
style = NULL # object |  (optional)

try:
    # Returns the chart for the currencies
    api_response = api_instance.get_currency_chart(userid=userid, interfacekey=interfacekey, coin=coin, currency=currency, interval=interval, style=style)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PortfolioAPIApi->get_currency_chart: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **userid** | **str**|  | [optional] 
 **interfacekey** | **str**|  | [optional] 
 **coin** | **str**|  | [optional] 
 **currency** | **str**|  | [optional] 
 **interval** | **int**|  | [optional] 
 **style** | [**object**](.md)|  | [optional] 

### Return type

[**PortfolioapiGetCurrencyChartResponse**](PortfolioapiGetCurrencyChartResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_portfolio_account_chart**
> PortfolioapiGetPortfolioAccountChartResponse get_portfolio_account_chart(userid=userid, interfacekey=interfacekey, currency=currency, interval=interval, style=style)

Returns the chart for the portofolio

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.PortfolioAPIApi()
userid = 'userid_example' # str |  (optional)
interfacekey = 'interfacekey_example' # str |  (optional)
currency = 'currency_example' # str |  (optional)
interval = 56 # int |  (optional)
style = NULL # object |  (optional)

try:
    # Returns the chart for the portofolio
    api_response = api_instance.get_portfolio_account_chart(userid=userid, interfacekey=interfacekey, currency=currency, interval=interval, style=style)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PortfolioAPIApi->get_portfolio_account_chart: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **userid** | **str**|  | [optional] 
 **interfacekey** | **str**|  | [optional] 
 **currency** | **str**|  | [optional] 
 **interval** | **int**|  | [optional] 
 **style** | [**object**](.md)|  | [optional] 

### Return type

[**PortfolioapiGetPortfolioAccountChartResponse**](PortfolioapiGetPortfolioAccountChartResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_portfolio_balance**
> PortfolioapiGetPortfolioBalanceResponse get_portfolio_balance(userid=userid, interfacekey=interfacekey, currency=currency, timestamp=timestamp)

Returns the portofolio

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.PortfolioAPIApi()
userid = 'userid_example' # str |  (optional)
interfacekey = 'interfacekey_example' # str |  (optional)
currency = 'currency_example' # str |  (optional)
timestamp = 56 # int |  (optional)

try:
    # Returns the portofolio
    api_response = api_instance.get_portfolio_balance(userid=userid, interfacekey=interfacekey, currency=currency, timestamp=timestamp)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PortfolioAPIApi->get_portfolio_balance: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **userid** | **str**|  | [optional] 
 **interfacekey** | **str**|  | [optional] 
 **currency** | **str**|  | [optional] 
 **timestamp** | **int**|  | [optional] 

### Return type

[**PortfolioapiGetPortfolioBalanceResponse**](PortfolioapiGetPortfolioBalanceResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_portfolio_coins_chart**
> PortfolioapiGetPortfolioCoinsChartResponse get_portfolio_coins_chart(userid=userid, interfacekey=interfacekey, currency=currency, interval=interval, style=style)

Returns the chart for the coins

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.PortfolioAPIApi()
userid = 'userid_example' # str |  (optional)
interfacekey = 'interfacekey_example' # str |  (optional)
currency = 'currency_example' # str |  (optional)
interval = 56 # int |  (optional)
style = NULL # object |  (optional)

try:
    # Returns the chart for the coins
    api_response = api_instance.get_portfolio_coins_chart(userid=userid, interfacekey=interfacekey, currency=currency, interval=interval, style=style)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PortfolioAPIApi->get_portfolio_coins_chart: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **userid** | **str**|  | [optional] 
 **interfacekey** | **str**|  | [optional] 
 **currency** | **str**|  | [optional] 
 **interval** | **int**|  | [optional] 
 **style** | [**object**](.md)|  | [optional] 

### Return type

[**PortfolioapiGetPortfolioCoinsChartResponse**](PortfolioapiGetPortfolioCoinsChartResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

