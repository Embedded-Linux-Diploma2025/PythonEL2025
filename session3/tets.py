import re
from playwright.sync_api import Playwright, sync_playwright, expect


def run(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://partner.hyundai.com/gscm/")
    page.locator("#mainframe_VFrameSet_LoginFrame_CommLgds010_1_form_ImageViewer00ImageElement").get_by_role("img", name="ImageViewer00").click()
    page.locator("#mainframe_VFrameSet_LoginFrame_CommLgds010_0_form_ImageViewer00ImageElement").get_by_role("img", name="ImageViewer00").click()
    page.locator("#mainframe_VFrameSet_LoginFrame_form_div_logo_edt_userId_input").click()
    page.locator("#mainframe_VFrameSet_LoginFrame_form_div_logo_edt_userId_input").press("CapsLock")
    page.locator("#mainframe_VFrameSet_LoginFrame_form_div_logo_edt_userId_input").fill("P311153")
    page.locator("#mainframe_VFrameSet_LoginFrame_form_div_logo_edt_userId_input").press("Tab")
    page.locator("#mainframe_VFrameSet_LoginFrame_form_div_logo_edt_userPwd_input").press("CapsLock")
    page.locator("#mainframe_VFrameSet_LoginFrame_form_div_logo_edt_userPwd_input").fill("P")
    page.locator("#mainframe_VFrameSet_LoginFrame_form_div_logo_edt_userPwd_input").press("CapsLock")
    page.locator("#mainframe_VFrameSet_LoginFrame_form_div_logo_edt_userPwd_input").fill("Pp318390@@@@")
    page.locator("#mainframe_VFrameSet_LoginFrame_form_div_logo_edt_userOtp_input").click()
    page.locator("#mainframe_VFrameSet_LoginFrame_form_div_logo_btn_loginTextBoxElement").get_by_text("Login").click()
    page.get_by_text("Confirm").click()

    # ---------------------
    context.close()
    browser.close()


with sync_playwright() as playwright:
    run(playwright)
