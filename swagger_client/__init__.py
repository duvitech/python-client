# coding: utf-8

# flake8: noqa

"""
    Curaegis Egress API

    Curaegis egress data API  # noqa: E501

    OpenAPI spec version: v1
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

# import apis into sdk package
from swagger_client.api.cura_score_api import CuraScoreApi
from swagger_client.api.devices_api import DevicesApi
from swagger_client.api.intraday_api import IntradayApi
from swagger_client.api.manager_api import ManagerApi
from swagger_client.api.resources_api import ResourcesApi
from swagger_client.api.sleep_api import SleepApi
from swagger_client.api.subscriptions_api import SubscriptionsApi
from swagger_client.api.summary_api import SummaryApi
from swagger_client.api.user_profile_api import UserProfileApi

# import ApiClient
from swagger_client.api_client import ApiClient
from swagger_client.configuration import Configuration
# import models into sdk package
from swagger_client.models.activities_intraday import ActivitiesIntraday
from swagger_client.models.activities_intraday_logs import ActivitiesIntradayLogs
from swagger_client.models.activities_intraday_logs_activitiesintraday import ActivitiesIntradayLogsActivitiesintraday
from swagger_client.models.activity_log import ActivityLog
from swagger_client.models.activity_log_activitieslog import ActivityLogActivitieslog
from swagger_client.models.activity_sleep import ActivitySleep
from swagger_client.models.activity_sleep_levels import ActivitySleepLevels
from swagger_client.models.activity_sleep_levels1 import ActivitySleepLevels1
from swagger_client.models.activity_sleep_levels1_data import ActivitySleepLevels1Data
from swagger_client.models.activity_sleep_levels1_summary import ActivitySleepLevels1Summary
from swagger_client.models.activity_sleep_levels1_summary_deep import ActivitySleepLevels1SummaryDeep
from swagger_client.models.activity_sleep_levels_data import ActivitySleepLevelsData
from swagger_client.models.activity_sleep_levels_summary import ActivitySleepLevelsSummary
from swagger_client.models.activity_sleep_levels_summary_deep import ActivitySleepLevelsSummaryDeep
from swagger_client.models.activity_sleep_sleep import ActivitySleepSleep
from swagger_client.models.activity_sleep_sleep1 import ActivitySleepSleep1
from swagger_client.models.activity_sleep_summary import ActivitySleepSummary
from swagger_client.models.activity_sleep_summary1 import ActivitySleepSummary1
from swagger_client.models.activity_summay import ActivitySummay
from swagger_client.models.activity_summay_activities import ActivitySummayActivities
from swagger_client.models.activity_summay_activities1 import ActivitySummayActivities1
from swagger_client.models.activity_summay_goals import ActivitySummayGoals
from swagger_client.models.activity_summay_goals1 import ActivitySummayGoals1
from swagger_client.models.activity_summay_summary import ActivitySummaySummary
from swagger_client.models.activity_summay_summary1 import ActivitySummaySummary1
from swagger_client.models.activity_summay_summary1_distances import ActivitySummaySummary1Distances
from swagger_client.models.activity_summay_summary1_heart_rate_zones import ActivitySummaySummary1HeartRateZones
from swagger_client.models.activity_summay_summary_distances import ActivitySummaySummaryDistances
from swagger_client.models.activity_summay_summary_heart_rate_zones import ActivitySummaySummaryHeartRateZones
from swagger_client.models.body import Body
from swagger_client.models.cura_score import CuraScore
from swagger_client.models.cura_score_ex import CuraScoreEx
from swagger_client.models.cura_score_values import CuraScoreValues
from swagger_client.models.cura_score_values1 import CuraScoreValues1
from swagger_client.models.dispatched_user import DispatchedUser
from swagger_client.models.error_model import ErrorModel
from swagger_client.models.error_model_error import ErrorModelError
from swagger_client.models.inline_response200 import InlineResponse200
from swagger_client.models.inline_response2001 import InlineResponse2001
from swagger_client.models.inline_response2002 import InlineResponse2002
from swagger_client.models.inline_response2003 import InlineResponse2003
from swagger_client.models.inline_response2003_activitieslog import InlineResponse2003Activitieslog
from swagger_client.models.inline_response_default import InlineResponseDefault
from swagger_client.models.inline_response_default_error import InlineResponseDefaultError
from swagger_client.models.intraday_logentry import IntradayLogentry
from swagger_client.models.new_device import NewDevice
from swagger_client.models.new_profile import NewProfile
from swagger_client.models.profile import Profile
from swagger_client.models.registration import Registration
from swagger_client.models.tenant_user import TenantUser
from swagger_client.models.user_profile import UserProfile
