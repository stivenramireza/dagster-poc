import pytest

from dagster import materialize

from complex_asset_graph import (
    nabisco_cereals,
    cereals,
    cereal_protein_fractions,
    highest_protein_nabisco_cereal,
)


@pytest.fixture(scope='module')
def assets():
    return [
        nabisco_cereals,
        cereals,
        cereal_protein_fractions,
        highest_protein_nabisco_cereal,
    ]


def test_cereal_assets(assets):
    result = materialize(assets)
    assert result.success
    assert (
        result.output_for_node('highest_protein_nabisco_cereal') == '100% Bran'
    )
