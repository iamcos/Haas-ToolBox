# swagger_client.BotAPIApi

All URIs are relative to *http://127.0.0.1:8090*

Method | HTTP request | Description
------------- | ------------- | -------------
[**activate_bot**](BotAPIApi.md#activate_bot) | **POST** /BotAPI.php?channel&#x3D;ACTIVATE_BOT | Activates the given bot
[**add_bot**](BotAPIApi.md#add_bot) | **POST** /BotAPI.php?channel&#x3D;ADD_BOT | Add a new bot
[**add_bot_from_backtest**](BotAPIApi.md#add_bot_from_backtest) | **POST** /BotAPI.php?channel&#x3D;ADD_BOT_FROM_BACKTEST | Add a new bot from a backtest result
[**adjust_position**](BotAPIApi.md#adjust_position) | **POST** /BotAPI.php?channel&#x3D;ADJUST_POSITION | Changes a bot its open position details
[**cancel_all_orders**](BotAPIApi.md#cancel_all_orders) | **POST** /BotAPI.php?channel&#x3D;CANCEL_ALL_ORDERS | Cancels all bot orders (manually)
[**cancel_order**](BotAPIApi.md#cancel_order) | **POST** /BotAPI.php?channel&#x3D;CANCEL_ORDER | Cancels a bot order (manually)
[**clean_bot**](BotAPIApi.md#clean_bot) | **POST** /BotAPI.php?channel&#x3D;CLEAN_BOT | Cleans the bot its logbook and trades
[**clone_bot**](BotAPIApi.md#clone_bot) | **POST** /BotAPI.php?channel&#x3D;CLONE_BOT | Clones a excisting bot
[**close_position**](BotAPIApi.md#close_position) | **POST** /BotAPI.php?channel&#x3D;CLOSE_POSITION | Closes a bot position (manually)
[**deactivate_bot**](BotAPIApi.md#deactivate_bot) | **POST** /BotAPI.php?channel&#x3D;DEACTIVATE_BOT | Deactivates the given bot
[**delete_bot**](BotAPIApi.md#delete_bot) | **POST** /BotAPI.php?channel&#x3D;DELETE_BOT | Deletes/removes the given bot
[**edit_script**](BotAPIApi.md#edit_script) | **POST** /BotAPI.php?channel&#x3D;EDIT_SCRIPT | Edits the bots its script
[**edit_settings**](BotAPIApi.md#edit_settings) | **POST** /BotAPI.php?channel&#x3D;EDIT_SETTINGS | Edits the bots its settings
[**favorite_bot**](BotAPIApi.md#favorite_bot) | **POST** /BotAPI.php?channel&#x3D;FAVORITE_BOT | Makes a bot a favorite bot
[**get_bot**](BotAPIApi.md#get_bot) | **POST** /BotAPI.php?channel&#x3D;GET_BOT | Returns the requested bot
[**get_bots**](BotAPIApi.md#get_bots) | **POST** /BotAPI.php?channel&#x3D;GET_BOTS | Returns all the user its bots
[**get_chart**](BotAPIApi.md#get_chart) | **POST** /BotAPI.php?channel&#x3D;GET_CHART | Returns the bots its rendered runtime chart
[**get_full_logbook**](BotAPIApi.md#get_full_logbook) | **POST** /BotAPI.php?channel&#x3D;GET_FULL_LOGBOOK | Returns the bots its full logbook
[**get_logbook**](BotAPIApi.md#get_logbook) | **POST** /BotAPI.php?channel&#x3D;GET_LOGBOOK | Returns the bots its message logbook
[**get_open_orders**](BotAPIApi.md#get_open_orders) | **POST** /BotAPI.php?channel&#x3D;GET_OPEN_ORDERS | Returns all the open bot orders
[**get_open_positions**](BotAPIApi.md#get_open_positions) | **POST** /BotAPI.php?channel&#x3D;GET_OPEN_POSITIONS | Returns all the open bot positions
[**get_runtime**](BotAPIApi.md#get_runtime) | **POST** /BotAPI.php?channel&#x3D;GET_RUNTIME | Returns the bots its runtime
[**get_runtime_logbook**](BotAPIApi.md#get_runtime_logbook) | **POST** /BotAPI.php?channel&#x3D;GET_RUNTIME_LOGBOOK | Returns the bots its recent logbook
[**rename_bot**](BotAPIApi.md#rename_bot) | **POST** /BotAPI.php?channel&#x3D;RENAME_BOT | Renames the bot

# **activate_bot**
> BotapiActivateBotResponse activate_bot(userid=userid, interfacekey=interfacekey, botid=botid)

Activates the given bot

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.BotAPIApi()
userid = 'userid_example' # str |  (optional)
interfacekey = 'interfacekey_example' # str |  (optional)
botid = 'botid_example' # str |  (optional)

try:
    # Activates the given bot
    api_response = api_instance.activate_bot(userid=userid, interfacekey=interfacekey, botid=botid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BotAPIApi->activate_bot: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **userid** | **str**|  | [optional] 
 **interfacekey** | **str**|  | [optional] 
 **botid** | **str**|  | [optional] 

### Return type

[**BotapiActivateBotResponse**](BotapiActivateBotResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **add_bot**
> BotapiAddBotResponse add_bot(userid=userid, interfacekey=interfacekey, botname=botname, scriptid=scriptid, scripttype=scripttype, accountid=accountid, market=market, leverage=leverage)

Add a new bot

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.BotAPIApi()
userid = 'userid_example' # str |  (optional)
interfacekey = 'interfacekey_example' # str |  (optional)
botname = 'botname_example' # str |  (optional)
scriptid = 'scriptid_example' # str |  (optional)
scripttype = 56 # int |  (optional)
accountid = 'accountid_example' # str |  (optional)
market = 'market_example' # str |  (optional)
leverage = 1.2 # float |  (optional)

try:
    # Add a new bot
    api_response = api_instance.add_bot(userid=userid, interfacekey=interfacekey, botname=botname, scriptid=scriptid, scripttype=scripttype, accountid=accountid, market=market, leverage=leverage)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BotAPIApi->add_bot: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **userid** | **str**|  | [optional] 
 **interfacekey** | **str**|  | [optional] 
 **botname** | **str**|  | [optional] 
 **scriptid** | **str**|  | [optional] 
 **scripttype** | **int**|  | [optional] 
 **accountid** | **str**|  | [optional] 
 **market** | **str**|  | [optional] 
 **leverage** | **float**|  | [optional] 

### Return type

[**BotapiAddBotResponse**](BotapiAddBotResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **add_bot_from_backtest**
> BotapiAddBotFromBacktestResponse add_bot_from_backtest(userid=userid, interfacekey=interfacekey, backtestid=backtestid, botname=botname, accountid=accountid, market=market)

Add a new bot from a backtest result

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.BotAPIApi()
userid = 'userid_example' # str |  (optional)
interfacekey = 'interfacekey_example' # str |  (optional)
backtestid = 'backtestid_example' # str |  (optional)
botname = 'botname_example' # str |  (optional)
accountid = 'accountid_example' # str |  (optional)
market = 'market_example' # str |  (optional)

try:
    # Add a new bot from a backtest result
    api_response = api_instance.add_bot_from_backtest(userid=userid, interfacekey=interfacekey, backtestid=backtestid, botname=botname, accountid=accountid, market=market)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BotAPIApi->add_bot_from_backtest: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **userid** | **str**|  | [optional] 
 **interfacekey** | **str**|  | [optional] 
 **backtestid** | **str**|  | [optional] 
 **botname** | **str**|  | [optional] 
 **accountid** | **str**|  | [optional] 
 **market** | **str**|  | [optional] 

### Return type

[**BotapiAddBotFromBacktestResponse**](BotapiAddBotFromBacktestResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **adjust_position**
> BotapiAdjustPositionResponse adjust_position(userid=userid, interfacekey=interfacekey, botid=botid, positionid=positionid, price=price, amount=amount)

Changes a bot its open position details

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.BotAPIApi()
userid = 'userid_example' # str |  (optional)
interfacekey = 'interfacekey_example' # str |  (optional)
botid = 'botid_example' # str |  (optional)
positionid = 'positionid_example' # str |  (optional)
price = 1.2 # float |  (optional)
amount = 1.2 # float |  (optional)

try:
    # Changes a bot its open position details
    api_response = api_instance.adjust_position(userid=userid, interfacekey=interfacekey, botid=botid, positionid=positionid, price=price, amount=amount)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BotAPIApi->adjust_position: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **userid** | **str**|  | [optional] 
 **interfacekey** | **str**|  | [optional] 
 **botid** | **str**|  | [optional] 
 **positionid** | **str**|  | [optional] 
 **price** | **float**|  | [optional] 
 **amount** | **float**|  | [optional] 

### Return type

[**BotapiAdjustPositionResponse**](BotapiAdjustPositionResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **cancel_all_orders**
> BotapiCancelAllOrdersResponse cancel_all_orders(userid=userid, interfacekey=interfacekey, botid=botid)

Cancels all bot orders (manually)

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.BotAPIApi()
userid = 'userid_example' # str |  (optional)
interfacekey = 'interfacekey_example' # str |  (optional)
botid = 'botid_example' # str |  (optional)

try:
    # Cancels all bot orders (manually)
    api_response = api_instance.cancel_all_orders(userid=userid, interfacekey=interfacekey, botid=botid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BotAPIApi->cancel_all_orders: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **userid** | **str**|  | [optional] 
 **interfacekey** | **str**|  | [optional] 
 **botid** | **str**|  | [optional] 

### Return type

[**BotapiCancelAllOrdersResponse**](BotapiCancelAllOrdersResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **cancel_order**
> BotapiCancelOrderResponse cancel_order(userid=userid, interfacekey=interfacekey, botid=botid, orderid=orderid)

Cancels a bot order (manually)

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.BotAPIApi()
userid = 'userid_example' # str |  (optional)
interfacekey = 'interfacekey_example' # str |  (optional)
botid = 'botid_example' # str |  (optional)
orderid = 'orderid_example' # str |  (optional)

try:
    # Cancels a bot order (manually)
    api_response = api_instance.cancel_order(userid=userid, interfacekey=interfacekey, botid=botid, orderid=orderid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BotAPIApi->cancel_order: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **userid** | **str**|  | [optional] 
 **interfacekey** | **str**|  | [optional] 
 **botid** | **str**|  | [optional] 
 **orderid** | **str**|  | [optional] 

### Return type

[**BotapiCancelOrderResponse**](BotapiCancelOrderResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **clean_bot**
> BotapiCleanBotResponse clean_bot(userid=userid, interfacekey=interfacekey, botid=botid)

Cleans the bot its logbook and trades

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.BotAPIApi()
userid = 'userid_example' # str |  (optional)
interfacekey = 'interfacekey_example' # str |  (optional)
botid = 'botid_example' # str |  (optional)

try:
    # Cleans the bot its logbook and trades
    api_response = api_instance.clean_bot(userid=userid, interfacekey=interfacekey, botid=botid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BotAPIApi->clean_bot: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **userid** | **str**|  | [optional] 
 **interfacekey** | **str**|  | [optional] 
 **botid** | **str**|  | [optional] 

### Return type

[**BotapiCleanBotResponse**](BotapiCleanBotResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **clone_bot**
> BotapiCloneBotResponse clone_bot(userid=userid, interfacekey=interfacekey, botid=botid, botname=botname)

Clones a excisting bot

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.BotAPIApi()
userid = 'userid_example' # str |  (optional)
interfacekey = 'interfacekey_example' # str |  (optional)
botid = 'botid_example' # str |  (optional)
botname = 'botname_example' # str |  (optional)

try:
    # Clones a excisting bot
    api_response = api_instance.clone_bot(userid=userid, interfacekey=interfacekey, botid=botid, botname=botname)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BotAPIApi->clone_bot: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **userid** | **str**|  | [optional] 
 **interfacekey** | **str**|  | [optional] 
 **botid** | **str**|  | [optional] 
 **botname** | **str**|  | [optional] 

### Return type

[**BotapiCloneBotResponse**](BotapiCloneBotResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **close_position**
> BotapiClosePositionResponse close_position(userid=userid, interfacekey=interfacekey, botid=botid, positionid=positionid)

Closes a bot position (manually)

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.BotAPIApi()
userid = 'userid_example' # str |  (optional)
interfacekey = 'interfacekey_example' # str |  (optional)
botid = 'botid_example' # str |  (optional)
positionid = 'positionid_example' # str |  (optional)

try:
    # Closes a bot position (manually)
    api_response = api_instance.close_position(userid=userid, interfacekey=interfacekey, botid=botid, positionid=positionid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BotAPIApi->close_position: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **userid** | **str**|  | [optional] 
 **interfacekey** | **str**|  | [optional] 
 **botid** | **str**|  | [optional] 
 **positionid** | **str**|  | [optional] 

### Return type

[**BotapiClosePositionResponse**](BotapiClosePositionResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **deactivate_bot**
> BotapiDeactivateBotResponse deactivate_bot(userid=userid, interfacekey=interfacekey, botid=botid)

Deactivates the given bot

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.BotAPIApi()
userid = 'userid_example' # str |  (optional)
interfacekey = 'interfacekey_example' # str |  (optional)
botid = 'botid_example' # str |  (optional)

try:
    # Deactivates the given bot
    api_response = api_instance.deactivate_bot(userid=userid, interfacekey=interfacekey, botid=botid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BotAPIApi->deactivate_bot: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **userid** | **str**|  | [optional] 
 **interfacekey** | **str**|  | [optional] 
 **botid** | **str**|  | [optional] 

### Return type

[**BotapiDeactivateBotResponse**](BotapiDeactivateBotResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_bot**
> BotapiDeleteBotResponse delete_bot(userid=userid, interfacekey=interfacekey, botid=botid)

Deletes/removes the given bot

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.BotAPIApi()
userid = 'userid_example' # str |  (optional)
interfacekey = 'interfacekey_example' # str |  (optional)
botid = 'botid_example' # str |  (optional)

try:
    # Deletes/removes the given bot
    api_response = api_instance.delete_bot(userid=userid, interfacekey=interfacekey, botid=botid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BotAPIApi->delete_bot: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **userid** | **str**|  | [optional] 
 **interfacekey** | **str**|  | [optional] 
 **botid** | **str**|  | [optional] 

### Return type

[**BotapiDeleteBotResponse**](BotapiDeleteBotResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **edit_script**
> BotapiEditScriptResponse edit_script(userid=userid, interfacekey=interfacekey, botid=botid, scriptid=scriptid, scripttype=scripttype)

Edits the bots its script

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.BotAPIApi()
userid = 'userid_example' # str |  (optional)
interfacekey = 'interfacekey_example' # str |  (optional)
botid = 'botid_example' # str |  (optional)
scriptid = 'scriptid_example' # str |  (optional)
scripttype = 56 # int |  (optional)

try:
    # Edits the bots its script
    api_response = api_instance.edit_script(userid=userid, interfacekey=interfacekey, botid=botid, scriptid=scriptid, scripttype=scripttype)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BotAPIApi->edit_script: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **userid** | **str**|  | [optional] 
 **interfacekey** | **str**|  | [optional] 
 **botid** | **str**|  | [optional] 
 **scriptid** | **str**|  | [optional] 
 **scripttype** | **int**|  | [optional] 

### Return type

[**BotapiEditScriptResponse**](BotapiEditScriptResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **edit_settings**
> BotapiEditSettingsResponse edit_settings(userid=userid, interfacekey=interfacekey, botid=botid, settings=settings)

Edits the bots its settings

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.BotAPIApi()
userid = 'userid_example' # str |  (optional)
interfacekey = 'interfacekey_example' # str |  (optional)
botid = 'botid_example' # str |  (optional)
settings = NULL # object |  (optional)

try:
    # Edits the bots its settings
    api_response = api_instance.edit_settings(userid=userid, interfacekey=interfacekey, botid=botid, settings=settings)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BotAPIApi->edit_settings: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **userid** | **str**|  | [optional] 
 **interfacekey** | **str**|  | [optional] 
 **botid** | **str**|  | [optional] 
 **settings** | [**object**](.md)|  | [optional] 

### Return type

[**BotapiEditSettingsResponse**](BotapiEditSettingsResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **favorite_bot**
> BotapiFavoriteBotResponse favorite_bot(userid=userid, interfacekey=interfacekey, botid=botid, isfavorite=isfavorite)

Makes a bot a favorite bot

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.BotAPIApi()
userid = 'userid_example' # str |  (optional)
interfacekey = 'interfacekey_example' # str |  (optional)
botid = 'botid_example' # str |  (optional)
isfavorite = true # bool |  (optional)

try:
    # Makes a bot a favorite bot
    api_response = api_instance.favorite_bot(userid=userid, interfacekey=interfacekey, botid=botid, isfavorite=isfavorite)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BotAPIApi->favorite_bot: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **userid** | **str**|  | [optional] 
 **interfacekey** | **str**|  | [optional] 
 **botid** | **str**|  | [optional] 
 **isfavorite** | **bool**|  | [optional] 

### Return type

[**BotapiFavoriteBotResponse**](BotapiFavoriteBotResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_bot**
> BotapiGetBotResponse get_bot(userid=userid, interfacekey=interfacekey, botid=botid)

Returns the requested bot

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.BotAPIApi()
userid = 'userid_example' # str |  (optional)
interfacekey = 'interfacekey_example' # str |  (optional)
botid = 'botid_example' # str |  (optional)

try:
    # Returns the requested bot
    api_response = api_instance.get_bot(userid=userid, interfacekey=interfacekey, botid=botid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BotAPIApi->get_bot: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **userid** | **str**|  | [optional] 
 **interfacekey** | **str**|  | [optional] 
 **botid** | **str**|  | [optional] 

### Return type

[**BotapiGetBotResponse**](BotapiGetBotResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_bots**
> BotapiGetBotsResponse get_bots(userid=userid, interfacekey=interfacekey)

Returns all the user its bots

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.BotAPIApi()
userid = 'userid_example' # str |  (optional)
interfacekey = 'interfacekey_example' # str |  (optional)

try:
    # Returns all the user its bots
    api_response = api_instance.get_bots(userid=userid, interfacekey=interfacekey)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BotAPIApi->get_bots: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **userid** | **str**|  | [optional] 
 **interfacekey** | **str**|  | [optional] 

### Return type

[**BotapiGetBotsResponse**](BotapiGetBotsResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_chart**
> BotapiGetChartResponse get_chart(userid=userid, interfacekey=interfacekey, botid=botid, interval=interval, style=style, showvolume=showvolume, savesettings=savesettings)

Returns the bots its rendered runtime chart

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.BotAPIApi()
userid = 'userid_example' # str |  (optional)
interfacekey = 'interfacekey_example' # str |  (optional)
botid = 'botid_example' # str |  (optional)
interval = 56 # int |  (optional)
style = 56 # int |  (optional)
showvolume = true # bool |  (optional)
savesettings = true # bool |  (optional)

try:
    # Returns the bots its rendered runtime chart
    api_response = api_instance.get_chart(userid=userid, interfacekey=interfacekey, botid=botid, interval=interval, style=style, showvolume=showvolume, savesettings=savesettings)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BotAPIApi->get_chart: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **userid** | **str**|  | [optional] 
 **interfacekey** | **str**|  | [optional] 
 **botid** | **str**|  | [optional] 
 **interval** | **int**|  | [optional] 
 **style** | **int**|  | [optional] 
 **showvolume** | **bool**|  | [optional] 
 **savesettings** | **bool**|  | [optional] 

### Return type

[**BotapiGetChartResponse**](BotapiGetChartResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_full_logbook**
> BotapiGetFullLogbookResponse get_full_logbook(userid=userid, interfacekey=interfacekey, botid=botid)

Returns the bots its full logbook

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.BotAPIApi()
userid = 'userid_example' # str |  (optional)
interfacekey = 'interfacekey_example' # str |  (optional)
botid = 'botid_example' # str |  (optional)

try:
    # Returns the bots its full logbook
    api_response = api_instance.get_full_logbook(userid=userid, interfacekey=interfacekey, botid=botid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BotAPIApi->get_full_logbook: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **userid** | **str**|  | [optional] 
 **interfacekey** | **str**|  | [optional] 
 **botid** | **str**|  | [optional] 

### Return type

[**BotapiGetFullLogbookResponse**](BotapiGetFullLogbookResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_logbook**
> BotapiGetLogbookResponse get_logbook(userid=userid, interfacekey=interfacekey, botid=botid, afterid=afterid, logcount=logcount)

Returns the bots its message logbook

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.BotAPIApi()
userid = 'userid_example' # str |  (optional)
interfacekey = 'interfacekey_example' # str |  (optional)
botid = 'botid_example' # str |  (optional)
afterid = 56 # int |  (optional)
logcount = 56 # int |  (optional)

try:
    # Returns the bots its message logbook
    api_response = api_instance.get_logbook(userid=userid, interfacekey=interfacekey, botid=botid, afterid=afterid, logcount=logcount)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BotAPIApi->get_logbook: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **userid** | **str**|  | [optional] 
 **interfacekey** | **str**|  | [optional] 
 **botid** | **str**|  | [optional] 
 **afterid** | **int**|  | [optional] 
 **logcount** | **int**|  | [optional] 

### Return type

[**BotapiGetLogbookResponse**](BotapiGetLogbookResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_open_orders**
> BotapiGetOpenOrdersResponse get_open_orders(userid=userid, interfacekey=interfacekey)

Returns all the open bot orders

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.BotAPIApi()
userid = 'userid_example' # str |  (optional)
interfacekey = 'interfacekey_example' # str |  (optional)

try:
    # Returns all the open bot orders
    api_response = api_instance.get_open_orders(userid=userid, interfacekey=interfacekey)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BotAPIApi->get_open_orders: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **userid** | **str**|  | [optional] 
 **interfacekey** | **str**|  | [optional] 

### Return type

[**BotapiGetOpenOrdersResponse**](BotapiGetOpenOrdersResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_open_positions**
> BotapiGetOpenPositionsResponse get_open_positions(userid=userid, interfacekey=interfacekey)

Returns all the open bot positions

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.BotAPIApi()
userid = 'userid_example' # str |  (optional)
interfacekey = 'interfacekey_example' # str |  (optional)

try:
    # Returns all the open bot positions
    api_response = api_instance.get_open_positions(userid=userid, interfacekey=interfacekey)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BotAPIApi->get_open_positions: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **userid** | **str**|  | [optional] 
 **interfacekey** | **str**|  | [optional] 

### Return type

[**BotapiGetOpenPositionsResponse**](BotapiGetOpenPositionsResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_runtime**
> BotapiGetRuntimeResponse get_runtime(userid=userid, interfacekey=interfacekey, botid=botid)

Returns the bots its runtime

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.BotAPIApi()
userid = 'userid_example' # str |  (optional)
interfacekey = 'interfacekey_example' # str |  (optional)
botid = 'botid_example' # str |  (optional)

try:
    # Returns the bots its runtime
    api_response = api_instance.get_runtime(userid=userid, interfacekey=interfacekey, botid=botid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BotAPIApi->get_runtime: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **userid** | **str**|  | [optional] 
 **interfacekey** | **str**|  | [optional] 
 **botid** | **str**|  | [optional] 

### Return type

[**BotapiGetRuntimeResponse**](BotapiGetRuntimeResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_runtime_logbook**
> BotapiGetRuntimeLogbookResponse get_runtime_logbook(userid=userid, interfacekey=interfacekey, botid=botid)

Returns the bots its recent logbook

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.BotAPIApi()
userid = 'userid_example' # str |  (optional)
interfacekey = 'interfacekey_example' # str |  (optional)
botid = 'botid_example' # str |  (optional)

try:
    # Returns the bots its recent logbook
    api_response = api_instance.get_runtime_logbook(userid=userid, interfacekey=interfacekey, botid=botid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BotAPIApi->get_runtime_logbook: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **userid** | **str**|  | [optional] 
 **interfacekey** | **str**|  | [optional] 
 **botid** | **str**|  | [optional] 

### Return type

[**BotapiGetRuntimeLogbookResponse**](BotapiGetRuntimeLogbookResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **rename_bot**
> BotapiRenameBotResponse rename_bot(userid=userid, interfacekey=interfacekey, botid=botid, botname=botname)

Renames the bot

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.BotAPIApi()
userid = 'userid_example' # str |  (optional)
interfacekey = 'interfacekey_example' # str |  (optional)
botid = 'botid_example' # str |  (optional)
botname = 'botname_example' # str |  (optional)

try:
    # Renames the bot
    api_response = api_instance.rename_bot(userid=userid, interfacekey=interfacekey, botid=botid, botname=botname)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BotAPIApi->rename_bot: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **userid** | **str**|  | [optional] 
 **interfacekey** | **str**|  | [optional] 
 **botid** | **str**|  | [optional] 
 **botname** | **str**|  | [optional] 

### Return type

[**BotapiRenameBotResponse**](BotapiRenameBotResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

