"""
Verified Source dlt Pipeline Template

This template provides a skeleton for using dlt verified sources.
Verified sources are pre-built, tested connectors for popular platforms.

Setup:
1. Run: dlt init <source_name> <destination_name>
   Example: dlt init salesforce bigquery
2. Configure credentials in .dlt/secrets.toml
3. Modify this file to customize resource selection and behavior
"""

import dlt

# TODO: Import the verified source
# This import will be available after running: dlt init <source_name> <destination>
# Example imports:
# from salesforce import salesforce_source
# from github import github_source
# from stripe import stripe_source


def load_all_resources() -> None:
    """
    Load all resources from the verified source.
    """

    # TODO: Replace with your verified source name
    source = verified_source()

    pipeline = dlt.pipeline(
        pipeline_name="verified_pipeline",  # Unique pipeline name
        destination="duckdb",                # Options: duckdb, bigquery, snowflake, etc.
        dataset_name="verified_data"         # Dataset/schema name in destination
    )

    # Load all resources from the source
    load_info = pipeline.run(source)
    print(load_info)


def load_selected_resources() -> None:
    """
    Load only specific resources from the verified source.
    """

    # TODO: Replace with your verified source name
    source = verified_source()

    pipeline = dlt.pipeline(
        pipeline_name="verified_pipeline",
        destination="duckdb",
        dataset_name="verified_data"
    )

    # Load only specific resources
    # TODO: Replace with actual resource names from your verified source
    load_info = pipeline.run(
        source.with_resources("resource1", "resource2", "resource3")
    )
    print(load_info)


def load_with_customization() -> None:
    """
    Load resources with customized behavior (incremental, write disposition, etc.).
    """

    # TODO: Replace with your verified source name
    source = verified_source()

    # Customize specific resources
    # Example: Configure incremental loading
    source.resources["resource_name"].apply_hints(
        write_disposition="merge",
        primary_key="id",
        incremental=dlt.sources.incremental("updated_at")
    )

    # Example: Change write disposition for a resource
    source.resources["another_resource"].apply_hints(
        write_disposition="replace"
    )

    pipeline = dlt.pipeline(
        pipeline_name="verified_pipeline",
        destination="duckdb",
        dataset_name="verified_data"
    )

    load_info = pipeline.run(source)
    print(load_info)


if __name__ == "__main__":
    # Choose which loading strategy to use:

    # Option 1: Load all resources
    load_all_resources()

    # Option 2: Load only specific resources
    # load_selected_resources()

    # Option 3: Load with customization
    # load_with_customization()
