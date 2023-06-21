import re
from typing import Dict, List, Optional

from rest_framework import serializers


class OptionDto:
    offset: Optional[int]
    limit: Optional[int]
    sort_order_attribute: Optional[List[str]]
    sort_order_ascending: Optional[bool]
    filters: Optional[Dict]
    pagination: Optional[int]

    class Serializer(serializers.Serializer):
        offset = serializers.IntegerField(required=False)
        limit = serializers.IntegerField(required=False)
        sort_order_attribute = serializers.ListField(
            child=serializers.CharField(), required=False)
        sort_order_ascending = serializers.BooleanField(required=False)
        filters = serializers.DictField(required=False)
        pagination = serializers.IntegerField(required=False)

    def __init__(self,
                 offset: Optional[int] = None,
                 limit: Optional[int] = None,
                 sort_order_attribute: Optional[List[str]] = None,
                 sort_order_ascending: Optional[bool] = None,
                 filters: Optional[Dict] = None,
                 pagination: Optional[int] = None):

        self.offset = offset
        self.limit = limit
        self.sort_order_attribute = sort_order_attribute
        self.sort_order_ascending = sort_order_ascending
        self.filters = filters
        self.pagination = pagination
