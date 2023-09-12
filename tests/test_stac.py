from stactools.ephemeral import stac

from . import test_data


def test_create_collection() -> None:
    # This function should be updated to exercise the attributes of interest on
    # the collection

    collection = stac.create_collection()
    collection.set_self_href(None)  # required for validation to pass
    assert collection.id == "example-collection"
    assert collection.extra_fields["custom_attribute"] == "foo"
    collection.validate()


def test_create_item() -> None:
    # This function should be updated to exercise the attributes of interest on
    # a typical item

    item = stac.create_item(test_data.get_path("data/asset.tif"))
    assert item.id == "example-item"
    assert item.properties["custom_attribute"] == "foo"
    item.validate()
