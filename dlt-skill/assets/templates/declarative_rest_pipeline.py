"""
Declarative REST API dlt Pipeline Template

This template provides a skeleton for creating a pipeline using the declarative REST API source.
Use this for REST APIs with standard patterns (authentication, pagination, etc.).
"""

import dlt
from dlt.sources.rest_api import rest_api_source


# Define the REST API configuration
config = {
    "client": {
        "base_url": "https://api.example.com/v1/",

        # Optional: Authentication
        # "auth": {
        #     "type": "bearer",
        #     "token": dlt.secrets["api_token"]
        # },

        # Optional: Custom headers
        # "headers": {
        #     "User-Agent": "MyApp/1.0"
        # },

        # Optional: Default paginator for all resources
        # "paginator": {
        #     "type": "page_number",
        #     "page_param": "page",
        #     "page_size": 100
        # }
    },

    # Optional: Default settings for all resources
    "resource_defaults": {
        "write_disposition": "append",
        "primary_key": "id",
    },

    # Define API resources/endpoints
    "resources": [
        # Simple endpoint (string notation)
        # "users",

        # Detailed endpoint (dictionary notation)
        {
            "name": "resource_name",
            "endpoint": {
                "path": "endpoint_path",

                # Optional: Query parameters
                # "params": {
                #     "status": "active",
                #     "limit": 100
                # },

                # Optional: Data selector (JSONPath)
                # "data_selector": "data.results",

                # Optional: Pagination override
                # "paginator": {
                #     "type": "offset",
                #     "limit": 100,
                #     "offset_param": "offset",
                #     "limit_param": "limit"
                # }
            },
            "write_disposition": "merge",
            "primary_key": "id",

            # Optional: Incremental loading
            # "incremental": {
            #     "cursor_path": "updated_at",
            #     "initial_value": "2024-01-01T00:00:00Z"
            # }
        },

        # Example: Parent-child relationship
        # {
        #     "name": "child_resource",
        #     "endpoint": {
        #         "path": "parents/{parent_id}/children"
        #     },
        #     "include_from_parent": ["id", "name"]
        # }
    ]
}


def run_pipeline() -> None:
    """
    Execute the REST API pipeline.
    """

    # Create the REST API source from config
    source = rest_api_source(config)

    # Configure the pipeline
    pipeline = dlt.pipeline(
        pipeline_name="rest_api_pipeline",  # Unique pipeline name
        destination="duckdb",                # Options: duckdb, bigquery, snowflake, etc.
        dataset_name="rest_api_data"         # Dataset/schema name in destination
    )

    # Run the pipeline
    load_info = pipeline.run(source)

    # Print load information
    print(load_info)


if __name__ == "__main__":
    run_pipeline()


# Authentication Examples
# ----------------------

# Bearer Token:
# "auth": {
#     "type": "bearer",
#     "token": dlt.secrets["api_token"]
# }

# Basic Auth:
# "auth": {
#     "type": "http_basic",
#     "username": dlt.secrets["username"],
#     "password": dlt.secrets["password"]
# }

# API Key in Header:
# "auth": {
#     "type": "api_key",
#     "name": "X-API-Key",
#     "api_key": dlt.secrets["api_key"],
#     "location": "header"
# }

# API Key in Query:
# "auth": {
#     "type": "api_key",
#     "name": "api_key",
#     "api_key": dlt.secrets["api_key"],
#     "location": "query"
# }


# Pagination Examples
# -------------------

# JSON Link (next URL in response):
# "paginator": {
#     "type": "json_link",
#     "next_url_path": "pagination.next"
# }

# Header Link (GitHub-style):
# "paginator": {
#     "type": "header_link"
# }

# Offset:
# "paginator": {
#     "type": "offset",
#     "limit": 100,
#     "offset_param": "offset",
#     "limit_param": "limit"
# }

# Page Number:
# "paginator": {
#     "type": "page_number",
#     "page_param": "page",
#     "page_size": 100
# }

# Cursor:
# "paginator": {
#     "type": "cursor",
#     "cursor_path": "next_cursor",
#     "cursor_param": "cursor"
# }


# Incremental Loading Example
# ---------------------------

# Add to endpoint configuration:
# "endpoint": {
#     "path": "items",
#     "params": {
#         "updated_since": "{incremental.start_value}"
#     }
# },
# "incremental": {
#     "cursor_path": "updated_at",
#     "initial_value": "2024-01-01T00:00:00Z"
# },
# "write_disposition": "merge",
# "primary_key": "id"
