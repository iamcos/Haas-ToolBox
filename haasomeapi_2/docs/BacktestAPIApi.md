# swagger_client.BacktestAPIApi

All URIs are relative to *http://127.0.0.1:8090*

Method | HTTP request | Description
------------- | ------------- | -------------
[**archive_backtest**](BacktestAPIApi.md#archive_backtest) | **POST** /BacktestAPI.php?channel&#x3D;ARCHIVE_BACKTEST | Controls to archive a backtest result or not
[**delete_backtest**](BacktestAPIApi.md#delete_backtest) | **POST** /BacktestAPI.php?channel&#x3D;DELETE_BACKTEST | Delete/remove a backtest result
[**delete_unarchived_backtest**](BacktestAPIApi.md#delete_unarchived_backtest) | **POST** /BacktestAPI.php?channel&#x3D;DELETE_UNARCHIVED_BACKTEST | Deletes/removes all unarchived backtest results
[**edit_backtest_tag**](BacktestAPIApi.md#edit_backtest_tag) | **POST** /BacktestAPI.php?channel&#x3D;EDIT_BACKTEST_TAG | Changes a backtest tag
[**get_backtest**](BacktestAPIApi.md#get_backtest) | **POST** /BacktestAPI.php?channel&#x3D;GET_BACKTEST | Returns a stored backtest result
[**get_backtest_runtime**](BacktestAPIApi.md#get_backtest_runtime) | **POST** /BacktestAPI.php?channel&#x3D;GET_BACKTEST_RUNTIME | Returns a stored backtest runtime
[**get_full_backtest_history**](BacktestAPIApi.md#get_full_backtest_history) | **POST** /BacktestAPI.php?channel&#x3D;GET_FULL_BACKTEST_HISTORY | Returns a list of all stored backtest results
[**get_latest_backtests**](BacktestAPIApi.md#get_latest_backtests) | **POST** /BacktestAPI.php?channel&#x3D;GET_LATEST_BACKTESTS | Returns a list of the latest stored backtest

# **archive_backtest**
> BacktestapiArchiveBacktestResponse archive_backtest(userid=userid, interfacekey=interfacekey, backtestid=backtestid, archiveresult=archiveresult)

Controls to archive a backtest result or not

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.BacktestAPIApi()
userid = 'userid_example' # str |  (optional)
interfacekey = 'interfacekey_example' # str |  (optional)
backtestid = 'backtestid_example' # str |  (optional)
archiveresult = true # bool |  (optional)

try:
    # Controls to archive a backtest result or not
    api_response = api_instance.archive_backtest(userid=userid, interfacekey=interfacekey, backtestid=backtestid, archiveresult=archiveresult)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BacktestAPIApi->archive_backtest: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **userid** | **str**|  | [optional] 
 **interfacekey** | **str**|  | [optional] 
 **backtestid** | **str**|  | [optional] 
 **archiveresult** | **bool**|  | [optional] 

### Return type

[**BacktestapiArchiveBacktestResponse**](BacktestapiArchiveBacktestResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_backtest**
> BacktestapiDeleteBacktestResponse delete_backtest(userid=userid, interfacekey=interfacekey, backtestid=backtestid)

Delete/remove a backtest result

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.BacktestAPIApi()
userid = 'userid_example' # str |  (optional)
interfacekey = 'interfacekey_example' # str |  (optional)
backtestid = 'backtestid_example' # str |  (optional)

try:
    # Delete/remove a backtest result
    api_response = api_instance.delete_backtest(userid=userid, interfacekey=interfacekey, backtestid=backtestid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BacktestAPIApi->delete_backtest: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **userid** | **str**|  | [optional] 
 **interfacekey** | **str**|  | [optional] 
 **backtestid** | **str**|  | [optional] 

### Return type

[**BacktestapiDeleteBacktestResponse**](BacktestapiDeleteBacktestResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_unarchived_backtest**
> BacktestapiDeleteUnarchivedBacktestResponse delete_unarchived_backtest(userid=userid, interfacekey=interfacekey)

Deletes/removes all unarchived backtest results

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.BacktestAPIApi()
userid = 'userid_example' # str |  (optional)
interfacekey = 'interfacekey_example' # str |  (optional)

try:
    # Deletes/removes all unarchived backtest results
    api_response = api_instance.delete_unarchived_backtest(userid=userid, interfacekey=interfacekey)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BacktestAPIApi->delete_unarchived_backtest: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **userid** | **str**|  | [optional] 
 **interfacekey** | **str**|  | [optional] 

### Return type

[**BacktestapiDeleteUnarchivedBacktestResponse**](BacktestapiDeleteUnarchivedBacktestResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **edit_backtest_tag**
> BacktestapiEditBacktestTagResponse edit_backtest_tag(userid=userid, interfacekey=interfacekey, backtestid=backtestid, backtesttag=backtesttag)

Changes a backtest tag

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.BacktestAPIApi()
userid = 'userid_example' # str |  (optional)
interfacekey = 'interfacekey_example' # str |  (optional)
backtestid = 'backtestid_example' # str |  (optional)
backtesttag = 'backtesttag_example' # str |  (optional)

try:
    # Changes a backtest tag
    api_response = api_instance.edit_backtest_tag(userid=userid, interfacekey=interfacekey, backtestid=backtestid, backtesttag=backtesttag)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BacktestAPIApi->edit_backtest_tag: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **userid** | **str**|  | [optional] 
 **interfacekey** | **str**|  | [optional] 
 **backtestid** | **str**|  | [optional] 
 **backtesttag** | **str**|  | [optional] 

### Return type

[**BacktestapiEditBacktestTagResponse**](BacktestapiEditBacktestTagResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_backtest**
> BacktestapiGetBacktestResponse get_backtest(userid=userid, backtestid=backtestid, interfacekey=interfacekey)

Returns a stored backtest result

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.BacktestAPIApi()
userid = 'userid_example' # str |  (optional)
backtestid = 'backtestid_example' # str |  (optional)
interfacekey = 'interfacekey_example' # str |  (optional)

try:
    # Returns a stored backtest result
    api_response = api_instance.get_backtest(userid=userid, backtestid=backtestid, interfacekey=interfacekey)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BacktestAPIApi->get_backtest: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **userid** | **str**|  | [optional] 
 **backtestid** | **str**|  | [optional] 
 **interfacekey** | **str**|  | [optional] 

### Return type

[**BacktestapiGetBacktestResponse**](BacktestapiGetBacktestResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_backtest_runtime**
> BacktestapiGetBacktestRuntimeResponse get_backtest_runtime(userid=userid, backtestid=backtestid, interfacekey=interfacekey)

Returns a stored backtest runtime

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.BacktestAPIApi()
userid = 'userid_example' # str |  (optional)
backtestid = 'backtestid_example' # str |  (optional)
interfacekey = 'interfacekey_example' # str |  (optional)

try:
    # Returns a stored backtest runtime
    api_response = api_instance.get_backtest_runtime(userid=userid, backtestid=backtestid, interfacekey=interfacekey)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BacktestAPIApi->get_backtest_runtime: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **userid** | **str**|  | [optional] 
 **backtestid** | **str**|  | [optional] 
 **interfacekey** | **str**|  | [optional] 

### Return type

[**BacktestapiGetBacktestRuntimeResponse**](BacktestapiGetBacktestRuntimeResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_full_backtest_history**
> BacktestapiGetFullBacktestHistoryResponse get_full_backtest_history(userid=userid, interfacekey=interfacekey)

Returns a list of all stored backtest results

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.BacktestAPIApi()
userid = 'userid_example' # str |  (optional)
interfacekey = 'interfacekey_example' # str |  (optional)

try:
    # Returns a list of all stored backtest results
    api_response = api_instance.get_full_backtest_history(userid=userid, interfacekey=interfacekey)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BacktestAPIApi->get_full_backtest_history: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **userid** | **str**|  | [optional] 
 **interfacekey** | **str**|  | [optional] 

### Return type

[**BacktestapiGetFullBacktestHistoryResponse**](BacktestapiGetFullBacktestHistoryResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_latest_backtests**
> BacktestapiGetLatestBacktestsResponse get_latest_backtests(userid=userid, interfacekey=interfacekey)

Returns a list of the latest stored backtest

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.BacktestAPIApi()
userid = 'userid_example' # str |  (optional)
interfacekey = 'interfacekey_example' # str |  (optional)

try:
    # Returns a list of the latest stored backtest
    api_response = api_instance.get_latest_backtests(userid=userid, interfacekey=interfacekey)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BacktestAPIApi->get_latest_backtests: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **userid** | **str**|  | [optional] 
 **interfacekey** | **str**|  | [optional] 

### Return type

[**BacktestapiGetLatestBacktestsResponse**](BacktestapiGetLatestBacktestsResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

