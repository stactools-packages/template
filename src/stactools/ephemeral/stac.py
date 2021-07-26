from datetime import datetime
from typing import List
import logging

from shapely.geometry import Polygon
from pystac.extensions.projection import ProjectionExtension
from pystac import (
    CatalogType,
    Collection,
    Item,
    Asset,
    Extent,
    SpatialExtent,
    TemporalExtent,
    Link,
    Provider,
    MediaType,
)

logger = logging.getLogger(__name__)


# This includes a set of minimum requirements for the creation of a STAC Collection,
# and should be added to/modified as necessary to develop a dataset-specific package.
def create_collection(
    title: str,
    description: str,
    catalog_type: str,
    providers: List[Provider],
    license: str,
    license_link: Link,
    extent: list,
    start_time: datetime,
    end_time: datetime,
    href: str = None,
) -> Collection:
    """Create a STAC Collection

    Args:
        title (str): Collection title
        description (str): Collection description
        catalog_type (str): One of
        'ABSOLUTE_PUBLISHED', 'RELATIVE_PUBLISHED', 'SELF_CONTAINED'
        providers (list[Provider]): One or more providers,
        see https://pystac.readthedocs.io/en/latest/api.html#provider
        license (str): Data provider license token
        license_link (Link): license Link object,
        see https://pystac.readthedocs.io/en/latest/api.html#link
        extent (list): Extent. ex [xmin, ymin, xmax, ymax].
        See https://pystac.readthedocs.io/en/latest/api.html#spatialextent
        start_time (datetime): Collection start time object- must be in UTC time zone
        end_time (datetime): Collection end time object- must be in UTC time zone
        href (str, optional): Location to store Collection json. Defaults to None,
        and no json will be created.

    Returns:
        Collection: STAC Collection object
    """
    # The ID may be changed to be provided as an arg if desired
    id = title.replace(" ", "-")

    collection = Collection(
        id=id,
        title=title,
        description=description,
        providers=providers,
        license=license,
        extent=Extent(SpatialExtent([extent]),
                      TemporalExtent([start_time, end_time])),
        catalog_type=getattr(CatalogType, catalog_type),
    )
    collection.add_link(license_link)

    if href:
        collection.set_self_href(href)
        collection.save_object()

    return collection


# This includes a set of minimum requirements for the creation of a STAC Item,
# and should be added to/modified as necessary to develop a dataset-specific package.
def create_item(
    title: str,
    description: str,
    geometry: str,
    start_datetime: datetime,
    end_datetime: datetime = None,
    asset_href: str = None,
    asset_type: str = None,
    projection_epsg: int = None,
    href: str = None,
) -> Item:
    """Create a STAC Item

    Args:
        title (str): STAC Item name
        description (str): STAC Item description
        geometry (str): Footprint of the asset represented by this item, formatted
        according to RFC 7946, section 3.1 (GeoJSON)
        start_datetime (datetime): Asset datetime
        end_datetime (datetime, optional): Asset end datetime if a range is required
        asset_href (str, optional): Location of the asset represented by the item.
        Defaults to None.
        asset_type (str, optional): If an asset_href is provided, the asset type must
        also be provided.
        See https://pystac.readthedocs.io/en/latest/api.html#mediatype for the types.
        Defaults to None.
        projection_epsg (int, optional): EPSG code of the asset spatial reference.
        Defaults to None.
        href (str, optional): Location to store Item json. Defaults to None,
        and no json will be created.

    Raises:
        ValueError: If an asset_href is provided, but no asset_type is provided

    Returns:
        Item: STAC Item object
    """
    # The ID may be changed to be provided as an arg if desired
    id = title.replace(" ", "-")

    properties = {
        "title": title,
        "description": description,
    }

    bbox = Polygon(geometry.get("coordinates")[0]).bounds

    # Create item
    item = Item(
        id=id,
        geometry=geometry,
        bbox=bbox,
        datetime=start_datetime,
        properties=properties,
        stac_extensions=[],
    )

    item.common_metadata.start_datetime = start_datetime
    if end_datetime:
        item.common_metadata.end_datetime = end_datetime

    if projection_epsg is not None:
        item_projection = ProjectionExtension.ext(item, add_if_missing=True)
        item_projection.epsg = projection_epsg

    # Add asset href
    if asset_href is not None:
        if not asset_type:
            raise ValueError("Asset type is required if an asset is provided")

        # "data" is used a placeholder, but you may want to change the data
        # asset name.
        item.add_asset(
            "data",
            Asset(
                href=asset_href,
                media_type=getattr(MediaType, asset_type),
                roles=["data"],
                title=f"{title} Data",
            ),
        )

    if href is not None:
        # "metadata" is used a placeholder, but you may want to change the metadata
        # asset name.
        item.add_asset(
            "metadata",
            Asset(
                href=href,
                media_type=MediaType.JSON,
                roles=["metadata"],
                title=f"{title} Metadata",
            ),
        )
        item.set_self_href(href)
        item.save_object()

    return item
