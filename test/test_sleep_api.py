# coding: utf-8

"""
    Curaegis Egress API

    Curaegis egress data API  # noqa: E501

    OpenAPI spec version: v1
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import unittest

import swagger_client
from swagger_client.api.sleep_api import SleepApi  # noqa: E501
from swagger_client.rest import ApiException


class TestSleepApi(unittest.TestCase):
    """SleepApi unit test stubs"""

    def setUp(self):
        self.api = swagger_client.api.sleep_api.SleepApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_sleep_log_get_by_id(self):
        """Test case for sleep_log_get_by_id

        """
        pass

    def test_sleep_log_get_range(self):
        """Test case for sleep_log_get_range

        """
        pass

    def test_sleep_log_get_timeseries(self):
        """Test case for sleep_log_get_timeseries

        """
        pass


if __name__ == '__main__':
    unittest.main()
