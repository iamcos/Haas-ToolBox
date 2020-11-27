# swagger_client.InterfaceAPIApi

All URIs are relative to *http://127.0.0.1:8090*

Method | HTTP request | Description
------------- | ------------- | -------------
[**changelog**](InterfaceAPIApi.md#changelog) | **POST** /InterfaceAPI.php?channel&#x3D;CHANGELOG | Returns the full change-log
[**get_blog_categories**](InterfaceAPIApi.md#get_blog_categories) | **POST** /InterfaceAPI.php?channel&#x3D;GET_BLOG_CATEGORIES | Returns all the blog catagories
[**get_blog_post**](InterfaceAPIApi.md#get_blog_post) | **POST** /InterfaceAPI.php?channel&#x3D;GET_BLOG_POST | Returns a blogpost
[**init_data**](InterfaceAPIApi.md#init_data) | **POST** /InterfaceAPI.php?channel&#x3D;INIT_DATA | Returns basic operational information, like the supported exchanges, pricesources and so on...
[**market_info**](InterfaceAPIApi.md#market_info) | **POST** /InterfaceAPI.php?channel&#x3D;MARKET_INFO | Returns the market information page
[**market_price_info**](InterfaceAPIApi.md#market_price_info) | **POST** /InterfaceAPI.php?channel&#x3D;MARKET_PRICE_INFO | Returns the market price information page
[**market_ta_info**](InterfaceAPIApi.md#market_ta_info) | **POST** /InterfaceAPI.php?channel&#x3D;MARKET_TA_INFO | Returns the market price technical analysis page
[**search_blog**](InterfaceAPIApi.md#search_blog) | **POST** /InterfaceAPI.php?channel&#x3D;SEARCH_BLOG | Searches the cloud its blog postings
[**website_privacy**](InterfaceAPIApi.md#website_privacy) | **POST** /InterfaceAPI.php?channel&#x3D;WEBSITE_PRIVACY | 
[**website_security**](InterfaceAPIApi.md#website_security) | **POST** /InterfaceAPI.php?channel&#x3D;WEBSITE_SECURITY | 
[**website_terms**](InterfaceAPIApi.md#website_terms) | **POST** /InterfaceAPI.php?channel&#x3D;WEBSITE_TERMS | 

# **changelog**
> InterfaceapiChangelogResponse changelog(userid=userid, interfacekey=interfacekey)

Returns the full change-log

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.InterfaceAPIApi()
userid = 'userid_example' # str |  (optional)
interfacekey = 'interfacekey_example' # str |  (optional)

try:
    # Returns the full change-log
    api_response = api_instance.changelog(userid=userid, interfacekey=interfacekey)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling InterfaceAPIApi->changelog: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **userid** | **str**|  | [optional] 
 **interfacekey** | **str**|  | [optional] 

### Return type

[**InterfaceapiChangelogResponse**](InterfaceapiChangelogResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_blog_categories**
> InterfaceapiGetBlogCategoriesResponse get_blog_categories(userid=userid, interfacekey=interfacekey)

Returns all the blog catagories

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.InterfaceAPIApi()
userid = 'userid_example' # str |  (optional)
interfacekey = 'interfacekey_example' # str |  (optional)

try:
    # Returns all the blog catagories
    api_response = api_instance.get_blog_categories(userid=userid, interfacekey=interfacekey)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling InterfaceAPIApi->get_blog_categories: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **userid** | **str**|  | [optional] 
 **interfacekey** | **str**|  | [optional] 

### Return type

[**InterfaceapiGetBlogCategoriesResponse**](InterfaceapiGetBlogCategoriesResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_blog_post**
> InterfaceapiGetBlogPostResponse get_blog_post(id=id)

Returns a blogpost

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.InterfaceAPIApi()
id = 'id_example' # str |  (optional)

try:
    # Returns a blogpost
    api_response = api_instance.get_blog_post(id=id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling InterfaceAPIApi->get_blog_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | [optional] 

### Return type

[**InterfaceapiGetBlogPostResponse**](InterfaceapiGetBlogPostResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **init_data**
> InterfaceapiInitDataResponse init_data()

Returns basic operational information, like the supported exchanges, pricesources and so on...

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.InterfaceAPIApi()

try:
    # Returns basic operational information, like the supported exchanges, pricesources and so on...
    api_response = api_instance.init_data()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling InterfaceAPIApi->init_data: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**InterfaceapiInitDataResponse**](InterfaceapiInitDataResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **market_info**
> InterfaceapiMarketInfoResponse market_info(userid=userid, interfacekey=interfacekey, market=market)

Returns the market information page

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.InterfaceAPIApi()
userid = 'userid_example' # str |  (optional)
interfacekey = 'interfacekey_example' # str |  (optional)
market = 'market_example' # str |  (optional)

try:
    # Returns the market information page
    api_response = api_instance.market_info(userid=userid, interfacekey=interfacekey, market=market)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling InterfaceAPIApi->market_info: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **userid** | **str**|  | [optional] 
 **interfacekey** | **str**|  | [optional] 
 **market** | **str**|  | [optional] 

### Return type

[**InterfaceapiMarketInfoResponse**](InterfaceapiMarketInfoResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **market_price_info**
> InterfaceapiMarketPriceInfoResponse market_price_info(userid=userid, interfacekey=interfacekey, market=market)

Returns the market price information page

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.InterfaceAPIApi()
userid = 'userid_example' # str |  (optional)
interfacekey = 'interfacekey_example' # str |  (optional)
market = 'market_example' # str |  (optional)

try:
    # Returns the market price information page
    api_response = api_instance.market_price_info(userid=userid, interfacekey=interfacekey, market=market)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling InterfaceAPIApi->market_price_info: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **userid** | **str**|  | [optional] 
 **interfacekey** | **str**|  | [optional] 
 **market** | **str**|  | [optional] 

### Return type

[**InterfaceapiMarketPriceInfoResponse**](InterfaceapiMarketPriceInfoResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **market_ta_info**
> InterfaceapiMarketTaInfoResponse market_ta_info(userid=userid, interfacekey=interfacekey, market=market)

Returns the market price technical analysis page

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.InterfaceAPIApi()
userid = 'userid_example' # str |  (optional)
interfacekey = 'interfacekey_example' # str |  (optional)
market = 'market_example' # str |  (optional)

try:
    # Returns the market price technical analysis page
    api_response = api_instance.market_ta_info(userid=userid, interfacekey=interfacekey, market=market)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling InterfaceAPIApi->market_ta_info: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **userid** | **str**|  | [optional] 
 **interfacekey** | **str**|  | [optional] 
 **market** | **str**|  | [optional] 

### Return type

[**InterfaceapiMarketTaInfoResponse**](InterfaceapiMarketTaInfoResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **search_blog**
> InterfaceapiSearchBlogResponse search_blog(userid=userid, interfacekey=interfacekey, category=category, searchkey=searchkey)

Searches the cloud its blog postings

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.InterfaceAPIApi()
userid = 'userid_example' # str |  (optional)
interfacekey = 'interfacekey_example' # str |  (optional)
category = 'category_example' # str |  (optional)
searchkey = 'searchkey_example' # str |  (optional)

try:
    # Searches the cloud its blog postings
    api_response = api_instance.search_blog(userid=userid, interfacekey=interfacekey, category=category, searchkey=searchkey)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling InterfaceAPIApi->search_blog: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **userid** | **str**|  | [optional] 
 **interfacekey** | **str**|  | [optional] 
 **category** | **str**|  | [optional] 
 **searchkey** | **str**|  | [optional] 

### Return type

[**InterfaceapiSearchBlogResponse**](InterfaceapiSearchBlogResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **website_privacy**
> website_privacy()



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.InterfaceAPIApi()

try:
    api_instance.website_privacy()
except ApiException as e:
    print("Exception when calling InterfaceAPIApi->website_privacy: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **website_security**
> website_security()



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.InterfaceAPIApi()

try:
    api_instance.website_security()
except ApiException as e:
    print("Exception when calling InterfaceAPIApi->website_security: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **website_terms**
> website_terms()



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.InterfaceAPIApi()

try:
    api_instance.website_terms()
except ApiException as e:
    print("Exception when calling InterfaceAPIApi->website_terms: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

