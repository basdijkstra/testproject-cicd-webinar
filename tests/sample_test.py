import pytest

from src.testproject.sdk.drivers import webdriver


@pytest.fixture()
def driver():
    driver = webdriver.Chrome()
    yield driver
    driver.quit()


def test_sample():

    driver.get("https://example.testproject.io/web/")

    driver.find_element_by_css_selector("#name").send_keys("John Smith")
    driver.find_element_by_css_selector("#password").send_keys("12345")
    driver.find_element_by_css_selector("#login").click()

    result = driver.find_element_by_css_selector("#greetings").is_displayed()

    assert result is True
