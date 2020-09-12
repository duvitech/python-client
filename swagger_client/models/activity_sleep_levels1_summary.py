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


class ActivitySleepLevels1Summary(object):
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
        'deep': 'ActivitySleepLevels1SummaryDeep',
        'light': 'ActivitySleepLevels1SummaryDeep',
        'rem': 'ActivitySleepLevels1SummaryDeep',
        'wake': 'ActivitySleepLevels1SummaryDeep'
    }

    attribute_map = {
        'deep': 'deep',
        'light': 'light',
        'rem': 'rem',
        'wake': 'wake'
    }

    def __init__(self, deep=None, light=None, rem=None, wake=None):  # noqa: E501
        """ActivitySleepLevels1Summary - a model defined in Swagger"""  # noqa: E501

        self._deep = None
        self._light = None
        self._rem = None
        self._wake = None
        self.discriminator = None

        if deep is not None:
            self.deep = deep
        if light is not None:
            self.light = light
        if rem is not None:
            self.rem = rem
        if wake is not None:
            self.wake = wake

    @property
    def deep(self):
        """Gets the deep of this ActivitySleepLevels1Summary.  # noqa: E501


        :return: The deep of this ActivitySleepLevels1Summary.  # noqa: E501
        :rtype: ActivitySleepLevels1SummaryDeep
        """
        return self._deep

    @deep.setter
    def deep(self, deep):
        """Sets the deep of this ActivitySleepLevels1Summary.


        :param deep: The deep of this ActivitySleepLevels1Summary.  # noqa: E501
        :type: ActivitySleepLevels1SummaryDeep
        """

        self._deep = deep

    @property
    def light(self):
        """Gets the light of this ActivitySleepLevels1Summary.  # noqa: E501


        :return: The light of this ActivitySleepLevels1Summary.  # noqa: E501
        :rtype: ActivitySleepLevels1SummaryDeep
        """
        return self._light

    @light.setter
    def light(self, light):
        """Sets the light of this ActivitySleepLevels1Summary.


        :param light: The light of this ActivitySleepLevels1Summary.  # noqa: E501
        :type: ActivitySleepLevels1SummaryDeep
        """

        self._light = light

    @property
    def rem(self):
        """Gets the rem of this ActivitySleepLevels1Summary.  # noqa: E501


        :return: The rem of this ActivitySleepLevels1Summary.  # noqa: E501
        :rtype: ActivitySleepLevels1SummaryDeep
        """
        return self._rem

    @rem.setter
    def rem(self, rem):
        """Sets the rem of this ActivitySleepLevels1Summary.


        :param rem: The rem of this ActivitySleepLevels1Summary.  # noqa: E501
        :type: ActivitySleepLevels1SummaryDeep
        """

        self._rem = rem

    @property
    def wake(self):
        """Gets the wake of this ActivitySleepLevels1Summary.  # noqa: E501


        :return: The wake of this ActivitySleepLevels1Summary.  # noqa: E501
        :rtype: ActivitySleepLevels1SummaryDeep
        """
        return self._wake

    @wake.setter
    def wake(self, wake):
        """Sets the wake of this ActivitySleepLevels1Summary.


        :param wake: The wake of this ActivitySleepLevels1Summary.  # noqa: E501
        :type: ActivitySleepLevels1SummaryDeep
        """

        self._wake = wake

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
        if issubclass(ActivitySleepLevels1Summary, dict):
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
        if not isinstance(other, ActivitySleepLevels1Summary):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
