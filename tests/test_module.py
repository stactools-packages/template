import unittest

import stactools.ephemeral


class TestModule(unittest.TestCase):
    def test_version(self) -> None:
        self.assertIsNotNone(stactools.ephemeral.__version__)
