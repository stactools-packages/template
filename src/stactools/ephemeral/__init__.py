import stactools.core
from stactools.cli.registry import Registry

from stactools.ephemeral.stac import create_collection, create_item

__all__ = ["create_collection", "create_item"]

stactools.core.use_fsspec()


def register_plugin(registry: Registry) -> None:
    from stactools.ephemeral import commands

    registry.register_subcommand(commands.create_ephemeralcmd_command)


__version__ = "0.1.0"
