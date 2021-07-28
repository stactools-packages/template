import click
import logging

from pystac import Item, Collection

logger = logging.getLogger(__name__)


def create_ephemeralcmd_command(cli):
    """Creates the ephemeral-package command line utility."""

    @cli.group(
        "ephemeralcmd", short_help=("Commands for working with ephemeral-package"),
    )
    def ephemeralcmd():
        pass

    @ephemeralcmd.command(
        "create-collection", short_help="Creates a STAC collection",
    )
    @click.argument("destination")
    def create_collection_command(destination: str) -> Collection:
        """Creates a STAC Collection

        Args:
            destination (str): A placeholder to use click and demonstrate arguments
        """
        assert destination

        raise NotImplementedError(
            "The create-collection command has not been developed"
        )

    @ephemeralcmd.command("create-item", short_help="Create a STAC item")
    @click.argument("source")
    @click.argument("destination")
    def create_item_command(source: str, destination: str) -> Item:
        """Creates a STAC Item
        """
        assert source, destination

        raise NotImplementedError("The create-item command has not been developed")

    return ephemeralcmd
