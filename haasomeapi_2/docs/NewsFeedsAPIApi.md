# swagger_client.NewsFeedsAPIApi

All URIs are relative to *http://127.0.0.1:8090*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_headlines_on_group**](NewsFeedsAPIApi.md#get_headlines_on_group) | **POST** /NewsFeedsAPI.php?channel&#x3D;GET_HEADLINES_ON_GROUP | Returns all headlines on group
[**get_headlines_on_key**](NewsFeedsAPIApi.md#get_headlines_on_key) | **POST** /NewsFeedsAPI.php?channel&#x3D;GET_HEADLINES_ON_KEY | Returns all news xxxxxx
[**get_headlines_on_name**](NewsFeedsAPIApi.md#get_headlines_on_name) | **POST** /NewsFeedsAPI.php?channel&#x3D;GET_HEADLINES_ON_NAME | Returns all news per id
[**get_market_news**](NewsFeedsAPIApi.md#get_market_news) | **POST** /NewsFeedsAPI.php?channel&#x3D;GET_MARKET_NEWS | Returns all news related to the given market
[**get_news_feed_groups**](NewsFeedsAPIApi.md#get_news_feed_groups) | **POST** /NewsFeedsAPI.php?channel&#x3D;GET_NEWS_FEED_GROUPS | Returns all news groups
[**get_news_feed_sources**](NewsFeedsAPIApi.md#get_news_feed_sources) | **POST** /NewsFeedsAPI.php?channel&#x3D;GET_NEWS_FEED_SOURCES | Returns all news sources
[**get_news_page**](NewsFeedsAPIApi.md#get_news_page) | **POST** /NewsFeedsAPI.php?channel&#x3D;GET_NEWS_PAGE | Returns all news for the news-page
[**get_video_feed_sources**](NewsFeedsAPIApi.md#get_video_feed_sources) | **POST** /NewsFeedsAPI.php?channel&#x3D;GET_VIDEO_FEED_SOURCES | Returns all videostream sources

# **get_headlines_on_group**
> NewsfeedsapiGetHeadlinesOnGroupResponse get_headlines_on_group(group=group)

Returns all headlines on group

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.NewsFeedsAPIApi()
group = 'group_example' # str |  (optional)

try:
    # Returns all headlines on group
    api_response = api_instance.get_headlines_on_group(group=group)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling NewsFeedsAPIApi->get_headlines_on_group: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **group** | **str**|  | [optional] 

### Return type

[**NewsfeedsapiGetHeadlinesOnGroupResponse**](NewsfeedsapiGetHeadlinesOnGroupResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_headlines_on_key**
> NewsfeedsapiGetHeadlinesOnKeyResponse get_headlines_on_key(group=group, key=key)

Returns all news xxxxxx

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.NewsFeedsAPIApi()
group = 'group_example' # str |  (optional)
key = 'key_example' # str |  (optional)

try:
    # Returns all news xxxxxx
    api_response = api_instance.get_headlines_on_key(group=group, key=key)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling NewsFeedsAPIApi->get_headlines_on_key: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **group** | **str**|  | [optional] 
 **key** | **str**|  | [optional] 

### Return type

[**NewsfeedsapiGetHeadlinesOnKeyResponse**](NewsfeedsapiGetHeadlinesOnKeyResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_headlines_on_name**
> NewsfeedsapiGetHeadlinesOnNameResponse get_headlines_on_name(id=id)

Returns all news per id

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.NewsFeedsAPIApi()
id = 'id_example' # str |  (optional)

try:
    # Returns all news per id
    api_response = api_instance.get_headlines_on_name(id=id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling NewsFeedsAPIApi->get_headlines_on_name: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | [optional] 

### Return type

[**NewsfeedsapiGetHeadlinesOnNameResponse**](NewsfeedsapiGetHeadlinesOnNameResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_market_news**
> NewsfeedsapiGetMarketNewsResponse get_market_news(userid=userid, interfacekey=interfacekey, market=market)

Returns all news related to the given market

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.NewsFeedsAPIApi()
userid = 'userid_example' # str |  (optional)
interfacekey = 'interfacekey_example' # str |  (optional)
market = 'market_example' # str |  (optional)

try:
    # Returns all news related to the given market
    api_response = api_instance.get_market_news(userid=userid, interfacekey=interfacekey, market=market)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling NewsFeedsAPIApi->get_market_news: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **userid** | **str**|  | [optional] 
 **interfacekey** | **str**|  | [optional] 
 **market** | **str**|  | [optional] 

### Return type

[**NewsfeedsapiGetMarketNewsResponse**](NewsfeedsapiGetMarketNewsResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_news_feed_groups**
> NewsfeedsapiGetNewsFeedGroupsResponse get_news_feed_groups()

Returns all news groups

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.NewsFeedsAPIApi()

try:
    # Returns all news groups
    api_response = api_instance.get_news_feed_groups()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling NewsFeedsAPIApi->get_news_feed_groups: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**NewsfeedsapiGetNewsFeedGroupsResponse**](NewsfeedsapiGetNewsFeedGroupsResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_news_feed_sources**
> NewsfeedsapiGetNewsFeedSourcesResponse get_news_feed_sources()

Returns all news sources

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.NewsFeedsAPIApi()

try:
    # Returns all news sources
    api_response = api_instance.get_news_feed_sources()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling NewsFeedsAPIApi->get_news_feed_sources: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**NewsfeedsapiGetNewsFeedSourcesResponse**](NewsfeedsapiGetNewsFeedSourcesResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_news_page**
> NewsfeedsapiGetNewsPageResponse get_news_page(userid=userid, interfacekey=interfacekey)

Returns all news for the news-page

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.NewsFeedsAPIApi()
userid = 'userid_example' # str |  (optional)
interfacekey = 'interfacekey_example' # str |  (optional)

try:
    # Returns all news for the news-page
    api_response = api_instance.get_news_page(userid=userid, interfacekey=interfacekey)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling NewsFeedsAPIApi->get_news_page: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **userid** | **str**|  | [optional] 
 **interfacekey** | **str**|  | [optional] 

### Return type

[**NewsfeedsapiGetNewsPageResponse**](NewsfeedsapiGetNewsPageResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_video_feed_sources**
> NewsfeedsapiGetVideoFeedSourcesResponse get_video_feed_sources()

Returns all videostream sources

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.NewsFeedsAPIApi()

try:
    # Returns all videostream sources
    api_response = api_instance.get_video_feed_sources()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling NewsFeedsAPIApi->get_video_feed_sources: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**NewsfeedsapiGetVideoFeedSourcesResponse**](NewsfeedsapiGetVideoFeedSourcesResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

