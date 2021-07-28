import os.path
from tempfile import TemporaryDirectory

import pystac
from stactools.ephemeral.commands import create_ephemeralcmd_command
from stactools.testing import CliTestCase


class CommandsTest(CliTestCase):
    def create_subcommand_functions(self):
        return [create_ephemeralcmd_command]

    def test_create_collection(self):
        with TemporaryDirectory() as tmp_dir:
            # Run your custom create-collection command and validate

            # Example:
            result = self.run_command([
                "ephemeralcmd",
                "create-collection",
                os.path.join(tmp_dir, "destination.json"),
            ])

            self.assertEqual(result.exit_code,
                             0,
                             msg="\n{}".format(result.output))

            jsons = [p for p in os.listdir(tmp_dir) if p.endswith(".json")]
            self.assertEqual(len(jsons), 1)

            collection = pystac.read_file(os.path.join(tmp_dir, jsons[0]))
            self.assertEqual(collection.id, "my-collection-id")

            collection.validate()

    def test_create_item(self):
        with TemporaryDirectory() as tmp_dir:
            # Run your custom create-item command and validate

            # Example:
            result = self.run_command([
                "ephemeralcmd",
                "create-item",
                "/my/source.x",
                os.path.join(tmp_dir, "destination.json"),
            ])
            self.assertEqual(result.exit_code,
                             0,
                             msg="\n{}".format(result.output))

            jsons = [p for p in os.listdir(tmp_dir) if p.endswith(".json")]
            self.assertEqual(len(jsons), 1)

            item_path = os.path.join(tmp_dir, jsons[0])
            item = pystac.read_file(item_path)
            self.assertEqual(item.id, "my-item-id")

            item.validate()
