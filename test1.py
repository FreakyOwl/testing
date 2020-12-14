import pytest
import scriptfortests


def test_assert():
    assert scriptfortests.listofurls.name == "123.txt"

def test_exception():
    with pytest.raises(SystemExit):
        scriptfortests.filefun()
