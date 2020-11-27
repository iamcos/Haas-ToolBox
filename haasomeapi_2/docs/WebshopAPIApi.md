# swagger_client.WebshopAPIApi

All URIs are relative to *http://127.0.0.1:8090*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_my_orders**](WebshopAPIApi.md#get_my_orders) | **POST** /WebshopAPI.php?channel&#x3D;GET_MY_ORDERS | Returns a list of all the user its orders
[**get_my_products**](WebshopAPIApi.md#get_my_products) | **POST** /WebshopAPI.php?channel&#x3D;GET_MY_PRODUCTS | Returns a list of all the user its products in the webshop
[**remove_product**](WebshopAPIApi.md#remove_product) | **POST** /WebshopAPI.php?channel&#x3D;REMOVE_PRODUCT | Delete/remove a product from the webshop

# **get_my_orders**
> WebshopapiGetMyOrdersResponse get_my_orders(userid=userid, interfacekey=interfacekey)

Returns a list of all the user its orders

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.WebshopAPIApi()
userid = 'userid_example' # str |  (optional)
interfacekey = 'interfacekey_example' # str |  (optional)

try:
    # Returns a list of all the user its orders
    api_response = api_instance.get_my_orders(userid=userid, interfacekey=interfacekey)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WebshopAPIApi->get_my_orders: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **userid** | **str**|  | [optional] 
 **interfacekey** | **str**|  | [optional] 

### Return type

[**WebshopapiGetMyOrdersResponse**](WebshopapiGetMyOrdersResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_my_products**
> WebshopapiGetMyProductsResponse get_my_products(userid=userid, interfacekey=interfacekey)

Returns a list of all the user its products in the webshop

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.WebshopAPIApi()
userid = 'userid_example' # str |  (optional)
interfacekey = 'interfacekey_example' # str |  (optional)

try:
    # Returns a list of all the user its products in the webshop
    api_response = api_instance.get_my_products(userid=userid, interfacekey=interfacekey)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WebshopAPIApi->get_my_products: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **userid** | **str**|  | [optional] 
 **interfacekey** | **str**|  | [optional] 

### Return type

[**WebshopapiGetMyProductsResponse**](WebshopapiGetMyProductsResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **remove_product**
> WebshopapiRemoveProductResponse remove_product(userid=userid, interfacekey=interfacekey, sku=sku)

Delete/remove a product from the webshop

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.WebshopAPIApi()
userid = 'userid_example' # str |  (optional)
interfacekey = 'interfacekey_example' # str |  (optional)
sku = 'sku_example' # str |  (optional)

try:
    # Delete/remove a product from the webshop
    api_response = api_instance.remove_product(userid=userid, interfacekey=interfacekey, sku=sku)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WebshopAPIApi->remove_product: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **userid** | **str**|  | [optional] 
 **interfacekey** | **str**|  | [optional] 
 **sku** | **str**|  | [optional] 

### Return type

[**WebshopapiRemoveProductResponse**](WebshopapiRemoveProductResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

