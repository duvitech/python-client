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


class CuraScoreEx(object):
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
        'id': 'str',
        'start': 'str',
        'scores': 'list[float]'
    }

    attribute_map = {
        'id': 'id',
        'start': 'start',
        'scores': 'scores'
    }

    def __init__(self, id=None, start=None, scores=None):  # noqa: E501
        """CuraScoreEx - a model defined in Swagger"""  # noqa: E501

        self._id = None
        self._start = None
        self._scores = None
        self.discriminator = None

        self.id = id
        self.start = start
        self.scores = scores

    @property
    def id(self):
        """Gets the id of this CuraScoreEx.  # noqa: E501


        :return: The id of this CuraScoreEx.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this CuraScoreEx.


        :param id: The id of this CuraScoreEx.  # noqa: E501
        :type: str
        """
        if id is None:
            raise ValueError("Invalid value for `id`, must not be `None`")  # noqa: E501

        self._id = id

    @property
    def start(self):
        """Gets the start of this CuraScoreEx.  # noqa: E501


        :return: The start of this CuraScoreEx.  # noqa: E501
        :rtype: str
        """
        return self._start

    @start.setter
    def start(self, start):
        """Sets the start of this CuraScoreEx.


        :param start: The start of this CuraScoreEx.  # noqa: E501
        :type: str
        """
        if start is None:
            raise ValueError("Invalid value for `start`, must not be `None`")  # noqa: E501

        self._start = start

    @property
    def scores(self):
        """Gets the scores of this CuraScoreEx.  # noqa: E501


        :return: The scores of this CuraScoreEx.  # noqa: E501
        :rtype: list[float]
        """
        return self._scores

    @scores.setter
    def scores(self, scores):
        """Sets the scores of this CuraScoreEx.


        :param scores: The scores of this CuraScoreEx.  # noqa: E501
        :type: list[float]
        """
        if scores is None:
            raise ValueError("Invalid value for `scores`, must not be `None`")  # noqa: E501

        self._scores = scores

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
        if issubclass(CuraScoreEx, dict):
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
        if not isinstance(other, CuraScoreEx):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
