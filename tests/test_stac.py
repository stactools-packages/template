import os
from tempfile import TemporaryDirectory
import unittest

import pystac
from stactools.ephemeral import stac


class StacTest(unittest.TestCase):
    def test_create_collection(self):
        # Write tests for each for the creation of a STAC Collection
        with TemporaryDirectory() as tmp_dir:
            # Create the STAC Collection...
            stac.create_collection()

            # Test that it has been created and validate
            jsons = [p for p in os.listdir(tmp_dir) if p.endswith(".json")]
            self.assertEqual(len(jsons), 1)

            collection_path = os.path.join(tmp_dir, jsons[0])

            collection = pystac.read_file(collection_path)

            collection.validate()

    def test_create_item(self):
        # Write tests for each for the creation of STAC Items
        with TemporaryDirectory() as tmp_dir:
            # Create the STAC Item...
            stac.create_item()

            # Test that it has been created and validate
            jsons = [p for p in os.listdir(tmp_dir) if p.endswith(".json")]
            self.assertEqual(len(jsons), 1)

            item_path = os.path.join(tmp_dir, jsons[0])

            item = pystac.read_file(item_path)

            item.validate()
