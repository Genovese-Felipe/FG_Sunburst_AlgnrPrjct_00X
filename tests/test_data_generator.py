import pandas as pd
from src.data_generator import generate_construction_data

def test_generate_construction_data_returns_dataframe():
    """
    Tests if the generate_construction_data function returns a pandas DataFrame.
    """
    data = generate_construction_data()
    assert isinstance(data, pd.DataFrame)

def test_generate_construction_data_not_empty():
    """
    Tests if the generated DataFrame is not empty.
    """
    data = generate_construction_data()
    assert not data.empty

def test_generate_construction_data_has_expected_columns():
    """
    Tests if the generated DataFrame has the expected columns.
    """
    data = generate_construction_data()
    expected_columns = ['pillar', 'area', 'service', 'task', 'cost']
    assert all(col in data.columns for col in expected_columns)