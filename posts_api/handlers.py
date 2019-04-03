from rest_framework import status
from rest_framework.exceptions import ErrorDetail
from rest_framework.response import Response
from rest_framework.views import exception_handler

EXCEPTIONS_DICT = {
    "ValidationError": {
        "text": "Wrong data!",
        "status_code": status.HTTP_400_BAD_REQUEST,
    },
    "ParseError": {
        "text": "Wrong data!",
        "status_code": status.HTTP_400_BAD_REQUEST,
    },
    "DoesNotExist": {
        "text": "Item matching your query does not exist!",
        "status_code": status.HTTP_404_NOT_FOUND,
    },
    "NotAuthenticated": {
        "text": "Authenticate please!",
        "status_code": status.HTTP_401_UNAUTHORIZED,
    },
    "MethodNotAllowed": {
        "text": "Method Not Allowed!",
        "status_code": status.HTTP_405_METHOD_NOT_ALLOWED,
    },
    "ValueError": {
        "text": "Wrong data type!",
        "status_code": status.HTTP_400_BAD_REQUEST,
    },
}


def handle_exceptions(exc, context):
    exc_type = type(exc).__name__
    response = exception_handler(exc, context)
    if hasattr(exc, "detail"):
        errors_list = list(exc.detail.values()) \
            if type(exc.detail) == dict else False
        if hasattr(exc.detail, "values") and errors_list:
            message_text = [
                error if type(error) == ErrorDetail else error[0]
                for error in errors_list
            ]
        else:
            message_text = exc.detail
        response.data = {"message": message_text, "type": exc_type}
    elif exc_type in EXCEPTIONS_DICT.keys():
        response = Response(
            {"message": EXCEPTIONS_DICT[exc_type]["text"], "type": exc_type},
            status=EXCEPTIONS_DICT[exc_type]["status_code"])
    elif hasattr(exc, "args"):
        message_text = [error for error in exc.args]
        response = Response(
            {"message": message_text, "type": exc_type},
            status=status.HTTP_400_BAD_REQUEST)


    else:
        response = Response({"message": exc_type, "type": exc_type},
                            status=status.HTTP_400_BAD_REQUEST)
    return response


def get_error_response(data=None):
    dict_error = None
    error_instance = None
    error_message = None
    if type(data) == dict:
        dict_error = data.get("type")
        error_instance = EXCEPTIONS_DICT.get(dict_error)
        default_value = error_instance.get("text") if error_instance else None
        error_message = data.get("message", default_value)
    if dict_error and error_instance:
        response_data = {
            "error": {
                "type": dict_error,
                "messages": error_message
            }
        }
    else:
        message = list(data.values())[0][0] \
                if type(list(data.values())[0]) in (list, tuple) \
                else list(data.values())[0]
        data = list(data.keys())[0] \
            if type(data).__name__ == "ReturnDict" else data
        data = data if type(data) == str else data.get("type", data)
        response_data = {
            "error": {
                "type": data,
                "message": message
            }
        }
    return response_data
