import pytest

from playwright.sync_api import Page, expect

def test_exercise3(page:Page):
    page.goto('https://qbek.github.io/selenium-exercises/pl/radio_buttons.html')
    page.locator('[value=radiozet]').check()
    expect(page.locator("#radiozet-details a")).to_have_attribute('href','https://www.radiozet.pl' )
