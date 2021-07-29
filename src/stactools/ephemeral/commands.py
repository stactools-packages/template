import click
import logging

from stactools.ephemeral import stac

logger = logging.getLogger(__name__)


def create_ephemeralcmd_command(cli):
    """Creates the stactools-ephemeral command line utility."""
    @cli.group(
        "ephemeralcmd",
        short_help=("Commands for working with stactools-ephemeral"),
    )
    def ephemeralcmd():
        pass

    @ephemeralcmd.command(
        "create-collection",
        short_help="Creates a STAC collection",
    )
    @click.argument("destination")
    def create_collection_command(destination: str):
        """Creates a STAC Collection

        Args:
            destination (str): An HREF for the Collection JSON
        """
        collection = stac.create_collection()

        collection.set_self_href(destination)

        collection.save_object()

        return None

    @ephemeralcmd.command("create-item", short_help="Create a STAC item")
    @click.argument("source")
    @click.argument("destination")
    def create_item_command(source: str, destination: str):
        """Creates a STAC Item

        Args:
            source (str): HREF of the Asset associated with the Item
            destination (str): An HREF for the STAC Collection
        """
        item = stac.create_item(source)

        item.save_object(dest_href=destination)

        return None

    return ephemeralcmd
