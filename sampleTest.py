import pytest

from playwright.sync_api import Page, expect


def test_exercise1(page:Page):
    page.goto('https://qbek.github.io/selenium-exercises/pl/basic_form.html')
    page.locator('#firstname').fill("Tomek")
    page.locator('#lastname').fill("Stanley")
    page.locator('#email').fill("test@email.com")
    page.locator("[type=submit]").click()

    # expect(page.locator('#firstname-check')).to_have_text("Tomek")
    # expect(page.locator('#lastname-check')).to_have_text("Stanley")
    # expect(page.locator('.form-control-plaintext')).to_have_value("test@email.com")
    # expect(page.locator('[type=lead]')).to_have_value("test@email.com")
    # expect(page.locator('button:text("Popraw")')).to_be_visible()

    # Assert all in a report - one assertion
    page_data = {
        'fname': page.locator('#firstname-check').text_content(),
        'lname': page.locator("#lastname-check").text_content(),
        'email': page.locator('.form-control-plaintext').input_value()
    }

    expected = {
        'fname': 'Tomek',
        'lname': 'Stanley',
        'email': 'test@email.com'
    }

    assert page_data == expected