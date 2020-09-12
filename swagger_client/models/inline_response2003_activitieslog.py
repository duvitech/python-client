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


class InlineResponse2003Activitieslog(object):
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
        'date_time': 'str',
        'value': 'int'
    }

    attribute_map = {
        'date_time': 'dateTime',
        'value': 'value'
    }

    def __init__(self, date_time=None, value=None):  # noqa: E501
        """InlineResponse2003Activitieslog - a model defined in Swagger"""  # noqa: E501

        self._date_time = None
        self._value = None
        self.discriminator = None

        if date_time is not None:
            self.date_time = date_time
        if value is not None:
            self.value = value

    @property
    def date_time(self):
        """Gets the date_time of this InlineResponse2003Activitieslog.  # noqa: E501


        :return: The date_time of this InlineResponse2003Activitieslog.  # noqa: E501
        :rtype: str
        """
        return self._date_time

    @date_time.setter
    def date_time(self, date_time):
        """Sets the date_time of this InlineResponse2003Activitieslog.


        :param date_time: The date_time of this InlineResponse2003Activitieslog.  # noqa: E501
        :type: str
        """

        self._date_time = date_time

    @property
    def value(self):
        """Gets the value of this InlineResponse2003Activitieslog.  # noqa: E501


        :return: The value of this InlineResponse2003Activitieslog.  # noqa: E501
        :rtype: int
        """
        return self._value

    @value.setter
    def value(self, value):
        """Sets the value of this InlineResponse2003Activitieslog.


        :param value: The value of this InlineResponse2003Activitieslog.  # noqa: E501
        :type: int
        """

        self._value = value

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
        if issubclass(InlineResponse2003Activitieslog, dict):
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
        if not isinstance(other, InlineResponse2003Activitieslog):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
