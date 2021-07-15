import click
import logging
import json
import os
import requests

logger = logging.getLogger(__name__)


def read_metadata_json(source: str) -> dict:
    """Collect a dict from a local or remote json source.

    Enables the flexible use of json metadata files in CLI commands.

    Args:
        source (str): Path or url to a .json file

    Returns:
        dict: The contents of the json file converted to a dictionary
    """
    if os.path.isfile(source):
        with open(source) as f:
            data = json.load(f)
    else:
        metadata_response = requests.get(source)
        data = metadata_response.json()

    return data


def create_package_command(cli):
    """Creates the package command line utility."""
    @cli.group(
        "package",
        short_help=("Commands for working with package"),
    )
    def package():
        pass

    @package.command(
        "create-collection",
        short_help="Creates a STAC collection",
    )
    @click.option(
        "-d",
        "--destination",
        required=True,
        help="The output directory for the STAC json",
    )
    def create_collection_command(destination: str):
        """Creates a STAC Collection

        Args:
            destination (str): A placeholder to use click and demonstrate arguments
        """
        assert destination

        raise NotImplementedError(
            "The create-collection command has not been developed")

    @package.command("create-item", short_help="Create a STAC item")
    def create_item_command():
        """Creates a STAC Item
        """
        raise NotImplementedError(
            "The create-item command has not been developed")

    return package
