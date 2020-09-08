# -*- coding: utf-8 -*-
import time
# REACHESTIMATE_URL = "https://graph.facebook.com/v8.0/act_{}/delivery_estimate" #delivery_estimate
# GRAPH_SEARCH_URL = "https://graph.facebook.com/v8.0/search"
# TARGETING_SEARCH_URL = "https://graph.facebook.com/v8.0/act_{}/targetingsearch"
SAVE_EMPTY = True
MAX_NUMBER_TRY = 10
REQUESTS_TIMEOUT = 60
INITIAL_TRY_SLEEP_TIME = 300
API_UNKOWN_ERROR_CODE_1 = 1
API_UNKOWN_ERROR_CODE_2 = 2
INVALID_PARAMETER_ERROR = 100
ZIPCODE_INVALID_SUBCODE_ERROR = None
FEW_USERS_IN_CUSTOM_LOCATIONS_SUBCODE_ERROR = 1885036
NUMBER_OF_REQUESTS_PER_BUCKET = 100
INGORE_INVALID_ZIP_CODES = True
MOCK_RESPONSE_FIELD = "mockResponse"
DEFAULT_DUMB_TARGETING = {'geo_locations': {'regions': [{'key': '3843'}], 'location_types': ['home']}, 'genders': [0], }
TOKENS = []
INPUT_AGE_RANGE_FIELD = "ages_ranges"
INPUT_GEOLOCATION_FIELD = "geo_locations"
INPUT_GEOLOCATION_LOCATION_TYPE_FIELD = "location_types"
DEFAULT_GEOLOCATION_LOCATION_TYPE_FIELD = ["home"]
INPUT_GENDER_FIELD = "genders"
INPUT_INTEREST_FIELD = "interests"
GROUP_ID_FIELD = "group_id"
INPUT_BEHAVIOR_FIELD = "behavior"
INPUT_SCHOLARITY_FIELD = "scholarities"
INPUT_LANGUAGE_FIELD = "languages"
INPUT_FAMILYSTATUS_FIELD = "family_statuses"
INPUT_RELATIONSHIPSTATUS_FIELD = "relationship_statuses"
TARGETING_FIELD = "targeting"
TARGETING_SPEC_FIELD = "targeting_spec"
RESPONSE_FIELD = "response"
DAU_AUDIENCE_FIELD = "dau_audience"
MAU_AUDIENCE_FIELD = "mau_audience"
ALLFIELDS_FIELD = "all_fields"
INPUT_NAME_FIELD = "name"
PERFORM_AND_BETWEEN_GROUPS_INPUT_FIELD = "perform_AND_between_groups"
MIN_AGE = "min"
MAX_AGE = "max"
DETAILS_FIELD_FROM_FACEBOOK_TARGETING_SEARCH = ["id", "name", "type", "description", "dau_audience_size", "mau_audience_size", "path","key","supports_city","supports_region"]
API_INTEREST_FIELD = "interests"
API_BEHAVIOR_FIELD = "behaviors"
API_HOUSEHOLD_COMPOSITION_FIELD = "household_composition"

INPUT_HOUSEHOLD_COMPOSITION_FIELD = "household_composition"
INPUT_CITIZENSHIP_BEHAVIOR_SUBFIELD = "citizenship"
INPUT_ACCESS_DEVICES_BEHAVIOR_SUBFIELD = "access_device"
API_SCHOLARITY_FIELD = "education_statuses"
API_FAMILYSTATUS_FIELD = "family_statuses"
API_RELATIONSHIPSTATUS_FIELD = "relationship_statuses"
API_LANGUAGES_FIELD = "locales"
API_GENDER_FIELD = "genders"
API_MIN_AGE_FIELD = "age_min"
API_MAX_AGE_FIELD = "age_max"
API_GEOLOCATION_FIELD = "geo_locations"
API_PUBLISHER_PLATFORMS_FIELD = "publisher_platforms"
PUBLISHER_PLATFORM_DEFAULT = ["facebook"]

INPUT_FIELDS_TO_COMBINE = [
    INPUT_INTEREST_FIELD,
    INPUT_AGE_RANGE_FIELD,
    INPUT_GENDER_FIELD,
    INPUT_BEHAVIOR_FIELD,
    INPUT_SCHOLARITY_FIELD,
    INPUT_LANGUAGE_FIELD,
    INPUT_FAMILYSTATUS_FIELD,
    INPUT_RELATIONSHIPSTATUS_FIELD,
    INPUT_GEOLOCATION_FIELD,
    INPUT_HOUSEHOLD_COMPOSITION_FIELD
]

DATAFRAME_COLUMNS = [INPUT_NAME_FIELD] + INPUT_FIELDS_TO_COMBINE + [ALLFIELDS_FIELD, TARGETING_FIELD, RESPONSE_FIELD, DAU_AUDIENCE_FIELD, MAU_AUDIENCE_FIELD ]

ALLOWED_FIELDS_IN_INPUT = DATAFRAME_COLUMNS + [PERFORM_AND_BETWEEN_GROUPS_INPUT_FIELD] + [API_PUBLISHER_PLATFORMS_FIELD]

ADVANCE_TARGETING_FIELDS_TYPE_ARRAY_IDS = [
    INPUT_INTEREST_FIELD,
    INPUT_BEHAVIOR_FIELD,
    INPUT_CITIZENSHIP_BEHAVIOR_SUBFIELD,
    INPUT_ACCESS_DEVICES_BEHAVIOR_SUBFIELD,
    INPUT_FAMILYSTATUS_FIELD,
    INPUT_HOUSEHOLD_COMPOSITION_FIELD
]

ADVANCE_TARGETING_FIELDS_TYPE_ARRAY_INTEGER = [
    INPUT_SCHOLARITY_FIELD, INPUT_RELATIONSHIPSTATUS_FIELD
]
INPUT_TO_API_FIELD_NAME = {
    INPUT_GENDER_FIELD : API_GENDER_FIELD,
    INPUT_INTEREST_FIELD: API_INTEREST_FIELD,
    INPUT_BEHAVIOR_FIELD: API_BEHAVIOR_FIELD,
    INPUT_CITIZENSHIP_BEHAVIOR_SUBFIELD: API_BEHAVIOR_FIELD,
    INPUT_HOUSEHOLD_COMPOSITION_FIELD: API_HOUSEHOLD_COMPOSITION_FIELD,
    INPUT_ACCESS_DEVICES_BEHAVIOR_SUBFIELD: API_BEHAVIOR_FIELD,
    INPUT_SCHOLARITY_FIELD: API_SCHOLARITY_FIELD,
    INPUT_FAMILYSTATUS_FIELD: API_FAMILYSTATUS_FIELD,
    INPUT_RELATIONSHIPSTATUS_FIELD: API_RELATIONSHIPSTATUS_FIELD
}

ADVANCE_TARGETING_FIELDS = [
    INPUT_INTEREST_FIELD, INPUT_BEHAVIOR_FIELD, INPUT_SCHOLARITY_FIELD, INPUT_FAMILYSTATUS_FIELD, INPUT_BEHAVIOR_FIELD
]

FAKE_DATA_RESPONSE_CONTENT = '{"mockResponse":true, "data":[{"bid_estimate":{"min_bid":0,"median_bid":0,"max_bid":0},"daily_outcomes_curve":[{"spend":0,"reach":0,"impressions":0,"actions":0}],"estimate_dau":0,"estimate_mau":0,"estimate_ready":true}]}'