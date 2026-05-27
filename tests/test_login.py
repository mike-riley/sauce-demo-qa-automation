from pages.login_page import LoginPage


def test_login_success(driver):

    login_page = LoginPage(driver)

    login_page.visit(
        LoginPage.URL
    )

    login_page.login(
        "standard_user",
        "secret_sauce"
    )

    assert login_page.is_logged_in()