import pytest

from complex_asset_graph import nabisco_cereals


@pytest.fixture(scope='module')
def cereals():
    return [{'name': 'cereal1', 'mfr': 'N'}, {'name': 'cereal2', 'mfr': 'K'}]


def test_nabisco_cereals(cereals):
    result = nabisco_cereals(cereals)
    assert len(result) == 1
    assert result == [{'name': 'cereal1', 'mfr': 'N'}]
