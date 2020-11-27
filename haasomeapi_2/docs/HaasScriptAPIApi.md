# swagger_client.HaasScriptAPIApi

All URIs are relative to *http://127.0.0.1:8090*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_script**](HaasScriptAPIApi.md#add_script) | **POST** /HaasScriptAPI.php?channel&#x3D;ADD_SCRIPT | 
[**backtest_script**](HaasScriptAPIApi.md#backtest_script) | **POST** /HaasScriptAPI.php?channel&#x3D;BACKTEST_SCRIPT | Executes a backtest
[**cancel_backtest**](HaasScriptAPIApi.md#cancel_backtest) | **POST** /HaasScriptAPI.php?channel&#x3D;CANCEL_BACKTEST | Cancels a running backtest
[**create_new_backup**](HaasScriptAPIApi.md#create_new_backup) | **POST** /HaasScriptAPI.php?channel&#x3D;CREATE_NEW_BACKUP | Creates a backup of the given script
[**debug_script**](HaasScriptAPIApi.md#debug_script) | **POST** /HaasScriptAPI.php?channel&#x3D;DEBUG_SCRIPT | Does a debug run of the script
[**delete_script**](HaasScriptAPIApi.md#delete_script) | **POST** /HaasScriptAPI.php?channel&#x3D;DELETE_SCRIPT | 
[**edit_script**](HaasScriptAPIApi.md#edit_script) | **POST** /HaasScriptAPI.php?channel&#x3D;EDIT_SCRIPT | 
[**edit_script_sourcecode**](HaasScriptAPIApi.md#edit_script_sourcecode) | **POST** /HaasScriptAPI.php?channel&#x3D;EDIT_SCRIPT_SOURCECODE | 
[**edit_script_specifications**](HaasScriptAPIApi.md#edit_script_specifications) | **POST** /HaasScriptAPI.php?channel&#x3D;EDIT_SCRIPT_SPECIFICATIONS | 
[**get_all_profiles**](HaasScriptAPIApi.md#get_all_profiles) | **POST** /HaasScriptAPI.php?channel&#x3D;GET_ALL_PROFILES | Returns the profiles per strategy
[**get_all_script_items**](HaasScriptAPIApi.md#get_all_script_items) | **POST** /HaasScriptAPI.php?channel&#x3D;GET_ALL_SCRIPT_ITEMS | 
[**get_all_script_records**](HaasScriptAPIApi.md#get_all_script_records) | **POST** /HaasScriptAPI.php?channel&#x3D;GET_ALL_SCRIPT_RECORDS | 
[**get_backup**](HaasScriptAPIApi.md#get_backup) | **POST** /HaasScriptAPI.php?channel&#x3D;GET_BACKUP | Opens the backup file as new script
[**get_backup_versions**](HaasScriptAPIApi.md#get_backup_versions) | **POST** /HaasScriptAPI.php?channel&#x3D;GET_BACKUP_VERSIONS | Returns a list of the backup versions
[**get_best_profiles**](HaasScriptAPIApi.md#get_best_profiles) | **POST** /HaasScriptAPI.php?channel&#x3D;GET_BEST_PROFILES | Returns the best profiles per market
[**get_block**](HaasScriptAPIApi.md#get_block) | **POST** /HaasScriptAPI.php?channel&#x3D;GET_BLOCK | 
[**get_blocks**](HaasScriptAPIApi.md#get_blocks) | **POST** /HaasScriptAPI.php?channel&#x3D;GET_BLOCKS | 
[**get_command**](HaasScriptAPIApi.md#get_command) | **POST** /HaasScriptAPI.php?channel&#x3D;GET_COMMAND | 
[**get_commands**](HaasScriptAPIApi.md#get_commands) | **POST** /HaasScriptAPI.php?channel&#x3D;GET_COMMANDS | 
[**get_pattern_chart**](HaasScriptAPIApi.md#get_pattern_chart) | **POST** /HaasScriptAPI.php?channel&#x3D;GET_PATTERN_CHART | Returns the price pattern chart
[**get_script_item**](HaasScriptAPIApi.md#get_script_item) | **POST** /HaasScriptAPI.php?channel&#x3D;GET_SCRIPT_ITEM | 
[**get_script_record**](HaasScriptAPIApi.md#get_script_record) | **POST** /HaasScriptAPI.php?channel&#x3D;GET_SCRIPT_RECORD | 
[**get_test_patterns**](HaasScriptAPIApi.md#get_test_patterns) | **POST** /HaasScriptAPI.php?channel&#x3D;GET_TEST_PATTERNS | Returns all avilible test patterns
[**init_script**](HaasScriptAPIApi.md#init_script) | **POST** /HaasScriptAPI.php?channel&#x3D;INIT_SCRIPT | Setup script and settings
[**pattern_highscores**](HaasScriptAPIApi.md#pattern_highscores) | **POST** /HaasScriptAPI.php?channel&#x3D;PATTERN_HIGHSCORES | Returns the highet scores reached for a test pattern
[**patterntest_script**](HaasScriptAPIApi.md#patterntest_script) | **POST** /HaasScriptAPI.php?channel&#x3D;PATTERNTEST_SCRIPT | Executes a pattern test
[**profile_script**](HaasScriptAPIApi.md#profile_script) | **POST** /HaasScriptAPI.php?channel&#x3D;PROFILE_SCRIPT | Renders a profile of the given strategy
[**publish_community_script**](HaasScriptAPIApi.md#publish_community_script) | **POST** /HaasScriptAPI.php?channel&#x3D;PUBLISH_COMMUNITY_SCRIPT | Publishes the strategy to haasscript.com (not used)
[**publish_script**](HaasScriptAPIApi.md#publish_script) | **POST** /HaasScriptAPI.php?channel&#x3D;PUBLISH_SCRIPT | Publishes the strategy to the webshop (not used)
[**quick_run_script**](HaasScriptAPIApi.md#quick_run_script) | **POST** /HaasScriptAPI.php?channel&#x3D;QUICK_RUN_SCRIPT | Does a brief backtest
[**restore_backup**](HaasScriptAPIApi.md#restore_backup) | **POST** /HaasScriptAPI.php?channel&#x3D;RESTORE_BACKUP | Restores a backup
[**search_in_scripts**](HaasScriptAPIApi.md#search_in_scripts) | **POST** /HaasScriptAPI.php?channel&#x3D;SEARCH_IN_SCRIPTS | Tres to find code within the scripts
[**unpublish_script**](HaasScriptAPIApi.md#unpublish_script) | **POST** /HaasScriptAPI.php?channel&#x3D;UNPUBLISH_SCRIPT | Remove publication (not used)

# **add_script**
> add_script(userid=userid, interfacekey=interfacekey, name=name, description=description, script=script, type=type, iscommand=iscommand)



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.HaasScriptAPIApi()
userid = 'userid_example' # str |  (optional)
interfacekey = 'interfacekey_example' # str |  (optional)
name = 'name_example' # str |  (optional)
description = 'description_example' # str |  (optional)
script = 'script_example' # str |  (optional)
type = 56 # int |  (optional)
iscommand = true # bool |  (optional)

try:
    api_instance.add_script(userid=userid, interfacekey=interfacekey, name=name, description=description, script=script, type=type, iscommand=iscommand)
except ApiException as e:
    print("Exception when calling HaasScriptAPIApi->add_script: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **userid** | **str**|  | [optional] 
 **interfacekey** | **str**|  | [optional] 
 **name** | **str**|  | [optional] 
 **description** | **str**|  | [optional] 
 **script** | **str**|  | [optional] 
 **type** | **int**|  | [optional] 
 **iscommand** | **bool**|  | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **backtest_script**
> HaasscriptapiBacktestScriptResponse backtest_script(userid=userid, interfacekey=interfacekey, backtestid=backtestid, scriptid=scriptid, settings=settings, startunix=startunix, endunix=endunix)

Executes a backtest

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.HaasScriptAPIApi()
userid = 'userid_example' # str |  (optional)
interfacekey = 'interfacekey_example' # str |  (optional)
backtestid = 'backtestid_example' # str |  (optional)
scriptid = 'scriptid_example' # str |  (optional)
settings = NULL # object |  (optional)
startunix = 56 # int |  (optional)
endunix = 56 # int |  (optional)

try:
    # Executes a backtest
    api_response = api_instance.backtest_script(userid=userid, interfacekey=interfacekey, backtestid=backtestid, scriptid=scriptid, settings=settings, startunix=startunix, endunix=endunix)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling HaasScriptAPIApi->backtest_script: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **userid** | **str**|  | [optional] 
 **interfacekey** | **str**|  | [optional] 
 **backtestid** | **str**|  | [optional] 
 **scriptid** | **str**|  | [optional] 
 **settings** | [**object**](.md)|  | [optional] 
 **startunix** | **int**|  | [optional] 
 **endunix** | **int**|  | [optional] 

### Return type

[**HaasscriptapiBacktestScriptResponse**](HaasscriptapiBacktestScriptResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **cancel_backtest**
> HaasscriptapiCancelBacktestResponse cancel_backtest(userid=userid, interfacekey=interfacekey, backtestid=backtestid)

Cancels a running backtest

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.HaasScriptAPIApi()
userid = 'userid_example' # str |  (optional)
interfacekey = 'interfacekey_example' # str |  (optional)
backtestid = 'backtestid_example' # str |  (optional)

try:
    # Cancels a running backtest
    api_response = api_instance.cancel_backtest(userid=userid, interfacekey=interfacekey, backtestid=backtestid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling HaasScriptAPIApi->cancel_backtest: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **userid** | **str**|  | [optional] 
 **interfacekey** | **str**|  | [optional] 
 **backtestid** | **str**|  | [optional] 

### Return type

[**HaasscriptapiCancelBacktestResponse**](HaasscriptapiCancelBacktestResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_new_backup**
> HaasscriptapiCreateNewBackupResponse create_new_backup(userid=userid, interfacekey=interfacekey, scriptid=scriptid)

Creates a backup of the given script

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.HaasScriptAPIApi()
userid = 'userid_example' # str |  (optional)
interfacekey = 'interfacekey_example' # str |  (optional)
scriptid = 'scriptid_example' # str |  (optional)

try:
    # Creates a backup of the given script
    api_response = api_instance.create_new_backup(userid=userid, interfacekey=interfacekey, scriptid=scriptid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling HaasScriptAPIApi->create_new_backup: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **userid** | **str**|  | [optional] 
 **interfacekey** | **str**|  | [optional] 
 **scriptid** | **str**|  | [optional] 

### Return type

[**HaasscriptapiCreateNewBackupResponse**](HaasscriptapiCreateNewBackupResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **debug_script**
> HaasscriptapiDebugScriptResponse debug_script(userid=userid, interfacekey=interfacekey, scriptid=scriptid, scripttype=scripttype, settings=settings)

Does a debug run of the script

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.HaasScriptAPIApi()
userid = 'userid_example' # str |  (optional)
interfacekey = 'interfacekey_example' # str |  (optional)
scriptid = 'scriptid_example' # str |  (optional)
scripttype = 56 # int |  (optional)
settings = NULL # object |  (optional)

try:
    # Does a debug run of the script
    api_response = api_instance.debug_script(userid=userid, interfacekey=interfacekey, scriptid=scriptid, scripttype=scripttype, settings=settings)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling HaasScriptAPIApi->debug_script: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **userid** | **str**|  | [optional] 
 **interfacekey** | **str**|  | [optional] 
 **scriptid** | **str**|  | [optional] 
 **scripttype** | **int**|  | [optional] 
 **settings** | [**object**](.md)|  | [optional] 

### Return type

[**HaasscriptapiDebugScriptResponse**](HaasscriptapiDebugScriptResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_script**
> delete_script(userid=userid, interfacekey=interfacekey, scriptid=scriptid)



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.HaasScriptAPIApi()
userid = 'userid_example' # str |  (optional)
interfacekey = 'interfacekey_example' # str |  (optional)
scriptid = 'scriptid_example' # str |  (optional)

try:
    api_instance.delete_script(userid=userid, interfacekey=interfacekey, scriptid=scriptid)
except ApiException as e:
    print("Exception when calling HaasScriptAPIApi->delete_script: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **userid** | **str**|  | [optional] 
 **interfacekey** | **str**|  | [optional] 
 **scriptid** | **str**|  | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **edit_script**
> edit_script(userid=userid, interfacekey=interfacekey, scriptid=scriptid, name=name, description=description, script=script)



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.HaasScriptAPIApi()
userid = 'userid_example' # str |  (optional)
interfacekey = 'interfacekey_example' # str |  (optional)
scriptid = 'scriptid_example' # str |  (optional)
name = 'name_example' # str |  (optional)
description = 'description_example' # str |  (optional)
script = 'script_example' # str |  (optional)

try:
    api_instance.edit_script(userid=userid, interfacekey=interfacekey, scriptid=scriptid, name=name, description=description, script=script)
except ApiException as e:
    print("Exception when calling HaasScriptAPIApi->edit_script: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **userid** | **str**|  | [optional] 
 **interfacekey** | **str**|  | [optional] 
 **scriptid** | **str**|  | [optional] 
 **name** | **str**|  | [optional] 
 **description** | **str**|  | [optional] 
 **script** | **str**|  | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **edit_script_sourcecode**
> edit_script_sourcecode(userid=userid, interfacekey=interfacekey, scriptid=scriptid, sourcecode=sourcecode)



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.HaasScriptAPIApi()
userid = 'userid_example' # str |  (optional)
interfacekey = 'interfacekey_example' # str |  (optional)
scriptid = 'scriptid_example' # str |  (optional)
sourcecode = 'sourcecode_example' # str |  (optional)

try:
    api_instance.edit_script_sourcecode(userid=userid, interfacekey=interfacekey, scriptid=scriptid, sourcecode=sourcecode)
except ApiException as e:
    print("Exception when calling HaasScriptAPIApi->edit_script_sourcecode: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **userid** | **str**|  | [optional] 
 **interfacekey** | **str**|  | [optional] 
 **scriptid** | **str**|  | [optional] 
 **sourcecode** | **str**|  | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **edit_script_specifications**
> edit_script_specifications(userid=userid, interfacekey=interfacekey, scriptid=scriptid, name=name, description=description)



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.HaasScriptAPIApi()
userid = 'userid_example' # str |  (optional)
interfacekey = 'interfacekey_example' # str |  (optional)
scriptid = 'scriptid_example' # str |  (optional)
name = 'name_example' # str |  (optional)
description = 'description_example' # str |  (optional)

try:
    api_instance.edit_script_specifications(userid=userid, interfacekey=interfacekey, scriptid=scriptid, name=name, description=description)
except ApiException as e:
    print("Exception when calling HaasScriptAPIApi->edit_script_specifications: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **userid** | **str**|  | [optional] 
 **interfacekey** | **str**|  | [optional] 
 **scriptid** | **str**|  | [optional] 
 **name** | **str**|  | [optional] 
 **description** | **str**|  | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_all_profiles**
> HaasscriptapiGetAllProfilesResponse get_all_profiles(userid=userid, interfacekey=interfacekey, scriptid=scriptid)

Returns the profiles per strategy

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.HaasScriptAPIApi()
userid = 'userid_example' # str |  (optional)
interfacekey = 'interfacekey_example' # str |  (optional)
scriptid = 'scriptid_example' # str |  (optional)

try:
    # Returns the profiles per strategy
    api_response = api_instance.get_all_profiles(userid=userid, interfacekey=interfacekey, scriptid=scriptid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling HaasScriptAPIApi->get_all_profiles: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **userid** | **str**|  | [optional] 
 **interfacekey** | **str**|  | [optional] 
 **scriptid** | **str**|  | [optional] 

### Return type

[**HaasscriptapiGetAllProfilesResponse**](HaasscriptapiGetAllProfilesResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_all_script_items**
> get_all_script_items(userid=userid, interfacekey=interfacekey)



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.HaasScriptAPIApi()
userid = 'userid_example' # str |  (optional)
interfacekey = 'interfacekey_example' # str |  (optional)

try:
    api_instance.get_all_script_items(userid=userid, interfacekey=interfacekey)
except ApiException as e:
    print("Exception when calling HaasScriptAPIApi->get_all_script_items: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **userid** | **str**|  | [optional] 
 **interfacekey** | **str**|  | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_all_script_records**
> get_all_script_records(userid=userid, interfacekey=interfacekey)



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.HaasScriptAPIApi()
userid = 'userid_example' # str |  (optional)
interfacekey = 'interfacekey_example' # str |  (optional)

try:
    api_instance.get_all_script_records(userid=userid, interfacekey=interfacekey)
except ApiException as e:
    print("Exception when calling HaasScriptAPIApi->get_all_script_records: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **userid** | **str**|  | [optional] 
 **interfacekey** | **str**|  | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_backup**
> HaasscriptapiGetBackupResponse get_backup(userid=userid, interfacekey=interfacekey, scriptid=scriptid, wantedversion=wantedversion)

Opens the backup file as new script

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.HaasScriptAPIApi()
userid = 'userid_example' # str |  (optional)
interfacekey = 'interfacekey_example' # str |  (optional)
scriptid = 'scriptid_example' # str |  (optional)
wantedversion = 56 # int |  (optional)

try:
    # Opens the backup file as new script
    api_response = api_instance.get_backup(userid=userid, interfacekey=interfacekey, scriptid=scriptid, wantedversion=wantedversion)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling HaasScriptAPIApi->get_backup: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **userid** | **str**|  | [optional] 
 **interfacekey** | **str**|  | [optional] 
 **scriptid** | **str**|  | [optional] 
 **wantedversion** | **int**|  | [optional] 

### Return type

[**HaasscriptapiGetBackupResponse**](HaasscriptapiGetBackupResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_backup_versions**
> HaasscriptapiGetBackupVersionsResponse get_backup_versions(userid=userid, interfacekey=interfacekey, scriptid=scriptid)

Returns a list of the backup versions

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.HaasScriptAPIApi()
userid = 'userid_example' # str |  (optional)
interfacekey = 'interfacekey_example' # str |  (optional)
scriptid = 'scriptid_example' # str |  (optional)

try:
    # Returns a list of the backup versions
    api_response = api_instance.get_backup_versions(userid=userid, interfacekey=interfacekey, scriptid=scriptid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling HaasScriptAPIApi->get_backup_versions: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **userid** | **str**|  | [optional] 
 **interfacekey** | **str**|  | [optional] 
 **scriptid** | **str**|  | [optional] 

### Return type

[**HaasscriptapiGetBackupVersionsResponse**](HaasscriptapiGetBackupVersionsResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_best_profiles**
> HaasscriptapiGetBestProfilesResponse get_best_profiles(userid=userid, interfacekey=interfacekey, market=market, filterprofile=filterprofile)

Returns the best profiles per market

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.HaasScriptAPIApi()
userid = 'userid_example' # str |  (optional)
interfacekey = 'interfacekey_example' # str |  (optional)
market = 'market_example' # str |  (optional)
filterprofile = NULL # object |  (optional)

try:
    # Returns the best profiles per market
    api_response = api_instance.get_best_profiles(userid=userid, interfacekey=interfacekey, market=market, filterprofile=filterprofile)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling HaasScriptAPIApi->get_best_profiles: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **userid** | **str**|  | [optional] 
 **interfacekey** | **str**|  | [optional] 
 **market** | **str**|  | [optional] 
 **filterprofile** | [**object**](.md)|  | [optional] 

### Return type

[**HaasscriptapiGetBestProfilesResponse**](HaasscriptapiGetBestProfilesResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_block**
> get_block(userid=userid, interfacekey=interfacekey, scriptid=scriptid)



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.HaasScriptAPIApi()
userid = 'userid_example' # str |  (optional)
interfacekey = 'interfacekey_example' # str |  (optional)
scriptid = 'scriptid_example' # str |  (optional)

try:
    api_instance.get_block(userid=userid, interfacekey=interfacekey, scriptid=scriptid)
except ApiException as e:
    print("Exception when calling HaasScriptAPIApi->get_block: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **userid** | **str**|  | [optional] 
 **interfacekey** | **str**|  | [optional] 
 **scriptid** | **str**|  | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_blocks**
> get_blocks(userid=userid, interfacekey=interfacekey)



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.HaasScriptAPIApi()
userid = 'userid_example' # str |  (optional)
interfacekey = 'interfacekey_example' # str |  (optional)

try:
    api_instance.get_blocks(userid=userid, interfacekey=interfacekey)
except ApiException as e:
    print("Exception when calling HaasScriptAPIApi->get_blocks: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **userid** | **str**|  | [optional] 
 **interfacekey** | **str**|  | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_command**
> get_command(userid=userid, interfacekey=interfacekey, scriptid=scriptid)



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.HaasScriptAPIApi()
userid = 'userid_example' # str |  (optional)
interfacekey = 'interfacekey_example' # str |  (optional)
scriptid = 'scriptid_example' # str |  (optional)

try:
    api_instance.get_command(userid=userid, interfacekey=interfacekey, scriptid=scriptid)
except ApiException as e:
    print("Exception when calling HaasScriptAPIApi->get_command: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **userid** | **str**|  | [optional] 
 **interfacekey** | **str**|  | [optional] 
 **scriptid** | **str**|  | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_commands**
> get_commands(userid=userid, interfacekey=interfacekey)



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.HaasScriptAPIApi()
userid = 'userid_example' # str |  (optional)
interfacekey = 'interfacekey_example' # str |  (optional)

try:
    api_instance.get_commands(userid=userid, interfacekey=interfacekey)
except ApiException as e:
    print("Exception when calling HaasScriptAPIApi->get_commands: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **userid** | **str**|  | [optional] 
 **interfacekey** | **str**|  | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_pattern_chart**
> HaasscriptapiGetPatternChartResponse get_pattern_chart(userid=userid, interfacekey=interfacekey, patternid=patternid)

Returns the price pattern chart

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.HaasScriptAPIApi()
userid = 'userid_example' # str |  (optional)
interfacekey = 'interfacekey_example' # str |  (optional)
patternid = 56 # int |  (optional)

try:
    # Returns the price pattern chart
    api_response = api_instance.get_pattern_chart(userid=userid, interfacekey=interfacekey, patternid=patternid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling HaasScriptAPIApi->get_pattern_chart: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **userid** | **str**|  | [optional] 
 **interfacekey** | **str**|  | [optional] 
 **patternid** | **int**|  | [optional] 

### Return type

[**HaasscriptapiGetPatternChartResponse**](HaasscriptapiGetPatternChartResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_script_item**
> get_script_item(userid=userid, interfacekey=interfacekey, scriptid=scriptid)



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.HaasScriptAPIApi()
userid = 'userid_example' # str |  (optional)
interfacekey = 'interfacekey_example' # str |  (optional)
scriptid = 'scriptid_example' # str |  (optional)

try:
    api_instance.get_script_item(userid=userid, interfacekey=interfacekey, scriptid=scriptid)
except ApiException as e:
    print("Exception when calling HaasScriptAPIApi->get_script_item: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **userid** | **str**|  | [optional] 
 **interfacekey** | **str**|  | [optional] 
 **scriptid** | **str**|  | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_script_record**
> get_script_record(userid=userid, interfacekey=interfacekey, scriptid=scriptid)



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.HaasScriptAPIApi()
userid = 'userid_example' # str |  (optional)
interfacekey = 'interfacekey_example' # str |  (optional)
scriptid = 'scriptid_example' # str |  (optional)

try:
    api_instance.get_script_record(userid=userid, interfacekey=interfacekey, scriptid=scriptid)
except ApiException as e:
    print("Exception when calling HaasScriptAPIApi->get_script_record: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **userid** | **str**|  | [optional] 
 **interfacekey** | **str**|  | [optional] 
 **scriptid** | **str**|  | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_test_patterns**
> HaasscriptapiGetTestPatternsResponse get_test_patterns(userid=userid, interfacekey=interfacekey)

Returns all avilible test patterns

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.HaasScriptAPIApi()
userid = 'userid_example' # str |  (optional)
interfacekey = 'interfacekey_example' # str |  (optional)

try:
    # Returns all avilible test patterns
    api_response = api_instance.get_test_patterns(userid=userid, interfacekey=interfacekey)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling HaasScriptAPIApi->get_test_patterns: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **userid** | **str**|  | [optional] 
 **interfacekey** | **str**|  | [optional] 

### Return type

[**HaasscriptapiGetTestPatternsResponse**](HaasscriptapiGetTestPatternsResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **init_script**
> HaasscriptapiInitScriptResponse init_script(userid=userid, interfacekey=interfacekey, scriptid=scriptid, settings=settings)

Setup script and settings

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.HaasScriptAPIApi()
userid = 'userid_example' # str |  (optional)
interfacekey = 'interfacekey_example' # str |  (optional)
scriptid = 'scriptid_example' # str |  (optional)
settings = NULL # object |  (optional)

try:
    # Setup script and settings
    api_response = api_instance.init_script(userid=userid, interfacekey=interfacekey, scriptid=scriptid, settings=settings)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling HaasScriptAPIApi->init_script: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **userid** | **str**|  | [optional] 
 **interfacekey** | **str**|  | [optional] 
 **scriptid** | **str**|  | [optional] 
 **settings** | [**object**](.md)|  | [optional] 

### Return type

[**HaasscriptapiInitScriptResponse**](HaasscriptapiInitScriptResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **pattern_highscores**
> HaasscriptapiPatternHighscoresResponse pattern_highscores(userid=userid, interfacekey=interfacekey, patternid=patternid)

Returns the highet scores reached for a test pattern

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.HaasScriptAPIApi()
userid = 'userid_example' # str |  (optional)
interfacekey = 'interfacekey_example' # str |  (optional)
patternid = 56 # int |  (optional)

try:
    # Returns the highet scores reached for a test pattern
    api_response = api_instance.pattern_highscores(userid=userid, interfacekey=interfacekey, patternid=patternid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling HaasScriptAPIApi->pattern_highscores: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **userid** | **str**|  | [optional] 
 **interfacekey** | **str**|  | [optional] 
 **patternid** | **int**|  | [optional] 

### Return type

[**HaasscriptapiPatternHighscoresResponse**](HaasscriptapiPatternHighscoresResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **patterntest_script**
> HaasscriptapiPatterntestScriptResponse patterntest_script(userid=userid, interfacekey=interfacekey, backtestid=backtestid, scriptid=scriptid, settings=settings, patternwarmup=patternwarmup, patternid=patternid)

Executes a pattern test

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.HaasScriptAPIApi()
userid = 'userid_example' # str |  (optional)
interfacekey = 'interfacekey_example' # str |  (optional)
backtestid = 'backtestid_example' # str |  (optional)
scriptid = 'scriptid_example' # str |  (optional)
settings = NULL # object |  (optional)
patternwarmup = 56 # int |  (optional)
patternid = 56 # int |  (optional)

try:
    # Executes a pattern test
    api_response = api_instance.patterntest_script(userid=userid, interfacekey=interfacekey, backtestid=backtestid, scriptid=scriptid, settings=settings, patternwarmup=patternwarmup, patternid=patternid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling HaasScriptAPIApi->patterntest_script: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **userid** | **str**|  | [optional] 
 **interfacekey** | **str**|  | [optional] 
 **backtestid** | **str**|  | [optional] 
 **scriptid** | **str**|  | [optional] 
 **settings** | [**object**](.md)|  | [optional] 
 **patternwarmup** | **int**|  | [optional] 
 **patternid** | **int**|  | [optional] 

### Return type

[**HaasscriptapiPatterntestScriptResponse**](HaasscriptapiPatterntestScriptResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **profile_script**
> HaasscriptapiProfileScriptResponse profile_script(userid=userid, interfacekey=interfacekey, scriptid=scriptid)

Renders a profile of the given strategy

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.HaasScriptAPIApi()
userid = 'userid_example' # str |  (optional)
interfacekey = 'interfacekey_example' # str |  (optional)
scriptid = 'scriptid_example' # str |  (optional)

try:
    # Renders a profile of the given strategy
    api_response = api_instance.profile_script(userid=userid, interfacekey=interfacekey, scriptid=scriptid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling HaasScriptAPIApi->profile_script: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **userid** | **str**|  | [optional] 
 **interfacekey** | **str**|  | [optional] 
 **scriptid** | **str**|  | [optional] 

### Return type

[**HaasscriptapiProfileScriptResponse**](HaasscriptapiProfileScriptResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **publish_community_script**
> HaasscriptapiPublishCommunityScriptResponse publish_community_script(userid=userid, interfacekey=interfacekey, scriptid=scriptid)

Publishes the strategy to haasscript.com (not used)

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.HaasScriptAPIApi()
userid = 'userid_example' # str |  (optional)
interfacekey = 'interfacekey_example' # str |  (optional)
scriptid = 'scriptid_example' # str |  (optional)

try:
    # Publishes the strategy to haasscript.com (not used)
    api_response = api_instance.publish_community_script(userid=userid, interfacekey=interfacekey, scriptid=scriptid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling HaasScriptAPIApi->publish_community_script: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **userid** | **str**|  | [optional] 
 **interfacekey** | **str**|  | [optional] 
 **scriptid** | **str**|  | [optional] 

### Return type

[**HaasscriptapiPublishCommunityScriptResponse**](HaasscriptapiPublishCommunityScriptResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **publish_script**
> HaasscriptapiPublishScriptResponse publish_script(userid=userid, interfacekey=interfacekey, scriptid=scriptid)

Publishes the strategy to the webshop (not used)

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.HaasScriptAPIApi()
userid = 'userid_example' # str |  (optional)
interfacekey = 'interfacekey_example' # str |  (optional)
scriptid = 'scriptid_example' # str |  (optional)

try:
    # Publishes the strategy to the webshop (not used)
    api_response = api_instance.publish_script(userid=userid, interfacekey=interfacekey, scriptid=scriptid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling HaasScriptAPIApi->publish_script: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **userid** | **str**|  | [optional] 
 **interfacekey** | **str**|  | [optional] 
 **scriptid** | **str**|  | [optional] 

### Return type

[**HaasscriptapiPublishScriptResponse**](HaasscriptapiPublishScriptResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **quick_run_script**
> HaasscriptapiQuickRunScriptResponse quick_run_script(userid=userid, interfacekey=interfacekey, backtestid=backtestid, scriptid=scriptid, settings=settings)

Does a brief backtest

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.HaasScriptAPIApi()
userid = 'userid_example' # str |  (optional)
interfacekey = 'interfacekey_example' # str |  (optional)
backtestid = 'backtestid_example' # str |  (optional)
scriptid = 'scriptid_example' # str |  (optional)
settings = NULL # object |  (optional)

try:
    # Does a brief backtest
    api_response = api_instance.quick_run_script(userid=userid, interfacekey=interfacekey, backtestid=backtestid, scriptid=scriptid, settings=settings)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling HaasScriptAPIApi->quick_run_script: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **userid** | **str**|  | [optional] 
 **interfacekey** | **str**|  | [optional] 
 **backtestid** | **str**|  | [optional] 
 **scriptid** | **str**|  | [optional] 
 **settings** | [**object**](.md)|  | [optional] 

### Return type

[**HaasscriptapiQuickRunScriptResponse**](HaasscriptapiQuickRunScriptResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **restore_backup**
> HaasscriptapiRestoreBackupResponse restore_backup(userid=userid, interfacekey=interfacekey, scriptid=scriptid, wantedversion=wantedversion)

Restores a backup

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.HaasScriptAPIApi()
userid = 'userid_example' # str |  (optional)
interfacekey = 'interfacekey_example' # str |  (optional)
scriptid = 'scriptid_example' # str |  (optional)
wantedversion = 56 # int |  (optional)

try:
    # Restores a backup
    api_response = api_instance.restore_backup(userid=userid, interfacekey=interfacekey, scriptid=scriptid, wantedversion=wantedversion)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling HaasScriptAPIApi->restore_backup: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **userid** | **str**|  | [optional] 
 **interfacekey** | **str**|  | [optional] 
 **scriptid** | **str**|  | [optional] 
 **wantedversion** | **int**|  | [optional] 

### Return type

[**HaasscriptapiRestoreBackupResponse**](HaasscriptapiRestoreBackupResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **search_in_scripts**
> HaasscriptapiSearchInScriptsResponse search_in_scripts(userid=userid, interfacekey=interfacekey, searchkey=searchkey)

Tres to find code within the scripts

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.HaasScriptAPIApi()
userid = 'userid_example' # str |  (optional)
interfacekey = 'interfacekey_example' # str |  (optional)
searchkey = 'searchkey_example' # str |  (optional)

try:
    # Tres to find code within the scripts
    api_response = api_instance.search_in_scripts(userid=userid, interfacekey=interfacekey, searchkey=searchkey)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling HaasScriptAPIApi->search_in_scripts: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **userid** | **str**|  | [optional] 
 **interfacekey** | **str**|  | [optional] 
 **searchkey** | **str**|  | [optional] 

### Return type

[**HaasscriptapiSearchInScriptsResponse**](HaasscriptapiSearchInScriptsResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **unpublish_script**
> HaasscriptapiUnpublishScriptResponse unpublish_script(userid=userid, interfacekey=interfacekey, scriptid=scriptid)

Remove publication (not used)

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.HaasScriptAPIApi()
userid = 'userid_example' # str |  (optional)
interfacekey = 'interfacekey_example' # str |  (optional)
scriptid = 'scriptid_example' # str |  (optional)

try:
    # Remove publication (not used)
    api_response = api_instance.unpublish_script(userid=userid, interfacekey=interfacekey, scriptid=scriptid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling HaasScriptAPIApi->unpublish_script: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **userid** | **str**|  | [optional] 
 **interfacekey** | **str**|  | [optional] 
 **scriptid** | **str**|  | [optional] 

### Return type

[**HaasscriptapiUnpublishScriptResponse**](HaasscriptapiUnpublishScriptResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

