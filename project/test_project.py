import project
import requests
from datetime import datetime
from datetime import timedelta


def test_making_link():
    cpv = "42111100-1"
    today = datetime.today()
    week = timedelta(days=7)
    last_week = today - week

    # expected parts of the URL
    expected_starting = last_week.strftime('%Y-%m-%dT00:00:00')
    expected_ending = today.strftime('%Y-%m-%dT23:59:59')

    expected_link = (
        f"https://ezamowienia.gov.pl/mo-board/api/v1/notice?NoticeType=ContractNotice"
        f"&TenderType=1.1.1&CpvCode={cpv}&PublicationDateFrom={expected_starting}"
        f"&PublicationDateTo={expected_ending}&PageSize=100"
    )

    assert type(project.making_link(cpv)) == str

    assert project.making_link(cpv) == expected_link


def test_appending_deals():
    deals = [{"orderObject": "Deal 1"}, {"orderObject": "Deal 2"}]
    expected_output = ["Deal 1", "Deal 2"]

    assert project.appending_deals(deals) == expected_output


captured_error_message = None


# changing error_box not to show popout window with message but to caching message for sake of testing
def capture_error_msg(message):
    global captured_error_message
    captured_error_message = message


def test_engine_timeout():
    global captured_error_message

    # define a CPV code that works
    cpv = "42111100-1"

    def raising_timeout():
        raise requests.exceptions.Timeout

    # replacing `requests.get` with a function that will rais a Timeout exception
    original_get = project.requests.get
    project.requests.get = raising_timeout

    # replace error_box with test version
    original_error_box = project.error_box
    project.error_box = capture_error_msg

    try:
        project.engine(cpv)
        assert captured_error_message == "Connection to eZam timeout"
    finally:
        # restore the original function
        requests.get = original_get
        project.error_box = original_error_box


def test_engine_validation():

    global captured_error_message
    cpv = None

    # replace error_box with test version
    original_error_box = project.error_box
    project.error_box = capture_error_msg

    try:
        project.engine(cpv)
        assert captured_error_message == "Please enter the CPV code"
    finally:
        # restore the original function
        project.error_box = original_error_box


def test_engine_invalid_cpv():
    global captured_error_message
    invalid_cpvs = ["invalid", "1234", "12345678", "abcdefgh-1"]

    # replace error_box with test version
    project.error_box = capture_error_msg

    for cpv in invalid_cpvs:
        project.engine(cpv)
        assert captured_error_message == (f'"{cpv}" is not valid CPV code'
                                          f'\n CPV code should be made of 8 digits, dash and 1 digit'
                                          f'\nLike this: 42111100-1')
