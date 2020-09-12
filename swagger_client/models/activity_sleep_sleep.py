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


class ActivitySleepSleep(object):
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
        'date_of_sleep': 'str',
        'duration': 'float',
        'efficiency': 'float',
        'is_main_sleep': 'bool',
        'levels': 'ActivitySleepLevels1',
        'log_id': 'float',
        'minutes_after_wakeup': 'float',
        'minutes_asleep': 'float',
        'minutes_awake': 'float',
        'minutes_to_fall_asleep': 'float',
        'start_time': 'str',
        'time_in_bed': 'float',
        'type': 'str'
    }

    attribute_map = {
        'date_of_sleep': 'dateOfSleep',
        'duration': 'duration',
        'efficiency': 'efficiency',
        'is_main_sleep': 'isMainSleep',
        'levels': 'levels',
        'log_id': 'logId',
        'minutes_after_wakeup': 'minutesAfterWakeup',
        'minutes_asleep': 'minutesAsleep',
        'minutes_awake': 'minutesAwake',
        'minutes_to_fall_asleep': 'minutesToFallAsleep',
        'start_time': 'startTime',
        'time_in_bed': 'timeInBed',
        'type': 'type'
    }

    def __init__(self, date_of_sleep=None, duration=None, efficiency=None, is_main_sleep=None, levels=None, log_id=None, minutes_after_wakeup=None, minutes_asleep=None, minutes_awake=None, minutes_to_fall_asleep=None, start_time=None, time_in_bed=None, type=None):  # noqa: E501
        """ActivitySleepSleep - a model defined in Swagger"""  # noqa: E501

        self._date_of_sleep = None
        self._duration = None
        self._efficiency = None
        self._is_main_sleep = None
        self._levels = None
        self._log_id = None
        self._minutes_after_wakeup = None
        self._minutes_asleep = None
        self._minutes_awake = None
        self._minutes_to_fall_asleep = None
        self._start_time = None
        self._time_in_bed = None
        self._type = None
        self.discriminator = None

        if date_of_sleep is not None:
            self.date_of_sleep = date_of_sleep
        if duration is not None:
            self.duration = duration
        if efficiency is not None:
            self.efficiency = efficiency
        if is_main_sleep is not None:
            self.is_main_sleep = is_main_sleep
        if levels is not None:
            self.levels = levels
        if log_id is not None:
            self.log_id = log_id
        if minutes_after_wakeup is not None:
            self.minutes_after_wakeup = minutes_after_wakeup
        if minutes_asleep is not None:
            self.minutes_asleep = minutes_asleep
        if minutes_awake is not None:
            self.minutes_awake = minutes_awake
        if minutes_to_fall_asleep is not None:
            self.minutes_to_fall_asleep = minutes_to_fall_asleep
        if start_time is not None:
            self.start_time = start_time
        if time_in_bed is not None:
            self.time_in_bed = time_in_bed
        if type is not None:
            self.type = type

    @property
    def date_of_sleep(self):
        """Gets the date_of_sleep of this ActivitySleepSleep.  # noqa: E501


        :return: The date_of_sleep of this ActivitySleepSleep.  # noqa: E501
        :rtype: str
        """
        return self._date_of_sleep

    @date_of_sleep.setter
    def date_of_sleep(self, date_of_sleep):
        """Sets the date_of_sleep of this ActivitySleepSleep.


        :param date_of_sleep: The date_of_sleep of this ActivitySleepSleep.  # noqa: E501
        :type: str
        """

        self._date_of_sleep = date_of_sleep

    @property
    def duration(self):
        """Gets the duration of this ActivitySleepSleep.  # noqa: E501


        :return: The duration of this ActivitySleepSleep.  # noqa: E501
        :rtype: float
        """
        return self._duration

    @duration.setter
    def duration(self, duration):
        """Sets the duration of this ActivitySleepSleep.


        :param duration: The duration of this ActivitySleepSleep.  # noqa: E501
        :type: float
        """

        self._duration = duration

    @property
    def efficiency(self):
        """Gets the efficiency of this ActivitySleepSleep.  # noqa: E501


        :return: The efficiency of this ActivitySleepSleep.  # noqa: E501
        :rtype: float
        """
        return self._efficiency

    @efficiency.setter
    def efficiency(self, efficiency):
        """Sets the efficiency of this ActivitySleepSleep.


        :param efficiency: The efficiency of this ActivitySleepSleep.  # noqa: E501
        :type: float
        """

        self._efficiency = efficiency

    @property
    def is_main_sleep(self):
        """Gets the is_main_sleep of this ActivitySleepSleep.  # noqa: E501


        :return: The is_main_sleep of this ActivitySleepSleep.  # noqa: E501
        :rtype: bool
        """
        return self._is_main_sleep

    @is_main_sleep.setter
    def is_main_sleep(self, is_main_sleep):
        """Sets the is_main_sleep of this ActivitySleepSleep.


        :param is_main_sleep: The is_main_sleep of this ActivitySleepSleep.  # noqa: E501
        :type: bool
        """

        self._is_main_sleep = is_main_sleep

    @property
    def levels(self):
        """Gets the levels of this ActivitySleepSleep.  # noqa: E501


        :return: The levels of this ActivitySleepSleep.  # noqa: E501
        :rtype: ActivitySleepLevels1
        """
        return self._levels

    @levels.setter
    def levels(self, levels):
        """Sets the levels of this ActivitySleepSleep.


        :param levels: The levels of this ActivitySleepSleep.  # noqa: E501
        :type: ActivitySleepLevels1
        """

        self._levels = levels

    @property
    def log_id(self):
        """Gets the log_id of this ActivitySleepSleep.  # noqa: E501


        :return: The log_id of this ActivitySleepSleep.  # noqa: E501
        :rtype: float
        """
        return self._log_id

    @log_id.setter
    def log_id(self, log_id):
        """Sets the log_id of this ActivitySleepSleep.


        :param log_id: The log_id of this ActivitySleepSleep.  # noqa: E501
        :type: float
        """

        self._log_id = log_id

    @property
    def minutes_after_wakeup(self):
        """Gets the minutes_after_wakeup of this ActivitySleepSleep.  # noqa: E501


        :return: The minutes_after_wakeup of this ActivitySleepSleep.  # noqa: E501
        :rtype: float
        """
        return self._minutes_after_wakeup

    @minutes_after_wakeup.setter
    def minutes_after_wakeup(self, minutes_after_wakeup):
        """Sets the minutes_after_wakeup of this ActivitySleepSleep.


        :param minutes_after_wakeup: The minutes_after_wakeup of this ActivitySleepSleep.  # noqa: E501
        :type: float
        """

        self._minutes_after_wakeup = minutes_after_wakeup

    @property
    def minutes_asleep(self):
        """Gets the minutes_asleep of this ActivitySleepSleep.  # noqa: E501


        :return: The minutes_asleep of this ActivitySleepSleep.  # noqa: E501
        :rtype: float
        """
        return self._minutes_asleep

    @minutes_asleep.setter
    def minutes_asleep(self, minutes_asleep):
        """Sets the minutes_asleep of this ActivitySleepSleep.


        :param minutes_asleep: The minutes_asleep of this ActivitySleepSleep.  # noqa: E501
        :type: float
        """

        self._minutes_asleep = minutes_asleep

    @property
    def minutes_awake(self):
        """Gets the minutes_awake of this ActivitySleepSleep.  # noqa: E501


        :return: The minutes_awake of this ActivitySleepSleep.  # noqa: E501
        :rtype: float
        """
        return self._minutes_awake

    @minutes_awake.setter
    def minutes_awake(self, minutes_awake):
        """Sets the minutes_awake of this ActivitySleepSleep.


        :param minutes_awake: The minutes_awake of this ActivitySleepSleep.  # noqa: E501
        :type: float
        """

        self._minutes_awake = minutes_awake

    @property
    def minutes_to_fall_asleep(self):
        """Gets the minutes_to_fall_asleep of this ActivitySleepSleep.  # noqa: E501


        :return: The minutes_to_fall_asleep of this ActivitySleepSleep.  # noqa: E501
        :rtype: float
        """
        return self._minutes_to_fall_asleep

    @minutes_to_fall_asleep.setter
    def minutes_to_fall_asleep(self, minutes_to_fall_asleep):
        """Sets the minutes_to_fall_asleep of this ActivitySleepSleep.


        :param minutes_to_fall_asleep: The minutes_to_fall_asleep of this ActivitySleepSleep.  # noqa: E501
        :type: float
        """

        self._minutes_to_fall_asleep = minutes_to_fall_asleep

    @property
    def start_time(self):
        """Gets the start_time of this ActivitySleepSleep.  # noqa: E501


        :return: The start_time of this ActivitySleepSleep.  # noqa: E501
        :rtype: str
        """
        return self._start_time

    @start_time.setter
    def start_time(self, start_time):
        """Sets the start_time of this ActivitySleepSleep.


        :param start_time: The start_time of this ActivitySleepSleep.  # noqa: E501
        :type: str
        """

        self._start_time = start_time

    @property
    def time_in_bed(self):
        """Gets the time_in_bed of this ActivitySleepSleep.  # noqa: E501


        :return: The time_in_bed of this ActivitySleepSleep.  # noqa: E501
        :rtype: float
        """
        return self._time_in_bed

    @time_in_bed.setter
    def time_in_bed(self, time_in_bed):
        """Sets the time_in_bed of this ActivitySleepSleep.


        :param time_in_bed: The time_in_bed of this ActivitySleepSleep.  # noqa: E501
        :type: float
        """

        self._time_in_bed = time_in_bed

    @property
    def type(self):
        """Gets the type of this ActivitySleepSleep.  # noqa: E501


        :return: The type of this ActivitySleepSleep.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this ActivitySleepSleep.


        :param type: The type of this ActivitySleepSleep.  # noqa: E501
        :type: str
        """

        self._type = type

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
        if issubclass(ActivitySleepSleep, dict):
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
        if not isinstance(other, ActivitySleepSleep):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
