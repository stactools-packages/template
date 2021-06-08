import unittest

import stactools.subpackage


class TestModule(unittest.TestCase):
    def test_version(self):
        self.assertIsNotNone(stactools.subpackage.__version__)
