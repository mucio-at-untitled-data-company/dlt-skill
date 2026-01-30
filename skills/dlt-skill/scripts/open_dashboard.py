#!/usr/bin/env python3
"""
Open dlt Pipeline Dashboard

This script opens the dlt pipeline dashboard for inspection and debugging.
It shows pipeline runs, schemas, data, and allows querying loaded data.

Usage:
    python open_dashboard.py <pipeline_name>
    python open_dashboard.py  # Will prompt for pipeline name
"""

import sys
import subprocess
from pathlib import Path


def find_pipelines() -> list[str]:
    """
    Find available pipeline names in the .dlt/pipelines directory.

    Returns:
        List of pipeline names
    """
    pipelines_dir = Path(".dlt/pipelines")
    if not pipelines_dir.exists():
        return []

    return [p.name for p in pipelines_dir.iterdir() if p.is_dir()]


def open_dashboard(pipeline_name: str) -> None:
    """
    Open the dlt dashboard for the specified pipeline.

    Args:
        pipeline_name: Name of the pipeline to inspect
    """
    try:
        print(f"Opening dashboard for pipeline: {pipeline_name}")
        subprocess.run(
            ["dlt", "pipeline", pipeline_name, "show"],
            check=True
        )
    except subprocess.CalledProcessError as e:
        print(f"Error opening dashboard: {e}", file=sys.stderr)
        print("\nTroubleshooting:")
        print("1. Ensure the pipeline has been run at least once")
        print("2. Check that the pipeline name is correct")
        print("3. Verify dlt is installed: pip install dlt")
        sys.exit(1)
    except FileNotFoundError:
        print("Error: dlt command not found", file=sys.stderr)
        print("Install dlt: pip install dlt")
        sys.exit(1)


def main() -> None:
    """Main entry point."""

    # Get pipeline name from command line or prompt
    if len(sys.argv) > 1:
        pipeline_name = sys.argv[1]
    else:
        # Try to find available pipelines
        pipelines = find_pipelines()

        if not pipelines:
            print("No pipelines found in .dlt/pipelines/")
            print("\nUsage: python open_dashboard.py <pipeline_name>")
            sys.exit(1)

        if len(pipelines) == 1:
            pipeline_name = pipelines[0]
            print(f"Found pipeline: {pipeline_name}")
        else:
            print("Available pipelines:")
            for i, name in enumerate(pipelines, 1):
                print(f"  {i}. {name}")

            try:
                choice = int(input("\nSelect pipeline number: "))
                pipeline_name = pipelines[choice - 1]
            except (ValueError, IndexError, KeyboardInterrupt):
                print("\nInvalid selection")
                sys.exit(1)

    # Open the dashboard
    open_dashboard(pipeline_name)


if __name__ == "__main__":
    main()
