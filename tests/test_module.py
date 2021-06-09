import unittest

import stactools.package


class TestModule(unittest.TestCase):
    def test_version(self):
        self.assertIsNotNone(stactools.package.__version__)
