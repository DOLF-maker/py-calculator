import pytest
from calculator import rrr_calculator

#test calculation logic
def test_rrr_calculation():
    result = rrr_calculator(510, 8, 2.9)
    assert result == 56.86