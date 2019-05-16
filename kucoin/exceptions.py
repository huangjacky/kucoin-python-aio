# coding=utf-8
# HTTP error status codes
# Code	Meaning
# 400	Bad Request -- Invalid request format
# 401	Unauthorized -- Invalid API Key
# 403	Forbidden -- The requested is hidden for administrators only.
# 404	Not Found -- The specified resource could not be found.
# 405	Method Not Allowed -- You tried to access the resource with an invalid method.
# 429	Too Many Requests -- Exceeded the access frequency
# 500	Internal Server Error -- We had a problem with our server. Try again later.
# 503	Service Unavailable -- We're temporarily offline for maintenance. Please try again later.
# System error codes
# Code	Meaning
# 400001	Any of KC-API-KEY, KC-API-SIGN, KC-API-TIMESTAMP, KC-API-PASSPHRASE is missing in your request header
# 400002	KC-API-TIMESTAMP Invalid -- Time differs from server time by more than 5 seconds
# 400003	KC-API-KEY not exists
# 400004	KC-API-PASSPHRASE error
# 400005	Signature error -- Please check your signature
# 400006	The requested ip address is not in the api whitelist
# 400007	Access Denied -- Your api key does not have sufficient permissions to access the uri
# 404000	Url Not Found -- The request resource could not be found
# 400100	Parameter Error -- You tried to access the resource with invalid parameters
# 411100	User are frozen -- User are frozen, please contact us via support center.
# 500000	Internal Server Error -- We had a problem with our server. Try again later.


class KucoinAPIException(Exception):
    """Exception class to handle general API Exceptions

        `code` values

        `message` format

    """

    def __init__(self, response, code, message):
        self.code = code
        self.message = message
        self.status_code = response.status
        self.response = response
        self.request = getattr(response, 'request', None)

    def __str__(self):  # pragma: no cover
        return 'KucoinAPIException {}: {}'.format(self.code, self.message)


class KucoinRequestException(Exception):
    def __init__(self, message):
        self.message = message

    def __str__(self):
        return 'KucoinRequestException: {}'.format(self.message)


class MarketOrderException(Exception):
    def __init__(self, message):
        self.message = message

    def __str__(self):
        return 'MarketOrderException: {}'.format(self.message)


class LimitOrderException(Exception):
    def __init__(self, message):
        self.message = message

    def __str__(self):
        return 'LimitOrderException: {}'.format(self.message)
