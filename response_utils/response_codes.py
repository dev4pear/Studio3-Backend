from enum import Enum


class ResponseCodes(Enum):
    NEW_REGISTRATION = "NEW_REGISTRATION"
    LOGIN_SUCCESS = "LOGIN_SUCCESS"
    NOT_LOGGED_IN = "NOT_LOGGED_IN"
    USER_PROFILE_UPDATE_SUCCESS = "USER_PROFILE_UPDATE_SUCCESS"
    UPLOAD_SUCCESS = "UPLOAD_SUCCESS"
    OVERWRITE_SUCCESS = "OVERWRITE_SUCCESS"
    ASSET_UPDATE_SUCCESS = "ASSET_UPDATE_SUCCESS"
    LIST_SUCCESS = "LIST_SUCCESS"
    LIST_TEMPLATES_SUCCESS = "LIST_TEMPLATES_SUCCESS"
    DOWNLOAD_JSON_SUCCESS = "DOWNLOAD_JSON_SUCCESS"
    DELETE_ASSET_SUCCESS = "DELETE_ASSET_SUCCESS"
    DUPLICATE_SUCCESS = "DUPLICATE_SUCCESS"