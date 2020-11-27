# swagger_client.DashboardAPIApi

All URIs are relative to *http://127.0.0.1:8090*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_dashboard**](DashboardAPIApi.md#add_dashboard) | **POST** /DashboardAPI.php?channel&#x3D;ADD_DASHBOARD | Add a new dashboard
[**add_widget**](DashboardAPIApi.md#add_widget) | **POST** /DashboardAPI.php?channel&#x3D;ADD_WIDGET | Adds a new widget to a dashboard
[**clear_dashboard**](DashboardAPIApi.md#clear_dashboard) | **POST** /DashboardAPI.php?channel&#x3D;CLEAR_DASHBOARD | Clears a dashboard (removes all widges from it)
[**clone_dashboard**](DashboardAPIApi.md#clone_dashboard) | **POST** /DashboardAPI.php?channel&#x3D;CLONE_DASHBOARD | Clones a dashboard
[**clone_widget**](DashboardAPIApi.md#clone_widget) | **POST** /DashboardAPI.php?channel&#x3D;CLONE_WIDGET | Clone a widget
[**delete_dashboard**](DashboardAPIApi.md#delete_dashboard) | **POST** /DashboardAPI.php?channel&#x3D;DELETE_DASHBOARD | Delete/remove a dashboard
[**delete_widget**](DashboardAPIApi.md#delete_widget) | **POST** /DashboardAPI.php?channel&#x3D;DELETE_WIDGET | Delete/remove a widget
[**edit_dashboard**](DashboardAPIApi.md#edit_dashboard) | **POST** /DashboardAPI.php?channel&#x3D;EDIT_DASHBOARD | Edits a dashboard name
[**get_dashboards**](DashboardAPIApi.md#get_dashboards) | **POST** /DashboardAPI.php?channel&#x3D;GET_DASHBOARDS | Returns a dictionary of all dashbaord containing their id and name
[**get_widgets**](DashboardAPIApi.md#get_widgets) | **POST** /DashboardAPI.php?channel&#x3D;GET_WIDGETS | Returns all widgets registered on the dashboard
[**move_widget**](DashboardAPIApi.md#move_widget) | **POST** /DashboardAPI.php?channel&#x3D;MOVE_WIDGET | Moves a widget around
[**setup_widget**](DashboardAPIApi.md#setup_widget) | **POST** /DashboardAPI.php?channel&#x3D;SETUP_WIDGET | Setup a widget its properties

# **add_dashboard**
> DashboardapiAddDashboardResponse add_dashboard(userid=userid, interfacekey=interfacekey, name=name)

Add a new dashboard

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DashboardAPIApi()
userid = 'userid_example' # str |  (optional)
interfacekey = 'interfacekey_example' # str |  (optional)
name = 'name_example' # str |  (optional)

try:
    # Add a new dashboard
    api_response = api_instance.add_dashboard(userid=userid, interfacekey=interfacekey, name=name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DashboardAPIApi->add_dashboard: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **userid** | **str**|  | [optional] 
 **interfacekey** | **str**|  | [optional] 
 **name** | **str**|  | [optional] 

### Return type

[**DashboardapiAddDashboardResponse**](DashboardapiAddDashboardResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **add_widget**
> DashboardapiAddWidgetResponse add_widget(userid=userid, interfacekey=interfacekey, dashboardid=dashboardid, type=type, x=x, y=y, z=z, width=width, height=height)

Adds a new widget to a dashboard

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DashboardAPIApi()
userid = 'userid_example' # str |  (optional)
interfacekey = 'interfacekey_example' # str |  (optional)
dashboardid = 'dashboardid_example' # str |  (optional)
type = 'type_example' # str |  (optional)
x = 56 # int |  (optional)
y = 56 # int |  (optional)
z = 56 # int |  (optional)
width = 56 # int |  (optional)
height = 56 # int |  (optional)

try:
    # Adds a new widget to a dashboard
    api_response = api_instance.add_widget(userid=userid, interfacekey=interfacekey, dashboardid=dashboardid, type=type, x=x, y=y, z=z, width=width, height=height)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DashboardAPIApi->add_widget: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **userid** | **str**|  | [optional] 
 **interfacekey** | **str**|  | [optional] 
 **dashboardid** | **str**|  | [optional] 
 **type** | **str**|  | [optional] 
 **x** | **int**|  | [optional] 
 **y** | **int**|  | [optional] 
 **z** | **int**|  | [optional] 
 **width** | **int**|  | [optional] 
 **height** | **int**|  | [optional] 

### Return type

[**DashboardapiAddWidgetResponse**](DashboardapiAddWidgetResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **clear_dashboard**
> DashboardapiClearDashboardResponse clear_dashboard(userid=userid, interfacekey=interfacekey, dashboardid=dashboardid)

Clears a dashboard (removes all widges from it)

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DashboardAPIApi()
userid = 'userid_example' # str |  (optional)
interfacekey = 'interfacekey_example' # str |  (optional)
dashboardid = 'dashboardid_example' # str |  (optional)

try:
    # Clears a dashboard (removes all widges from it)
    api_response = api_instance.clear_dashboard(userid=userid, interfacekey=interfacekey, dashboardid=dashboardid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DashboardAPIApi->clear_dashboard: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **userid** | **str**|  | [optional] 
 **interfacekey** | **str**|  | [optional] 
 **dashboardid** | **str**|  | [optional] 

### Return type

[**DashboardapiClearDashboardResponse**](DashboardapiClearDashboardResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **clone_dashboard**
> DashboardapiCloneDashboardResponse clone_dashboard(userid=userid, interfacekey=interfacekey, dashboardid=dashboardid, name=name)

Clones a dashboard

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DashboardAPIApi()
userid = 'userid_example' # str |  (optional)
interfacekey = 'interfacekey_example' # str |  (optional)
dashboardid = 'dashboardid_example' # str |  (optional)
name = 'name_example' # str |  (optional)

try:
    # Clones a dashboard
    api_response = api_instance.clone_dashboard(userid=userid, interfacekey=interfacekey, dashboardid=dashboardid, name=name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DashboardAPIApi->clone_dashboard: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **userid** | **str**|  | [optional] 
 **interfacekey** | **str**|  | [optional] 
 **dashboardid** | **str**|  | [optional] 
 **name** | **str**|  | [optional] 

### Return type

[**DashboardapiCloneDashboardResponse**](DashboardapiCloneDashboardResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **clone_widget**
> DashboardapiCloneWidgetResponse clone_widget(userid=userid, interfacekey=interfacekey, widgetid=widgetid, x=x, y=y, z=z)

Clone a widget

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DashboardAPIApi()
userid = 'userid_example' # str |  (optional)
interfacekey = 'interfacekey_example' # str |  (optional)
widgetid = 'widgetid_example' # str |  (optional)
x = 56 # int |  (optional)
y = 56 # int |  (optional)
z = 56 # int |  (optional)

try:
    # Clone a widget
    api_response = api_instance.clone_widget(userid=userid, interfacekey=interfacekey, widgetid=widgetid, x=x, y=y, z=z)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DashboardAPIApi->clone_widget: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **userid** | **str**|  | [optional] 
 **interfacekey** | **str**|  | [optional] 
 **widgetid** | **str**|  | [optional] 
 **x** | **int**|  | [optional] 
 **y** | **int**|  | [optional] 
 **z** | **int**|  | [optional] 

### Return type

[**DashboardapiCloneWidgetResponse**](DashboardapiCloneWidgetResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_dashboard**
> DashboardapiDeleteDashboardResponse delete_dashboard(userid=userid, interfacekey=interfacekey, dashboardid=dashboardid)

Delete/remove a dashboard

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DashboardAPIApi()
userid = 'userid_example' # str |  (optional)
interfacekey = 'interfacekey_example' # str |  (optional)
dashboardid = 'dashboardid_example' # str |  (optional)

try:
    # Delete/remove a dashboard
    api_response = api_instance.delete_dashboard(userid=userid, interfacekey=interfacekey, dashboardid=dashboardid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DashboardAPIApi->delete_dashboard: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **userid** | **str**|  | [optional] 
 **interfacekey** | **str**|  | [optional] 
 **dashboardid** | **str**|  | [optional] 

### Return type

[**DashboardapiDeleteDashboardResponse**](DashboardapiDeleteDashboardResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_widget**
> DashboardapiDeleteWidgetResponse delete_widget(userid=userid, interfacekey=interfacekey, dashboardid=dashboardid, widgetid=widgetid)

Delete/remove a widget

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DashboardAPIApi()
userid = 'userid_example' # str |  (optional)
interfacekey = 'interfacekey_example' # str |  (optional)
dashboardid = 'dashboardid_example' # str |  (optional)
widgetid = 'widgetid_example' # str |  (optional)

try:
    # Delete/remove a widget
    api_response = api_instance.delete_widget(userid=userid, interfacekey=interfacekey, dashboardid=dashboardid, widgetid=widgetid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DashboardAPIApi->delete_widget: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **userid** | **str**|  | [optional] 
 **interfacekey** | **str**|  | [optional] 
 **dashboardid** | **str**|  | [optional] 
 **widgetid** | **str**|  | [optional] 

### Return type

[**DashboardapiDeleteWidgetResponse**](DashboardapiDeleteWidgetResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **edit_dashboard**
> DashboardapiEditDashboardResponse edit_dashboard(userid=userid, interfacekey=interfacekey, dashboardid=dashboardid, name=name)

Edits a dashboard name

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DashboardAPIApi()
userid = 'userid_example' # str |  (optional)
interfacekey = 'interfacekey_example' # str |  (optional)
dashboardid = 'dashboardid_example' # str |  (optional)
name = 'name_example' # str |  (optional)

try:
    # Edits a dashboard name
    api_response = api_instance.edit_dashboard(userid=userid, interfacekey=interfacekey, dashboardid=dashboardid, name=name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DashboardAPIApi->edit_dashboard: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **userid** | **str**|  | [optional] 
 **interfacekey** | **str**|  | [optional] 
 **dashboardid** | **str**|  | [optional] 
 **name** | **str**|  | [optional] 

### Return type

[**DashboardapiEditDashboardResponse**](DashboardapiEditDashboardResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_dashboards**
> DashboardapiGetDashboardsResponse get_dashboards(userid=userid, interfacekey=interfacekey)

Returns a dictionary of all dashbaord containing their id and name

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DashboardAPIApi()
userid = 'userid_example' # str |  (optional)
interfacekey = 'interfacekey_example' # str |  (optional)

try:
    # Returns a dictionary of all dashbaord containing their id and name
    api_response = api_instance.get_dashboards(userid=userid, interfacekey=interfacekey)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DashboardAPIApi->get_dashboards: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **userid** | **str**|  | [optional] 
 **interfacekey** | **str**|  | [optional] 

### Return type

[**DashboardapiGetDashboardsResponse**](DashboardapiGetDashboardsResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_widgets**
> DashboardapiGetWidgetsResponse get_widgets(userid=userid, interfacekey=interfacekey, dashboardid=dashboardid)

Returns all widgets registered on the dashboard

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DashboardAPIApi()
userid = 'userid_example' # str |  (optional)
interfacekey = 'interfacekey_example' # str |  (optional)
dashboardid = 'dashboardid_example' # str |  (optional)

try:
    # Returns all widgets registered on the dashboard
    api_response = api_instance.get_widgets(userid=userid, interfacekey=interfacekey, dashboardid=dashboardid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DashboardAPIApi->get_widgets: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **userid** | **str**|  | [optional] 
 **interfacekey** | **str**|  | [optional] 
 **dashboardid** | **str**|  | [optional] 

### Return type

[**DashboardapiGetWidgetsResponse**](DashboardapiGetWidgetsResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **move_widget**
> DashboardapiMoveWidgetResponse move_widget(userid=userid, interfacekey=interfacekey, dashboardid=dashboardid, widgetid=widgetid, x=x, y=y, z=z, width=width, height=height)

Moves a widget around

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DashboardAPIApi()
userid = 'userid_example' # str |  (optional)
interfacekey = 'interfacekey_example' # str |  (optional)
dashboardid = 'dashboardid_example' # str |  (optional)
widgetid = 'widgetid_example' # str |  (optional)
x = 56 # int |  (optional)
y = 56 # int |  (optional)
z = 56 # int |  (optional)
width = 56 # int |  (optional)
height = 56 # int |  (optional)

try:
    # Moves a widget around
    api_response = api_instance.move_widget(userid=userid, interfacekey=interfacekey, dashboardid=dashboardid, widgetid=widgetid, x=x, y=y, z=z, width=width, height=height)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DashboardAPIApi->move_widget: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **userid** | **str**|  | [optional] 
 **interfacekey** | **str**|  | [optional] 
 **dashboardid** | **str**|  | [optional] 
 **widgetid** | **str**|  | [optional] 
 **x** | **int**|  | [optional] 
 **y** | **int**|  | [optional] 
 **z** | **int**|  | [optional] 
 **width** | **int**|  | [optional] 
 **height** | **int**|  | [optional] 

### Return type

[**DashboardapiMoveWidgetResponse**](DashboardapiMoveWidgetResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **setup_widget**
> DashboardapiSetupWidgetResponse setup_widget(userid=userid, interfacekey=interfacekey, dashboardid=dashboardid, widgetid=widgetid, specs=specs)

Setup a widget its properties

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DashboardAPIApi()
userid = 'userid_example' # str |  (optional)
interfacekey = 'interfacekey_example' # str |  (optional)
dashboardid = 'dashboardid_example' # str |  (optional)
widgetid = 'widgetid_example' # str |  (optional)
specs = NULL # object |  (optional)

try:
    # Setup a widget its properties
    api_response = api_instance.setup_widget(userid=userid, interfacekey=interfacekey, dashboardid=dashboardid, widgetid=widgetid, specs=specs)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DashboardAPIApi->setup_widget: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **userid** | **str**|  | [optional] 
 **interfacekey** | **str**|  | [optional] 
 **dashboardid** | **str**|  | [optional] 
 **widgetid** | **str**|  | [optional] 
 **specs** | [**object**](.md)|  | [optional] 

### Return type

[**DashboardapiSetupWidgetResponse**](DashboardapiSetupWidgetResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

