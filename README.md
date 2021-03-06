# swagger-client
Curaegis egress data API

This Python package is automatically generated by the [Swagger Codegen](https://github.com/swagger-api/swagger-codegen) project:

- API version: v1
- Package version: 1.0.0
- Build package: io.swagger.codegen.languages.PythonClientCodegen

## Requirements.

Python 2.7 and 3.4+

## Installation & Usage
### pip install

If the python package is hosted on Github, you can install directly from Github

```sh
pip install git+https://github.com//.git
```
(you may need to run `pip` with root permission: `sudo pip install git+https://github.com//.git`)

Then import the package:
```python
import swagger_client 
```

### Setuptools

Install via [Setuptools](http://pypi.python.org/pypi/setuptools).

```sh
python setup.py install --user
```
(or `sudo python setup.py install` to install the package for all users)

Then import the package:
```python
import swagger_client
```

## Getting Started

Please follow the [installation procedure](#installation--usage) and then run the following:

```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: ApiKeyAuth
configuration = swagger_client.Configuration()
configuration.api_key['X-API-KEY'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-API-KEY'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.CuraScoreApi(swagger_client.ApiClient(configuration))
id = 'id_example' # str | id to filter by (optional)

try:
    api_response = api_instance.get_cura_by_id(id=id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CuraScoreApi->get_cura_by_id: %s\n" % e)

```

## Documentation for API Endpoints

All URIs are relative to *https://edgestream-egress.azurewebsites.net/curaegis/v1*

Class | Method | HTTP request | Description
------------ | ------------- | ------------- | -------------
*CuraScoreApi* | [**get_cura_by_id**](docs/CuraScoreApi.md#get_cura_by_id) | **GET** /curascore | 
*CuraScoreApi* | [**get_cura_ex_by_id**](docs/CuraScoreApi.md#get_cura_ex_by_id) | **GET** /curascoreex | 
*DevicesApi* | [**add_device_by_id**](docs/DevicesApi.md#add_device_by_id) | **POST** /register | 
*DevicesApi* | [**add_profile_by_id**](docs/DevicesApi.md#add_profile_by_id) | **POST** /profile | 
*DevicesApi* | [**get_device_list**](docs/DevicesApi.md#get_device_list) | **GET** /devices | 
*DevicesApi* | [**get_profile_by_id**](docs/DevicesApi.md#get_profile_by_id) | **GET** /profile | 
*IntradayApi* | [**intraday_get_by_default**](docs/IntradayApi.md#intraday_get_by_default) | **GET** /{id}/intraday/{resource}/date/{date} | 
*IntradayApi* | [**intraday_get_by_id**](docs/IntradayApi.md#intraday_get_by_id) | **GET** /{id}/intraday/{resource}/date/{date}/{detail}/{stime}/{etime} | 
*ManagerApi* | [**get_cura_by_users**](docs/ManagerApi.md#get_cura_by_users) | **POST** /dispatchedusers | 
*ResourcesApi* | [**resourcelog_get_by_date_range**](docs/ResourcesApi.md#resourcelog_get_by_date_range) | **GET** /{id}/activities/{resource}/range/{basedate}/{enddate} | 
*ResourcesApi* | [**resourcelog_get_by_id**](docs/ResourcesApi.md#resourcelog_get_by_id) | **GET** /{id}/activities/{resource}/date/{date}/{period} | 
*SleepApi* | [**sleep_log_get_by_id**](docs/SleepApi.md#sleep_log_get_by_id) | **GET** /{id}/sleep/{date} | 
*SleepApi* | [**sleep_log_get_range**](docs/SleepApi.md#sleep_log_get_range) | **GET** /{id}/sleep/{resource}/{date}/{period} | 
*SleepApi* | [**sleep_log_get_timeseries**](docs/SleepApi.md#sleep_log_get_timeseries) | **GET** /{id}/sleep/{resource}/range/{basedate}/{enddate} | 
*SubscriptionsApi* | [**add_subscription_by_id**](docs/SubscriptionsApi.md#add_subscription_by_id) | **POST** /{id}/subscription/{resource} | 
*SubscriptionsApi* | [**delete_subscription_by_id**](docs/SubscriptionsApi.md#delete_subscription_by_id) | **DELETE** /{id}/subscription/{resource} | 
*SubscriptionsApi* | [**get_subscribed_by_id**](docs/SubscriptionsApi.md#get_subscribed_by_id) | **GET** /{id}/subscription/{resource} | 
*SummaryApi* | [**activity_summary_get_by_id**](docs/SummaryApi.md#activity_summary_get_by_id) | **GET** /{id}/activities | 
*SummaryApi* | [**activity_summary_get_by_id_date**](docs/SummaryApi.md#activity_summary_get_by_id_date) | **GET** /{id}/activities/date/{date} | 
*UserProfileApi* | [**activity_profile_get_by_id**](docs/UserProfileApi.md#activity_profile_get_by_id) | **GET** /{id}/profile | 


## Documentation For Models

 - [ActivitiesIntraday](docs/ActivitiesIntraday.md)
 - [ActivitiesIntradayLogs](docs/ActivitiesIntradayLogs.md)
 - [ActivitiesIntradayLogsActivitiesintraday](docs/ActivitiesIntradayLogsActivitiesintraday.md)
 - [ActivityLog](docs/ActivityLog.md)
 - [ActivityLogActivitieslog](docs/ActivityLogActivitieslog.md)
 - [ActivitySleep](docs/ActivitySleep.md)
 - [ActivitySleepLevels](docs/ActivitySleepLevels.md)
 - [ActivitySleepLevels1](docs/ActivitySleepLevels1.md)
 - [ActivitySleepLevels1Data](docs/ActivitySleepLevels1Data.md)
 - [ActivitySleepLevels1Summary](docs/ActivitySleepLevels1Summary.md)
 - [ActivitySleepLevels1SummaryDeep](docs/ActivitySleepLevels1SummaryDeep.md)
 - [ActivitySleepLevelsData](docs/ActivitySleepLevelsData.md)
 - [ActivitySleepLevelsSummary](docs/ActivitySleepLevelsSummary.md)
 - [ActivitySleepLevelsSummaryDeep](docs/ActivitySleepLevelsSummaryDeep.md)
 - [ActivitySleepSleep](docs/ActivitySleepSleep.md)
 - [ActivitySleepSleep1](docs/ActivitySleepSleep1.md)
 - [ActivitySleepSummary](docs/ActivitySleepSummary.md)
 - [ActivitySleepSummary1](docs/ActivitySleepSummary1.md)
 - [ActivitySummay](docs/ActivitySummay.md)
 - [ActivitySummayActivities](docs/ActivitySummayActivities.md)
 - [ActivitySummayActivities1](docs/ActivitySummayActivities1.md)
 - [ActivitySummayGoals](docs/ActivitySummayGoals.md)
 - [ActivitySummayGoals1](docs/ActivitySummayGoals1.md)
 - [ActivitySummaySummary](docs/ActivitySummaySummary.md)
 - [ActivitySummaySummary1](docs/ActivitySummaySummary1.md)
 - [ActivitySummaySummary1Distances](docs/ActivitySummaySummary1Distances.md)
 - [ActivitySummaySummary1HeartRateZones](docs/ActivitySummaySummary1HeartRateZones.md)
 - [ActivitySummaySummaryDistances](docs/ActivitySummaySummaryDistances.md)
 - [ActivitySummaySummaryHeartRateZones](docs/ActivitySummaySummaryHeartRateZones.md)
 - [Body](docs/Body.md)
 - [CuraScore](docs/CuraScore.md)
 - [CuraScoreEx](docs/CuraScoreEx.md)
 - [CuraScoreValues](docs/CuraScoreValues.md)
 - [CuraScoreValues1](docs/CuraScoreValues1.md)
 - [DispatchedUser](docs/DispatchedUser.md)
 - [ErrorModel](docs/ErrorModel.md)
 - [ErrorModelError](docs/ErrorModelError.md)
 - [InlineResponse200](docs/InlineResponse200.md)
 - [InlineResponse2001](docs/InlineResponse2001.md)
 - [InlineResponse2002](docs/InlineResponse2002.md)
 - [InlineResponse2003](docs/InlineResponse2003.md)
 - [InlineResponse2003Activitieslog](docs/InlineResponse2003Activitieslog.md)
 - [InlineResponseDefault](docs/InlineResponseDefault.md)
 - [InlineResponseDefaultError](docs/InlineResponseDefaultError.md)
 - [IntradayLogentry](docs/IntradayLogentry.md)
 - [NewDevice](docs/NewDevice.md)
 - [NewProfile](docs/NewProfile.md)
 - [Profile](docs/Profile.md)
 - [Registration](docs/Registration.md)
 - [TenantUser](docs/TenantUser.md)
 - [UserProfile](docs/UserProfile.md)


## Documentation For Authorization


## ApiKeyAuth

- **Type**: API key
- **API key parameter name**: X-API-KEY
- **Location**: HTTP header


## Author



