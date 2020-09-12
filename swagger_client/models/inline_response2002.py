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


class InlineResponse2002(object):
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
        'tenantid': 'float',
        'userid': 'float',
        'curascore': 'float',
        'lastsyncdate': 'str',
        'timetox': 'str'
    }

    attribute_map = {
        'tenantid': 'tenantid',
        'userid': 'userid',
        'curascore': 'curascore',
        'lastsyncdate': 'lastsyncdate',
        'timetox': 'timetox'
    }

    def __init__(self, tenantid=None, userid=None, curascore=None, lastsyncdate=None, timetox=None):  # noqa: E501
        """InlineResponse2002 - a model defined in Swagger"""  # noqa: E501

        self._tenantid = None
        self._userid = None
        self._curascore = None
        self._lastsyncdate = None
        self._timetox = None
        self.discriminator = None

        self.tenantid = tenantid
        self.userid = userid
        self.curascore = curascore
        self.lastsyncdate = lastsyncdate
        self.timetox = timetox

    @property
    def tenantid(self):
        """Gets the tenantid of this InlineResponse2002.  # noqa: E501


        :return: The tenantid of this InlineResponse2002.  # noqa: E501
        :rtype: float
        """
        return self._tenantid

    @tenantid.setter
    def tenantid(self, tenantid):
        """Sets the tenantid of this InlineResponse2002.


        :param tenantid: The tenantid of this InlineResponse2002.  # noqa: E501
        :type: float
        """
        if tenantid is None:
            raise ValueError("Invalid value for `tenantid`, must not be `None`")  # noqa: E501

        self._tenantid = tenantid

    @property
    def userid(self):
        """Gets the userid of this InlineResponse2002.  # noqa: E501


        :return: The userid of this InlineResponse2002.  # noqa: E501
        :rtype: float
        """
        return self._userid

    @userid.setter
    def userid(self, userid):
        """Sets the userid of this InlineResponse2002.


        :param userid: The userid of this InlineResponse2002.  # noqa: E501
        :type: float
        """
        if userid is None:
            raise ValueError("Invalid value for `userid`, must not be `None`")  # noqa: E501

        self._userid = userid

    @property
    def curascore(self):
        """Gets the curascore of this InlineResponse2002.  # noqa: E501


        :return: The curascore of this InlineResponse2002.  # noqa: E501
        :rtype: float
        """
        return self._curascore

    @curascore.setter
    def curascore(self, curascore):
        """Sets the curascore of this InlineResponse2002.


        :param curascore: The curascore of this InlineResponse2002.  # noqa: E501
        :type: float
        """
        if curascore is None:
            raise ValueError("Invalid value for `curascore`, must not be `None`")  # noqa: E501

        self._curascore = curascore

    @property
    def lastsyncdate(self):
        """Gets the lastsyncdate of this InlineResponse2002.  # noqa: E501


        :return: The lastsyncdate of this InlineResponse2002.  # noqa: E501
        :rtype: str
        """
        return self._lastsyncdate

    @lastsyncdate.setter
    def lastsyncdate(self, lastsyncdate):
        """Sets the lastsyncdate of this InlineResponse2002.


        :param lastsyncdate: The lastsyncdate of this InlineResponse2002.  # noqa: E501
        :type: str
        """
        if lastsyncdate is None:
            raise ValueError("Invalid value for `lastsyncdate`, must not be `None`")  # noqa: E501

        self._lastsyncdate = lastsyncdate

    @property
    def timetox(self):
        """Gets the timetox of this InlineResponse2002.  # noqa: E501


        :return: The timetox of this InlineResponse2002.  # noqa: E501
        :rtype: str
        """
        return self._timetox

    @timetox.setter
    def timetox(self, timetox):
        """Sets the timetox of this InlineResponse2002.


        :param timetox: The timetox of this InlineResponse2002.  # noqa: E501
        :type: str
        """
        if timetox is None:
            raise ValueError("Invalid value for `timetox`, must not be `None`")  # noqa: E501

        self._timetox = timetox

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
        if issubclass(InlineResponse2002, dict):
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
        if not isinstance(other, InlineResponse2002):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
