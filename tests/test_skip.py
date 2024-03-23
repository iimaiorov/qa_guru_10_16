import pytest
from selene import browser, have, by


def is_desktop():
    return browser.config.window_width > 1011


def is_mobile():
    return browser.config.window_width < 1011


def test_github_desktop(desktop_and_mobile_browser):
    if is_desktop():
        browser.open('/')
        browser.element('.HeaderMenu-link--sign-in').click()
        browser.element(by.class_name('auth-form-header')).should(have.text('Sign in to GitHub'))
    else:
        pytest.skip('Skiped but this is mobile size')


def test_github_mobile(desktop_and_mobile_browser):
    if is_mobile():
        browser.open('/')
        browser.element('.Button--link .Button-content').click()
        browser.element('.HeaderMenu-link--sign-in').click()
        browser.element(by.class_name('auth-form-header')).should(have.text('Sign in to GitHub'))
    else:
        pytest.skip('Skiped but this is desktop size')

