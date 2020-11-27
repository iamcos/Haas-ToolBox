# swagger_client.SignalAPIApi

All URIs are relative to *http://127.0.0.1:8090*

Method | HTTP request | Description
------------- | ------------- | -------------
[**edit_signal**](SignalAPIApi.md#edit_signal) | **POST** /SignalAPI.php?channel&#x3D;EDIT_SIGNAL | Stores the given changes to the signal
[**email_signaldetails**](SignalAPIApi.md#email_signaldetails) | **POST** /SignalAPI.php?channel&#x3D;EMAIL_SIGNALDETAILS | Sends a email to the user with the private/secret key of the signal
[**get_backtest**](SignalAPIApi.md#get_backtest) | **POST** /SignalAPI.php?channel&#x3D;GET_BACKTEST | Returns the backtest signal its signals
[**get_signal**](SignalAPIApi.md#get_signal) | **POST** /SignalAPI.php?channel&#x3D;GET_SIGNAL | Returns the current signal
[**my_signals**](SignalAPIApi.md#my_signals) | **POST** /SignalAPI.php?channel&#x3D;MY_SIGNALS | This returns a list of all the user its signals
[**new_signal**](SignalAPIApi.md#new_signal) | **POST** /SignalAPI.php?channel&#x3D;NEW_SIGNAL | Creates a new signal and then the details of that signal will be returned.
[**publish_signal**](SignalAPIApi.md#publish_signal) | **POST** /SignalAPI.php?channel&#x3D;PUBLISH_SIGNAL | Releases the signal to the webshop so it an be sold
[**remove_signal**](SignalAPIApi.md#remove_signal) | **POST** /SignalAPI.php?channel&#x3D;REMOVE_SIGNAL | Deletes the signal and its history
[**store_signal**](SignalAPIApi.md#store_signal) | **POST** /SignalAPI.php?channel&#x3D;STORE_SIGNAL | Use this webhook to send signals to the HaasCloud
[**unpublish_signal**](SignalAPIApi.md#unpublish_signal) | **POST** /SignalAPI.php?channel&#x3D;UNPUBLISH_SIGNAL | Removes the signal from the webshop

# **edit_signal**
> SignalapiEditSignalResponse edit_signal(userid=userid, interfacekey=interfacekey, id=id, name=name, description=description)

Stores the given changes to the signal

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.SignalAPIApi()
userid = 'userid_example' # str |  (optional)
interfacekey = 'interfacekey_example' # str |  (optional)
id = 'id_example' # str |  (optional)
name = 'name_example' # str |  (optional)
description = 'description_example' # str |  (optional)

try:
    # Stores the given changes to the signal
    api_response = api_instance.edit_signal(userid=userid, interfacekey=interfacekey, id=id, name=name, description=description)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SignalAPIApi->edit_signal: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **userid** | **str**|  | [optional] 
 **interfacekey** | **str**|  | [optional] 
 **id** | **str**|  | [optional] 
 **name** | **str**|  | [optional] 
 **description** | **str**|  | [optional] 

### Return type

[**SignalapiEditSignalResponse**](SignalapiEditSignalResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **email_signaldetails**
> SignalapiEmailSignaldetailsResponse email_signaldetails(userid=userid, interfacekey=interfacekey, id=id)

Sends a email to the user with the private/secret key of the signal

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.SignalAPIApi()
userid = 'userid_example' # str |  (optional)
interfacekey = 'interfacekey_example' # str |  (optional)
id = 'id_example' # str |  (optional)

try:
    # Sends a email to the user with the private/secret key of the signal
    api_response = api_instance.email_signaldetails(userid=userid, interfacekey=interfacekey, id=id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SignalAPIApi->email_signaldetails: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **userid** | **str**|  | [optional] 
 **interfacekey** | **str**|  | [optional] 
 **id** | **str**|  | [optional] 

### Return type

[**SignalapiEmailSignaldetailsResponse**](SignalapiEmailSignaldetailsResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_backtest**
> SignalapiGetBacktestResponse get_backtest(userid=userid, interfacekey=interfacekey, id=id)

Returns the backtest signal its signals

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.SignalAPIApi()
userid = 'userid_example' # str |  (optional)
interfacekey = 'interfacekey_example' # str |  (optional)
id = 'id_example' # str |  (optional)

try:
    # Returns the backtest signal its signals
    api_response = api_instance.get_backtest(userid=userid, interfacekey=interfacekey, id=id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SignalAPIApi->get_backtest: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **userid** | **str**|  | [optional] 
 **interfacekey** | **str**|  | [optional] 
 **id** | **str**|  | [optional] 

### Return type

[**SignalapiGetBacktestResponse**](SignalapiGetBacktestResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_signal**
> SignalapiGetSignalResponse get_signal(userid=userid, interfacekey=interfacekey, id=id)

Returns the current signal

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.SignalAPIApi()
userid = 'userid_example' # str |  (optional)
interfacekey = 'interfacekey_example' # str |  (optional)
id = 'id_example' # str |  (optional)

try:
    # Returns the current signal
    api_response = api_instance.get_signal(userid=userid, interfacekey=interfacekey, id=id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SignalAPIApi->get_signal: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **userid** | **str**|  | [optional] 
 **interfacekey** | **str**|  | [optional] 
 **id** | **str**|  | [optional] 

### Return type

[**SignalapiGetSignalResponse**](SignalapiGetSignalResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **my_signals**
> SignalapiMySignalsResponse my_signals(userid=userid, interfacekey=interfacekey)

This returns a list of all the user its signals

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.SignalAPIApi()
userid = 'userid_example' # str |  (optional)
interfacekey = 'interfacekey_example' # str |  (optional)

try:
    # This returns a list of all the user its signals
    api_response = api_instance.my_signals(userid=userid, interfacekey=interfacekey)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SignalAPIApi->my_signals: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **userid** | **str**|  | [optional] 
 **interfacekey** | **str**|  | [optional] 

### Return type

[**SignalapiMySignalsResponse**](SignalapiMySignalsResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **new_signal**
> SignalapiNewSignalResponse new_signal(userid=userid, interfacekey=interfacekey, name=name, description=description)

Creates a new signal and then the details of that signal will be returned.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.SignalAPIApi()
userid = 'userid_example' # str |  (optional)
interfacekey = 'interfacekey_example' # str |  (optional)
name = 'name_example' # str |  (optional)
description = 'description_example' # str |  (optional)

try:
    # Creates a new signal and then the details of that signal will be returned.
    api_response = api_instance.new_signal(userid=userid, interfacekey=interfacekey, name=name, description=description)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SignalAPIApi->new_signal: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **userid** | **str**|  | [optional] 
 **interfacekey** | **str**|  | [optional] 
 **name** | **str**|  | [optional] 
 **description** | **str**|  | [optional] 

### Return type

[**SignalapiNewSignalResponse**](SignalapiNewSignalResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **publish_signal**
> SignalapiPublishSignalResponse publish_signal(userid=userid, interfacekey=interfacekey, id=id)

Releases the signal to the webshop so it an be sold

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.SignalAPIApi()
userid = 'userid_example' # str |  (optional)
interfacekey = 'interfacekey_example' # str |  (optional)
id = 'id_example' # str |  (optional)

try:
    # Releases the signal to the webshop so it an be sold
    api_response = api_instance.publish_signal(userid=userid, interfacekey=interfacekey, id=id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SignalAPIApi->publish_signal: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **userid** | **str**|  | [optional] 
 **interfacekey** | **str**|  | [optional] 
 **id** | **str**|  | [optional] 

### Return type

[**SignalapiPublishSignalResponse**](SignalapiPublishSignalResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **remove_signal**
> SignalapiRemoveSignalResponse remove_signal(userid=userid, interfacekey=interfacekey, id=id)

Deletes the signal and its history

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.SignalAPIApi()
userid = 'userid_example' # str |  (optional)
interfacekey = 'interfacekey_example' # str |  (optional)
id = 'id_example' # str |  (optional)

try:
    # Deletes the signal and its history
    api_response = api_instance.remove_signal(userid=userid, interfacekey=interfacekey, id=id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SignalAPIApi->remove_signal: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **userid** | **str**|  | [optional] 
 **interfacekey** | **str**|  | [optional] 
 **id** | **str**|  | [optional] 

### Return type

[**SignalapiRemoveSignalResponse**](SignalapiRemoveSignalResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **store_signal**
> SignalapiStoreSignalResponse store_signal(id=id, secret=secret, signal=signal)

Use this webhook to send signals to the HaasCloud

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.SignalAPIApi()
id = 'id_example' # str |  (optional)
secret = 'secret_example' # str |  (optional)
signal = 56 # int |  (optional)

try:
    # Use this webhook to send signals to the HaasCloud
    api_response = api_instance.store_signal(id=id, secret=secret, signal=signal)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SignalAPIApi->store_signal: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | [optional] 
 **secret** | **str**|  | [optional] 
 **signal** | **int**|  | [optional] 

### Return type

[**SignalapiStoreSignalResponse**](SignalapiStoreSignalResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **unpublish_signal**
> SignalapiUnpublishSignalResponse unpublish_signal(userid=userid, interfacekey=interfacekey, id=id)

Removes the signal from the webshop

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.SignalAPIApi()
userid = 'userid_example' # str |  (optional)
interfacekey = 'interfacekey_example' # str |  (optional)
id = 'id_example' # str |  (optional)

try:
    # Removes the signal from the webshop
    api_response = api_instance.unpublish_signal(userid=userid, interfacekey=interfacekey, id=id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SignalAPIApi->unpublish_signal: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **userid** | **str**|  | [optional] 
 **interfacekey** | **str**|  | [optional] 
 **id** | **str**|  | [optional] 

### Return type

[**SignalapiUnpublishSignalResponse**](SignalapiUnpublishSignalResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

