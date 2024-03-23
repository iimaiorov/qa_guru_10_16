from selene import browser, have, by


def test_github_desktop(desktop_browser):
    browser.open('/')

    browser.element('.HeaderMenu-link--sign-in').click()
    browser.element(by.class_name('auth-form-header')).should(have.text('Sign in to GitHub'))


def test_github_mobile(mobile_browser):
    browser.open('/')

    browser.element('.Button--link .Button-content').click()
    browser.element('.HeaderMenu-link--sign-in').click()
    browser.element(by.class_name('auth-form-header')).should(have.text('Sign in to GitHub'))
