"""
Custom Python dlt Pipeline Template

This template provides a skeleton for creating a custom dlt pipeline using Python code.
Use this when you need custom logic or are using Python packages to access data.
"""

import dlt
from typing import Iterator, Any


@dlt.source
def custom_source(
    # Add configuration parameters here
    # Use dlt.secrets.value for sensitive values from .dlt/secrets.toml
    # Use dlt.config.value for non-sensitive values from .dlt/config.toml
    api_key: str = dlt.secrets.value,
    base_url: str = dlt.config.value,
):
    """
    Define your custom source.

    Args:
        api_key: API authentication key
        base_url: Base URL for the API

    Returns:
        One or more dlt resources
    """

    # Return one or more resources
    return my_resource()


@dlt.resource(
    write_disposition="append",  # Options: "append", "replace", "merge"
    # primary_key="id",          # Uncomment for merge operations
    # table_name="custom_table"  # Optional: override table name
)
def my_resource() -> Iterator[dict[str, Any]]:
    """
    Define your resource that extracts data.

    Yields:
        Data items as dictionaries
    """

    # TODO: Implement data extraction logic
    # Example: Fetch data from API, database, file, etc.

    # Yield data (pages recommended over individual items for performance)
    data = []  # Replace with actual data fetching
    yield data


# Example: Resource with incremental loading
@dlt.resource(
    write_disposition="merge",
    primary_key="id"
)
def incremental_resource(
    updated_at=dlt.sources.incremental(
        "updated_at",
        initial_value="2024-01-01T00:00:00Z"
    )
) -> Iterator[dict[str, Any]]:
    """
    Resource with incremental loading based on a cursor field.

    Args:
        updated_at: Incremental cursor tracking the updated_at field

    Yields:
        Data items updated since the last run
    """

    # TODO: Fetch data modified since updated_at.last_value
    # Example: data = fetch_data(since=updated_at.last_value)

    data = []  # Replace with actual data fetching
    yield data


if __name__ == "__main__":
    # Configure the pipeline
    pipeline = dlt.pipeline(
        pipeline_name="custom_pipeline",  # Unique pipeline name
        destination="duckdb",              # Options: duckdb, bigquery, snowflake, etc.
        dataset_name="custom_data"         # Dataset/schema name in destination
    )

    # Run the pipeline
    load_info = pipeline.run(custom_source())

    # Print load information
    print(load_info)

    # Optional: Show pipeline in dashboard
    # pipeline.show()
