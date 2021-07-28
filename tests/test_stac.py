import unittest

from stactools.ephemeral import stac


class StacTest(unittest.TestCase):
    def test_create_collection(self):
        # Write tests for each for the creation of a STAC Collection
        # Create the STAC Collection...
        collection = stac.create_collection()
        collection.set_self_href("")

        # Check that it has some required attributes
        self.assertEqual(collection.id, "my-collection-id")
        # self.assertEqual(collection.other_attr...

        # Validate
        collection.validate()

    def test_create_item(self):
        # Write tests for each for the creation of STAC Items
        # Create the STAC Item...
        item = stac.create_item("/path/to/asset.tif")

        # Check that it has some required attributes
        self.assertEqual(item.id, "my-item-id")
        # self.assertEqual(item.other_attr...

        # Validate
        item.validate()
