from pathlib import Path
from playwright.sync_api import sync_playwright


BROWSER_DATA_DIR = Path(__file__).parent / "browser-data"


def is_logged_in(page):
    current_url = page.url

    if "/auth/" in current_url:
        return False

    if "/web/auth-callback" in current_url:
        return False

    if current_url.startswith("https://connexapp.dayzim.com/web/"):
        return True

    return False


def wait_for_manual_login(page):
    print("Please log into ConnexApp in the browser.")
    print("Waiting for ConnexApp to finish redirecting...")

    if wait_until_logged_in(page, timeout_seconds=300):
        return

    raise RuntimeError("Timed out waiting for ConnexApp login to finish.")


def wait_until_logged_in(page, timeout_seconds):
    for _ in range(timeout_seconds):
        if is_logged_in(page):
            print("Automated login successful!")
            print()
            return True
        page.wait_for_timeout(1000)

    return False


def has_login_credentials(login_config):
    if not login_config:
        return False

    email = login_config.get("email") or login_config.get("username")
    return bool(email and login_config.get("password"))


def login_if_needed(page, login_config=None):
    if is_logged_in(page):
        return

    if has_login_credentials(login_config):
        print("Login credentials found in profile. Attempting automated login...")
        login_with_credentials(page, login_config)

        if wait_until_logged_in(page, timeout_seconds=30):
            return

        print("Automated login did not complete. Falling back to manual login.")

    wait_for_manual_login(page)


def login_with_credentials(page, login_config):
    email = login_config.get("email")
    password = login_config["password"]

    page.get_by_role("textbox", name="Email").clear()
    page.get_by_role("textbox", name="Email").fill(email)
    page.get_by_role("textbox", name="Password").clear()
    page.get_by_role("textbox", name="Password").fill(password)
    page.get_by_role("button", name="Sign In").click()


def open_portal(portal_url, headless=False):
    playwright = sync_playwright().start()

    context = playwright.chromium.launch_persistent_context(
        BROWSER_DATA_DIR,
        headless=headless,
    )

    page = context.pages[0]

    page.goto(portal_url)
    page.wait_for_load_state("networkidle")

    return playwright, context, page
