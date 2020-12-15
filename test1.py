import pytest
import scriptfortests


def test_exception():
    with pytest.raises(FileNotFoundError):
        scriptfortests.getdata('1234.txt')
        
        
def test_fileformat():
    with open('123.txt', 'r') as listofurls:
        for line in listofurls:
            assert line[:15] == 'https://vk.com/'
            assert line[-1] == '\n'
