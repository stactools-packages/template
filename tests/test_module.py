import stactools.ephemeral


def test_version() -> None:
    assert stactools.ephemeral.__version__ is not None
