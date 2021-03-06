# coding: utf-8

"""
    Curaegis Egress API

    Curaegis egress data API  # noqa: E501

    OpenAPI spec version: v1
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six


class ActivitySleep(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'sleep': 'list[ActivitySleepSleep1]',
        'summary': 'ActivitySleepSummary1'
    }

    attribute_map = {
        'sleep': 'sleep',
        'summary': 'summary'
    }

    def __init__(self, sleep=None, summary=None):  # noqa: E501
        """ActivitySleep - a model defined in Swagger"""  # noqa: E501

        self._sleep = None
        self._summary = None
        self.discriminator = None

        self.sleep = sleep
        if summary is not None:
            self.summary = summary

    @property
    def sleep(self):
        """Gets the sleep of this ActivitySleep.  # noqa: E501


        :return: The sleep of this ActivitySleep.  # noqa: E501
        :rtype: list[ActivitySleepSleep1]
        """
        return self._sleep

    @sleep.setter
    def sleep(self, sleep):
        """Sets the sleep of this ActivitySleep.


        :param sleep: The sleep of this ActivitySleep.  # noqa: E501
        :type: list[ActivitySleepSleep1]
        """
        if sleep is None:
            raise ValueError("Invalid value for `sleep`, must not be `None`")  # noqa: E501

        self._sleep = sleep

    @property
    def summary(self):
        """Gets the summary of this ActivitySleep.  # noqa: E501


        :return: The summary of this ActivitySleep.  # noqa: E501
        :rtype: ActivitySleepSummary1
        """
        return self._summary

    @summary.setter
    def summary(self, summary):
        """Sets the summary of this ActivitySleep.


        :param summary: The summary of this ActivitySleep.  # noqa: E501
        :type: ActivitySleepSummary1
        """

        self._summary = summary

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value
        if issubclass(ActivitySleep, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, ActivitySleep):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
