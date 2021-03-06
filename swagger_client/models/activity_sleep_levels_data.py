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


class ActivitySleepLevelsData(object):
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
        '_datetime': 'str',
        'level': 'str',
        'seconds': 'int'
    }

    attribute_map = {
        '_datetime': 'datetime',
        'level': 'level',
        'seconds': 'seconds'
    }

    def __init__(self, _datetime=None, level=None, seconds=None):  # noqa: E501
        """ActivitySleepLevelsData - a model defined in Swagger"""  # noqa: E501

        self.__datetime = None
        self._level = None
        self._seconds = None
        self.discriminator = None

        if _datetime is not None:
            self._datetime = _datetime
        if level is not None:
            self.level = level
        if seconds is not None:
            self.seconds = seconds

    @property
    def _datetime(self):
        """Gets the _datetime of this ActivitySleepLevelsData.  # noqa: E501


        :return: The _datetime of this ActivitySleepLevelsData.  # noqa: E501
        :rtype: str
        """
        return self.__datetime

    @_datetime.setter
    def _datetime(self, _datetime):
        """Sets the _datetime of this ActivitySleepLevelsData.


        :param _datetime: The _datetime of this ActivitySleepLevelsData.  # noqa: E501
        :type: str
        """

        self.__datetime = _datetime

    @property
    def level(self):
        """Gets the level of this ActivitySleepLevelsData.  # noqa: E501


        :return: The level of this ActivitySleepLevelsData.  # noqa: E501
        :rtype: str
        """
        return self._level

    @level.setter
    def level(self, level):
        """Sets the level of this ActivitySleepLevelsData.


        :param level: The level of this ActivitySleepLevelsData.  # noqa: E501
        :type: str
        """

        self._level = level

    @property
    def seconds(self):
        """Gets the seconds of this ActivitySleepLevelsData.  # noqa: E501


        :return: The seconds of this ActivitySleepLevelsData.  # noqa: E501
        :rtype: int
        """
        return self._seconds

    @seconds.setter
    def seconds(self, seconds):
        """Sets the seconds of this ActivitySleepLevelsData.


        :param seconds: The seconds of this ActivitySleepLevelsData.  # noqa: E501
        :type: int
        """

        self._seconds = seconds

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
        if issubclass(ActivitySleepLevelsData, dict):
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
        if not isinstance(other, ActivitySleepLevelsData):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
