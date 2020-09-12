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


class ActivitiesIntradayLogsActivitiesintraday(object):
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
        'dataset': 'list[list[object]]',
        'dataset_interval': 'int',
        'dataset_type': 'str'
    }

    attribute_map = {
        'dataset': 'dataset',
        'dataset_interval': 'datasetInterval',
        'dataset_type': 'datasetType'
    }

    def __init__(self, dataset=None, dataset_interval=None, dataset_type=None):  # noqa: E501
        """ActivitiesIntradayLogsActivitiesintraday - a model defined in Swagger"""  # noqa: E501

        self._dataset = None
        self._dataset_interval = None
        self._dataset_type = None
        self.discriminator = None

        self.dataset = dataset
        self.dataset_interval = dataset_interval
        self.dataset_type = dataset_type

    @property
    def dataset(self):
        """Gets the dataset of this ActivitiesIntradayLogsActivitiesintraday.  # noqa: E501


        :return: The dataset of this ActivitiesIntradayLogsActivitiesintraday.  # noqa: E501
        :rtype: list[list[object]]
        """
        return self._dataset

    @dataset.setter
    def dataset(self, dataset):
        """Sets the dataset of this ActivitiesIntradayLogsActivitiesintraday.


        :param dataset: The dataset of this ActivitiesIntradayLogsActivitiesintraday.  # noqa: E501
        :type: list[list[object]]
        """
        if dataset is None:
            raise ValueError("Invalid value for `dataset`, must not be `None`")  # noqa: E501

        self._dataset = dataset

    @property
    def dataset_interval(self):
        """Gets the dataset_interval of this ActivitiesIntradayLogsActivitiesintraday.  # noqa: E501


        :return: The dataset_interval of this ActivitiesIntradayLogsActivitiesintraday.  # noqa: E501
        :rtype: int
        """
        return self._dataset_interval

    @dataset_interval.setter
    def dataset_interval(self, dataset_interval):
        """Sets the dataset_interval of this ActivitiesIntradayLogsActivitiesintraday.


        :param dataset_interval: The dataset_interval of this ActivitiesIntradayLogsActivitiesintraday.  # noqa: E501
        :type: int
        """
        if dataset_interval is None:
            raise ValueError("Invalid value for `dataset_interval`, must not be `None`")  # noqa: E501

        self._dataset_interval = dataset_interval

    @property
    def dataset_type(self):
        """Gets the dataset_type of this ActivitiesIntradayLogsActivitiesintraday.  # noqa: E501


        :return: The dataset_type of this ActivitiesIntradayLogsActivitiesintraday.  # noqa: E501
        :rtype: str
        """
        return self._dataset_type

    @dataset_type.setter
    def dataset_type(self, dataset_type):
        """Sets the dataset_type of this ActivitiesIntradayLogsActivitiesintraday.


        :param dataset_type: The dataset_type of this ActivitiesIntradayLogsActivitiesintraday.  # noqa: E501
        :type: str
        """
        if dataset_type is None:
            raise ValueError("Invalid value for `dataset_type`, must not be `None`")  # noqa: E501

        self._dataset_type = dataset_type

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
        if issubclass(ActivitiesIntradayLogsActivitiesintraday, dict):
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
        if not isinstance(other, ActivitiesIntradayLogsActivitiesintraday):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other