from datetime import datetime, timezone

from pystac import (
    Collection,
    Extent,
    Item,
    SpatialExtent,
    TemporalExtent,
)

import stactools.core.create


def create_collection() -> Collection:
    """Creates a STAC Collection.

    This function should create a collection for this dataset. See `the STAC
    specification
    <https://github.com/radiantearth/stac-spec/blob/master/collection-spec/collection-spec.md>`_
    for information about collection fields, and
    `Collection<https://pystac.readthedocs.io/en/latest/api.html#collection>`_
    for information about the PySTAC class.

    Returns:
        Collection: STAC Collection object
    """
    extent = Extent(
        SpatialExtent([[-180.0, 90.0, 180.0, -90.0]]),
        TemporalExtent([[datetime.now(tz=timezone.utc), None]]),
    )

    collection = Collection(
        id="example-collection",
        title="Example collection",
        description="An example collection",
        extent=extent,
        extra_fields={"custom_attribute": "foo"},
    )
    return collection


def create_item(asset_href: str) -> Item:
    """Creates a STAC item from a raster asset.

    This example function uses :py:func:`stactools.core.utils.create_item` to
    generate an example item.  Datasets should customize the item with
    dataset-specific information, e.g.  extracted from metadata files.

    See `the STAC specification
    <https://github.com/radiantearth/stac-spec/blob/master/item-spec/item-spec.md>`_
    for information about an item's fields, and
    `Item<https://pystac.readthedocs.io/en/latest/api/pystac.html#pystac.Item>`_ for
    information on the PySTAC class.

    This function should be updated to take all hrefs needed to build the item.
    It is an anti-pattern to assume that related files (e.g. metadata) are in
    the same directory as the primary file.

    Args:
        asset_href (str): The HREF pointing to an asset associated with the item

    Returns:
        Item: STAC Item object
    """
    item = stactools.core.create.item(asset_href)
    item.id = "example-item"
    item.properties["custom_attribute"] = "foo"
    return item
