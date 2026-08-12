from pathlib import Path
from playwright.sync_api import sync_playwright, TimeoutError


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

    for _ in range(120):
        if is_logged_in(page):
            return

        page.wait_for_timeout(1000)

    raise TimeoutError("Timed out waiting for ConnexApp login to finish.")


def open_portal(portal_url):
    playwright = sync_playwright().start()

    context = playwright.chromium.launch_persistent_context(
        BROWSER_DATA_DIR,
        headless=False,
    )

    page = context.pages[0]

    page.goto(portal_url)
    page.wait_for_load_state("networkidle")

    return playwright, context, page
