import pytest
import main_script


def test_exception():
    with pytest.raises(FileNotFoundError):
        main_script.get_data('1234.txt')
        
        
def test_urlformat():
    with open('VK_URLs.txt', 'r') as listofurls:
        for line in listofurls:
            assert line[:15] == 'https://vk.com/'
            assert line[-1] == '\n'
