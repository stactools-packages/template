from datetime import datetime
import logging

from pystac import Collection, Item

logger = logging.getLogger(__name__)


def create_collection() -> Collection:
    """Create a STAC Collection

    Returns:
        Collection: STAC Collection object
    """
    # This function should include logic to extract all relevant metadata from
    # an asset describing the STAC collection and/or metadata coded into an
    # accompanying constants.py file

    # See https://pystac.readthedocs.io/en/latest/api.html#collection for requirements

    raise NotImplementedError()


def create_item() -> Item:
    """Create a STAC Item

    Returns:
        Item: STAC Item object
    """
    # This function should include logic to extract all relevant metadata from an
    # asset, metadata asset, and/or a constants.py file

    # See https://pystac.readthedocs.io/en/latest/api.html#item for requirements
    
    raise NotImplementedError()
