
import json
import re
from typing import List

from django.core.exceptions import BadRequest
from django.core.handlers.wsgi import WSGIRequest
from django.db.models.query import QuerySet

from post_list.dto.option_dto import OptionDto


class BaseRepository:
    def __init__(self) -> None:
        self.comma_delimiter = re.compile(r"[,]")
        self.option_split_pattern = re.compile(r"[><=]+")
        self.filter_extension_mapping = {
            ">=": "__gte",
            "<=": "__lte",
            ">": "__gt",
            "<": "__lt",
            "=": "__icontains"
        }
        self.display_page = 5

    def create_options(self, request: WSGIRequest) -> OptionDto:
        try:
            offset = int(request.query_params.get("offset", "0"))
            limit = int(request.query_params.get("limit", "100000"))
            sort_order_attribute = request.query_params.get(
                "sort_order_attribute", [])
            sort_order_ascending = json.loads(request.query_params.get(
                "sort_order_ascending", "true"))
            filters = request.query_params.get("filters",
                                               {})
            pagination = int(request.query_params.get("pagination", "-1"))

            if sort_order_ascending:
                attribute_prefix = ""
            else:
                attribute_prefix = "-"

            if sort_order_attribute:
                attribute_list = []
                attribute_parts = self.comma_delimiter.split(
                    sort_order_attribute)
                for attribute in attribute_parts:
                    attribute = f"{attribute_prefix}{attribute}"
                    attribute_list.append(attribute)

                sort_order_attribute = attribute_list

            if filters:
                filter_dict = {}
                filter_parts = self.comma_delimiter.split(filters)
                for filter_part in filter_parts:
                    components = self.option_split_pattern.split(
                        filter_part)
                    if len(components) != 2:
                        raise BadRequest(
                            f"Filter component {filter_part} is not supported"
                        )

                    delimiter = self.option_split_pattern.findall(filter_part)[
                        0]
                    extension = self.filter_extension_mapping.get(
                        delimiter, None)
                    if extension is None:
                        raise BadRequest(
                            f"Filter extension {extension} is not supported"
                        )

                    attribute = components[0] + extension
                    filter_dict[attribute] = components[1]

                filters = filter_dict

            select_options = OptionDto(
                offset,
                limit,
                sort_order_attribute,
                sort_order_ascending,
                filters,
                pagination
            )
            return select_options

        except Exception as e:
            raise BadRequest(
                f"Cannot validate options: {e}"
            )

    def filter_options(
        self,
        items: QuerySet,
        options: OptionDto
    ) -> QuerySet:
        try:
            if options.filters:
                items = items.filter(**options.filters)
            if len(options.sort_order_attribute) > 0:
                items = items.order_by(*options.sort_order_attribute)

            items = items[options.offset: options.offset + options.limit]

            if options.pagination >= 0:
                start_position = options.pagination * self.display_page
                items = items[start_position: start_position +
                              self.display_page]

            return items
        except Exception as e:
            raise BadRequest(
                f"Cannot apply options: {e}"
            )

    def get_request_data(self, request: WSGIRequest):
        try:
            data = request.data.dict()

            return data
        except Exception as e:
            raise BadRequest(
                f"Cannot get request data: {e}"
            )
