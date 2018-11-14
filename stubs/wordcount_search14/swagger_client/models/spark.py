# coding: utf-8

"""
    wordcount_search14

    Apps that count the number of specific characters  # noqa: E501

    OpenAPI spec version: 0.0.1
    Contact: ghwlchlaks@naver.com
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six


class Spark(object):
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
        'email': 'str',
        'data': 'str',
        'target': 'str',
        'user': 'str',
        'app': 'str'
    }

    attribute_map = {
        'email': 'email',
        'data': 'data',
        'target': 'target',
        'user': 'user',
        'app': 'APP'
    }

    def __init__(self, email=None, data=None, target=None, user=None, app=None):  # noqa: E501
        """Spark - a model defined in Swagger"""  # noqa: E501

        self._email = None
        self._data = None
        self._target = None
        self._user = None
        self._app = None
        self.discriminator = None

        self.email = email
        self.data = data
        self.target = target
        self.user = user
        self.app = app

    @property
    def email(self):
        """Gets the email of this Spark.  # noqa: E501


        :return: The email of this Spark.  # noqa: E501
        :rtype: str
        """
        return self._email

    @email.setter
    def email(self, email):
        """Sets the email of this Spark.


        :param email: The email of this Spark.  # noqa: E501
        :type: str
        """
        if email is None:
            raise ValueError("Invalid value for `email`, must not be `None`")  # noqa: E501

        self._email = email

    @property
    def data(self):
        """Gets the data of this Spark.  # noqa: E501


        :return: The data of this Spark.  # noqa: E501
        :rtype: str
        """
        return self._data

    @data.setter
    def data(self, data):
        """Sets the data of this Spark.


        :param data: The data of this Spark.  # noqa: E501
        :type: str
        """
        if data is None:
            raise ValueError("Invalid value for `data`, must not be `None`")  # noqa: E501

        self._data = data

    @property
    def target(self):
        """Gets the target of this Spark.  # noqa: E501


        :return: The target of this Spark.  # noqa: E501
        :rtype: str
        """
        return self._target

    @target.setter
    def target(self, target):
        """Sets the target of this Spark.


        :param target: The target of this Spark.  # noqa: E501
        :type: str
        """
        if target is None:
            raise ValueError("Invalid value for `target`, must not be `None`")  # noqa: E501

        self._target = target

    @property
    def user(self):
        """Gets the user of this Spark.  # noqa: E501


        :return: The user of this Spark.  # noqa: E501
        :rtype: str
        """
        return self._user

    @user.setter
    def user(self, user):
        """Sets the user of this Spark.


        :param user: The user of this Spark.  # noqa: E501
        :type: str
        """
        if user is None:
            raise ValueError("Invalid value for `user`, must not be `None`")  # noqa: E501

        self._user = user

    @property
    def app(self):
        """Gets the app of this Spark.  # noqa: E501


        :return: The app of this Spark.  # noqa: E501
        :rtype: str
        """
        return self._app

    @app.setter
    def app(self, app):
        """Sets the app of this Spark.


        :param app: The app of this Spark.  # noqa: E501
        :type: str
        """
        if app is None:
            raise ValueError("Invalid value for `app`, must not be `None`")  # noqa: E501

        self._app = app

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

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, Spark):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
