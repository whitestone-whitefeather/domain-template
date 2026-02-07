
from src.example_module import transform

def test_transform_unique_sorted():
    assert transform([3,1,2,2,3]) == [1,2,3]
