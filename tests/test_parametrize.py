import pytest
from selene import browser, have, by


@pytest.mark.parametrize('desktop_browser', [(1366, 768)], indirect=True)
def test_github_desktop(desktop_browser):
    browser.open('/')

    browser.element(by.link_text('Sign in')).click()
    browser.element(by.class_name('auth-form-header')).should(have.text('Sign in to GitHub'))


@pytest.mark.parametrize('mobile_browser', [(393, 851)], indirect=True)
def test_github_mobile(mobile_browser):
    browser.open('/')

    browser.element(by.link_text('Sign in')).click()
    browser.element(by.class_name('auth-form-header')).should(have.text('Sign in to GitHub'))
