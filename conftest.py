from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
import pytest


def pytest_addoption(parser):
    parser.addoption(
        "--headless",
        action="store_true",
        default=True,
        help="Run Chrome in headless mode"
    )


@pytest.fixture
def driver(request):
    headless = request.config.getoption("--headless")

    chrome_options = Options()

    if headless:
        chrome_options.add_argument("--headless=new")
        chrome_options.add_argument("--disable-gpu")
        chrome_options.add_argument("--window-size=1280,800")

    service = Service(ChromeDriverManager().install())

    drv = webdriver.Chrome(
        service=service,
        options=chrome_options
    )

    drv.implicitly_wait(5)

    yield drv

    drv.quit()