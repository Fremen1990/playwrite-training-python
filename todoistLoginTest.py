import pytest

USER = "test@test.com"
PWD = "1234"

from playwright.sync_api import Page, expect

def test_exercise3(page:Page):
    page.goto('https://app.todoist.com/auth/login')
    page.locator("[type=email]").fill(USER)
    page.locator("[type=password]").fill(PWD)
    page.locator("[type=submit]").click()
    expect(page.get_by_test_id("task-selection-list-container")).to_be_visible()
