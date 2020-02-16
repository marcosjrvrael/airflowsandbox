import sys
sys.path.append('../')
from src.simplefunction import get_count

def test_get_count():
    result = get_count('teste')
    assert result == 2