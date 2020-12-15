import pytest
import scriptfortests


def test_exception():
    with pytest.raises(SystemExit):
        scriptfortests.getdata('1234.txt')
