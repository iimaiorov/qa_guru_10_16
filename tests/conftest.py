import pytest
from selene import browser


@pytest.fixture(params=[(1920, 1080), (1600, 900)], scope='function')
def desktop_browser(request):
    browser.config.window_width, browser.config.window_height = request.param
    browser.config.base_url = 'https://github.com'
    yield
    browser.quit()


@pytest.fixture(params=[(360, 800), (768, 1024)], scope='function')
def mobile_browser(request):
    browser.config.window_width, browser.config.window_height = request.param
    browser.config.base_url = 'https://github.com'
    yield
    browser.quit()


@pytest.fixture(params=[(1920, 1080), (360, 800), (768, 1024), (1600, 900)],
                scope='function')
def desktop_and_mobile_browser(request):
    browser.config.window_width, browser.config.window_height = request.param
    browser.config.base_url = 'https://github.com'
    yield
    browser.quit()
