import pytest

USER = "test@test.com"
PWD = "1234"

from playwright.sync_api import Page, expect

def test_user_can_login(page:Page):
    page.goto('https://app.todoist.com/auth/login')
    page.locator("[type=email]").fill(USER)
    page.locator("[type=password]").fill(PWD)
    page.locator("[type=submit]").click()
    page.wait_for_url('https://app.todoist.com/app/')
    cookies = page.context.cookies()
    assert any(cookie['name'] == 'todoist' for cookie in cookies), f"Expected cookie todoist doesnt exists in {cookies}"
    # expect(page.get_by_test_id("task-selection-list-container")).to_be_visible()
