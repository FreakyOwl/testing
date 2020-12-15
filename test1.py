import pytest
import scriptfortests


def test_exception():
    with pytest.raises(FileNotFoundError):
        scriptfortests.getdata('1234.txt')
