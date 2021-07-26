import unittest

import stactools.ephemeral


class TestModule(unittest.TestCase):
    def test_version(self):
        self.assertIsNotNone(stactools.ephemeral.__version__)
