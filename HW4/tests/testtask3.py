from HW4.task3 import mylogger
import pytest


@pytest.mark.parametrize('test_text', ('error:',
                                       'ERROR!',
                                       'Error:,'))
def test_logger_error(test_text, capsys):
    mylogger(test_text)
    assert test_text in capsys.readouterr().err


@pytest.mark.parametrize('test_text', ('An',
                                       'Beneathsedfes',
                                       'In odfdssd'))
def test_logger_out(test_text, capsys):
    mylogger(test_text)
    assert test_text in capsys.readouterr().out