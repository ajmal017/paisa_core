from enum import Enum
from paisa_core.base import EnumDirectValueMeta


class OrderFor(Enum, metaclass=EnumDirectValueMeta):
    PLACE = "P"
    MODIFY = "M"
    CANCEL = "C"


class OrderType(Enum, metaclass=EnumDirectValueMeta):
    BUY = "BUY"
    SELL = "SELL"


# Exchanges type enum
class Exchange(Enum, metaclass=EnumDirectValueMeta):
    NSE = "N"
    BSE = "B"
    MCX = "M"


# Exchange type of the order
class ExchangeSegment(Enum, metaclass=EnumDirectValueMeta):
    CASH = "C"
    DERIVATIVE = "D"
    CURRENCY = "U"


class OrderValidity(Enum, metaclass=EnumDirectValueMeta):
    DAY = 0
    GTD = 1
    GTC = 2
    IOC = 3
    EOS = 4
    FOK = 6


API_ENDPOINT = "https://Openapi.5paisa.com"


def append_with_endpoint(route):
    return API_ENDPOINT + route


# Base config will only hold request_code and URL endpoint.
BASE_CONFIG = {
    "api": {
        "order_request": {
            "request_code": "5POrdReq",
            "url": append_with_endpoint("/VendorsAPI/Service1.svc/V1/OrderRequest")
        },
        "order_status": {
            "request_code": "5POrdStatus",
            "url": append_with_endpoint("/VendorsAPI/Service1.svc/OrderStatus")
        },
        "user_login": {
            "request_code": "5PLoginV2",
            "url": append_with_endpoint("/VendorsAPI/Service1.svc/V2/LoginRequestMobileNewbyEmail")
        },
        "user_margin": {
            "request_code": "5PMarginV3",
            "url": append_with_endpoint("/VendorsAPI/Service1.svc/V3/Margin")
        },
        "user_order_book": {
            "request_code": "5POrdBkV2",
            "url": append_with_endpoint("/VendorsAPI/Service1.svc/V2/OrderBook")
        },
        "user_positions": {
            "request_code": "5PNPNWV1",
            "url": append_with_endpoint("/VendorsAPI/Service1.svc/V1/NetPositionNetWise")
        },
        "user_holdings": {
            "request_code": "5PHoldingV2",
            "url": append_with_endpoint("/VendorsAPI/Service1.svc/V2/Holding")
        }
    }
}

# It is salt value. list of integer but it"ll be converted to byte
SALT = [83, 71, 26, 58, 54, 35, 22, 11, 83, 71, 26, 58, 54, 35, 22, 11]

# default headers
default_headers = {
    "Content-Type": "application/json",
    "Accept": "*/*",
    "Cache-Control": "no-cache",
    "Host": "Openapi.5paisa.com",
    "accept-encoding": "gzip, deflate",
    "content-length": "816",
    "Connection": "keep-alive",
    "cache-control": "no-cache"
}
