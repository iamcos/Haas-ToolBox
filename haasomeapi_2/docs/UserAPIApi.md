# swagger_client.UserAPIApi

All URIs are relative to *http://127.0.0.1:8090*

Method | HTTP request | Description
------------- | ------------- | -------------
[**app_login**](UserAPIApi.md#app_login) | **POST** /UserAPI.php?channel&#x3D;APP_LOGIN | The 3th party login
[**aprove_changelog**](UserAPIApi.md#aprove_changelog) | **POST** /UserAPI.php?channel&#x3D;APROVE_CHANGELOG | Sets approval to the latest changelog
[**check_token**](UserAPIApi.md#check_token) | **POST** /UserAPI.php?channel&#x3D;CHECK_TOKEN | This checks if the user login is still valid
[**download_notifications**](UserAPIApi.md#download_notifications) | **POST** /UserAPI.php?channel&#x3D;DOWNLOAD_NOTIFICATIONS | Returns all the user its notifications
[**get_notification_profile**](UserAPIApi.md#get_notification_profile) | **POST** /UserAPI.php?channel&#x3D;GET_NOTIFICATION_PROFILE | Return the notification profile
[**get_notifications**](UserAPIApi.md#get_notifications) | **POST** /UserAPI.php?channel&#x3D;GET_NOTIFICATIONS | Returns a list of all recent user notifications
[**get_supportkey**](UserAPIApi.md#get_supportkey) | **POST** /UserAPI.php?channel&#x3D;GET_SUPPORTKEY | Returns the current user support key
[**get_user_setting**](UserAPIApi.md#get_user_setting) | **POST** /UserAPI.php?channel&#x3D;GET_USER_SETTING | Returns the user its setting
[**is_telegram_setup**](UserAPIApi.md#is_telegram_setup) | **POST** /UserAPI.php?channel&#x3D;IS_TELEGRAM_SETUP | Returns if telegram has been setup
[**logout**](UserAPIApi.md#logout) | **POST** /UserAPI.php?channel&#x3D;LOGOUT | Logout procedure, valid for all login methods
[**refresh_supportkey**](UserAPIApi.md#refresh_supportkey) | **POST** /UserAPI.php?channel&#x3D;REFRESH_SUPPORTKEY | Refreshes the user support key
[**remove_telegram**](UserAPIApi.md#remove_telegram) | **POST** /UserAPI.php?channel&#x3D;REMOVE_TELEGRAM | Removes the telegram API keys
[**save_notification_profile**](UserAPIApi.md#save_notification_profile) | **POST** /UserAPI.php?channel&#x3D;SAVE_NOTIFICATION_PROFILE | Saves a new notification profile
[**set_user_setting**](UserAPIApi.md#set_user_setting) | **POST** /UserAPI.php?channel&#x3D;SET_USER_SETTING | Saves a user setting
[**setup_telegram**](UserAPIApi.md#setup_telegram) | **POST** /UserAPI.php?channel&#x3D;SETUP_TELEGRAM | To be used to setup a connection to telegram
[**test_telegram**](UserAPIApi.md#test_telegram) | **POST** /UserAPI.php?channel&#x3D;TEST_TELEGRAM | Sends a test message to telegram
[**user_changelog**](UserAPIApi.md#user_changelog) | **POST** /UserAPI.php?channel&#x3D;USER_CHANGELOG | Returns the changelog which the user has not approved yet

# **app_login**
> UserapiAppLoginResponse app_login(email=email, secretkey=secretkey, interfacekey=interfacekey, userspecs=userspecs)

The 3th party login

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.UserAPIApi()
email = 'email_example' # str |  (optional)
secretkey = 'secretkey_example' # str |  (optional)
interfacekey = 'interfacekey_example' # str |  (optional)
userspecs = NULL # object |  (optional)

try:
    # The 3th party login
    api_response = api_instance.app_login(email=email, secretkey=secretkey, interfacekey=interfacekey, userspecs=userspecs)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UserAPIApi->app_login: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **email** | **str**|  | [optional] 
 **secretkey** | **str**|  | [optional] 
 **interfacekey** | **str**|  | [optional] 
 **userspecs** | [**object**](.md)|  | [optional] 

### Return type

[**UserapiAppLoginResponse**](UserapiAppLoginResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **aprove_changelog**
> UserapiAproveChangelogResponse aprove_changelog(userid=userid, interfacekey=interfacekey)

Sets approval to the latest changelog

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.UserAPIApi()
userid = 'userid_example' # str |  (optional)
interfacekey = 'interfacekey_example' # str |  (optional)

try:
    # Sets approval to the latest changelog
    api_response = api_instance.aprove_changelog(userid=userid, interfacekey=interfacekey)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UserAPIApi->aprove_changelog: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **userid** | **str**|  | [optional] 
 **interfacekey** | **str**|  | [optional] 

### Return type

[**UserapiAproveChangelogResponse**](UserapiAproveChangelogResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **check_token**
> UserapiCheckTokenResponse check_token(userid=userid, interfacekey=interfacekey)

This checks if the user login is still valid

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.UserAPIApi()
userid = 'userid_example' # str |  (optional)
interfacekey = 'interfacekey_example' # str |  (optional)

try:
    # This checks if the user login is still valid
    api_response = api_instance.check_token(userid=userid, interfacekey=interfacekey)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UserAPIApi->check_token: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **userid** | **str**|  | [optional] 
 **interfacekey** | **str**|  | [optional] 

### Return type

[**UserapiCheckTokenResponse**](UserapiCheckTokenResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **download_notifications**
> UserapiDownloadNotificationsResponse download_notifications(userid=userid, interfacekey=interfacekey)

Returns all the user its notifications

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.UserAPIApi()
userid = 'userid_example' # str |  (optional)
interfacekey = 'interfacekey_example' # str |  (optional)

try:
    # Returns all the user its notifications
    api_response = api_instance.download_notifications(userid=userid, interfacekey=interfacekey)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UserAPIApi->download_notifications: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **userid** | **str**|  | [optional] 
 **interfacekey** | **str**|  | [optional] 

### Return type

[**UserapiDownloadNotificationsResponse**](UserapiDownloadNotificationsResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_notification_profile**
> UserapiGetNotificationProfileResponse get_notification_profile(userid=userid, profiletype=profiletype)

Return the notification profile

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.UserAPIApi()
userid = 'userid_example' # str |  (optional)
profiletype = 56 # int |  (optional)

try:
    # Return the notification profile
    api_response = api_instance.get_notification_profile(userid=userid, profiletype=profiletype)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UserAPIApi->get_notification_profile: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **userid** | **str**|  | [optional] 
 **profiletype** | **int**|  | [optional] 

### Return type

[**UserapiGetNotificationProfileResponse**](UserapiGetNotificationProfileResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_notifications**
> UserapiGetNotificationsResponse get_notifications(userid=userid, interfacekey=interfacekey)

Returns a list of all recent user notifications

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.UserAPIApi()
userid = 'userid_example' # str |  (optional)
interfacekey = 'interfacekey_example' # str |  (optional)

try:
    # Returns a list of all recent user notifications
    api_response = api_instance.get_notifications(userid=userid, interfacekey=interfacekey)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UserAPIApi->get_notifications: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **userid** | **str**|  | [optional] 
 **interfacekey** | **str**|  | [optional] 

### Return type

[**UserapiGetNotificationsResponse**](UserapiGetNotificationsResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_supportkey**
> UserapiGetSupportkeyResponse get_supportkey(userid=userid, interfacekey=interfacekey)

Returns the current user support key

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.UserAPIApi()
userid = 'userid_example' # str |  (optional)
interfacekey = 'interfacekey_example' # str |  (optional)

try:
    # Returns the current user support key
    api_response = api_instance.get_supportkey(userid=userid, interfacekey=interfacekey)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UserAPIApi->get_supportkey: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **userid** | **str**|  | [optional] 
 **interfacekey** | **str**|  | [optional] 

### Return type

[**UserapiGetSupportkeyResponse**](UserapiGetSupportkeyResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_user_setting**
> UserapiGetUserSettingResponse get_user_setting(userid=userid, interfacekey=interfacekey, key=key)

Returns the user its setting

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.UserAPIApi()
userid = 'userid_example' # str |  (optional)
interfacekey = 'interfacekey_example' # str |  (optional)
key = 'key_example' # str |  (optional)

try:
    # Returns the user its setting
    api_response = api_instance.get_user_setting(userid=userid, interfacekey=interfacekey, key=key)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UserAPIApi->get_user_setting: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **userid** | **str**|  | [optional] 
 **interfacekey** | **str**|  | [optional] 
 **key** | **str**|  | [optional] 

### Return type

[**UserapiGetUserSettingResponse**](UserapiGetUserSettingResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **is_telegram_setup**
> UserapiIsTelegramSetupResponse is_telegram_setup(userid=userid, interfacekey=interfacekey)

Returns if telegram has been setup

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.UserAPIApi()
userid = 'userid_example' # str |  (optional)
interfacekey = 'interfacekey_example' # str |  (optional)

try:
    # Returns if telegram has been setup
    api_response = api_instance.is_telegram_setup(userid=userid, interfacekey=interfacekey)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UserAPIApi->is_telegram_setup: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **userid** | **str**|  | [optional] 
 **interfacekey** | **str**|  | [optional] 

### Return type

[**UserapiIsTelegramSetupResponse**](UserapiIsTelegramSetupResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **logout**
> UserapiLogoutResponse logout(userid=userid, interfacekey=interfacekey)

Logout procedure, valid for all login methods

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.UserAPIApi()
userid = 'userid_example' # str |  (optional)
interfacekey = 'interfacekey_example' # str |  (optional)

try:
    # Logout procedure, valid for all login methods
    api_response = api_instance.logout(userid=userid, interfacekey=interfacekey)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UserAPIApi->logout: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **userid** | **str**|  | [optional] 
 **interfacekey** | **str**|  | [optional] 

### Return type

[**UserapiLogoutResponse**](UserapiLogoutResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **refresh_supportkey**
> UserapiRefreshSupportkeyResponse refresh_supportkey(userid=userid, interfacekey=interfacekey)

Refreshes the user support key

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.UserAPIApi()
userid = 'userid_example' # str |  (optional)
interfacekey = 'interfacekey_example' # str |  (optional)

try:
    # Refreshes the user support key
    api_response = api_instance.refresh_supportkey(userid=userid, interfacekey=interfacekey)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UserAPIApi->refresh_supportkey: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **userid** | **str**|  | [optional] 
 **interfacekey** | **str**|  | [optional] 

### Return type

[**UserapiRefreshSupportkeyResponse**](UserapiRefreshSupportkeyResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **remove_telegram**
> UserapiRemoveTelegramResponse remove_telegram(userid=userid, interfacekey=interfacekey)

Removes the telegram API keys

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.UserAPIApi()
userid = 'userid_example' # str |  (optional)
interfacekey = 'interfacekey_example' # str |  (optional)

try:
    # Removes the telegram API keys
    api_response = api_instance.remove_telegram(userid=userid, interfacekey=interfacekey)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UserAPIApi->remove_telegram: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **userid** | **str**|  | [optional] 
 **interfacekey** | **str**|  | [optional] 

### Return type

[**UserapiRemoveTelegramResponse**](UserapiRemoveTelegramResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **save_notification_profile**
> UserapiSaveNotificationProfileResponse save_notification_profile(userid=userid, profile=profile, profiletype=profiletype)

Saves a new notification profile

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.UserAPIApi()
userid = 'userid_example' # str |  (optional)
profile = NULL # object |  (optional)
profiletype = 56 # int |  (optional)

try:
    # Saves a new notification profile
    api_response = api_instance.save_notification_profile(userid=userid, profile=profile, profiletype=profiletype)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UserAPIApi->save_notification_profile: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **userid** | **str**|  | [optional] 
 **profile** | [**object**](.md)|  | [optional] 
 **profiletype** | **int**|  | [optional] 

### Return type

[**UserapiSaveNotificationProfileResponse**](UserapiSaveNotificationProfileResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **set_user_setting**
> UserapiSetUserSettingResponse set_user_setting(userid=userid, interfacekey=interfacekey, key=key, value=value)

Saves a user setting

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.UserAPIApi()
userid = 'userid_example' # str |  (optional)
interfacekey = 'interfacekey_example' # str |  (optional)
key = 'key_example' # str |  (optional)
value = 'value_example' # str |  (optional)

try:
    # Saves a user setting
    api_response = api_instance.set_user_setting(userid=userid, interfacekey=interfacekey, key=key, value=value)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UserAPIApi->set_user_setting: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **userid** | **str**|  | [optional] 
 **interfacekey** | **str**|  | [optional] 
 **key** | **str**|  | [optional] 
 **value** | **str**|  | [optional] 

### Return type

[**UserapiSetUserSettingResponse**](UserapiSetUserSettingResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **setup_telegram**
> UserapiSetupTelegramResponse setup_telegram(userid=userid, interfacekey=interfacekey, token=token)

To be used to setup a connection to telegram

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.UserAPIApi()
userid = 'userid_example' # str |  (optional)
interfacekey = 'interfacekey_example' # str |  (optional)
token = 'token_example' # str |  (optional)

try:
    # To be used to setup a connection to telegram
    api_response = api_instance.setup_telegram(userid=userid, interfacekey=interfacekey, token=token)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UserAPIApi->setup_telegram: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **userid** | **str**|  | [optional] 
 **interfacekey** | **str**|  | [optional] 
 **token** | **str**|  | [optional] 

### Return type

[**UserapiSetupTelegramResponse**](UserapiSetupTelegramResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **test_telegram**
> UserapiTestTelegramResponse test_telegram(userid=userid, interfacekey=interfacekey)

Sends a test message to telegram

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.UserAPIApi()
userid = 'userid_example' # str |  (optional)
interfacekey = 'interfacekey_example' # str |  (optional)

try:
    # Sends a test message to telegram
    api_response = api_instance.test_telegram(userid=userid, interfacekey=interfacekey)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UserAPIApi->test_telegram: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **userid** | **str**|  | [optional] 
 **interfacekey** | **str**|  | [optional] 

### Return type

[**UserapiTestTelegramResponse**](UserapiTestTelegramResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **user_changelog**
> UserapiUserChangelogResponse user_changelog(userid=userid, interfacekey=interfacekey)

Returns the changelog which the user has not approved yet

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.UserAPIApi()
userid = 'userid_example' # str |  (optional)
interfacekey = 'interfacekey_example' # str |  (optional)

try:
    # Returns the changelog which the user has not approved yet
    api_response = api_instance.user_changelog(userid=userid, interfacekey=interfacekey)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UserAPIApi->user_changelog: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **userid** | **str**|  | [optional] 
 **interfacekey** | **str**|  | [optional] 

### Return type

[**UserapiUserChangelogResponse**](UserapiUserChangelogResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

