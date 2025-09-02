'''
Requirements

- Get search keywords from the command line arguments
  - Read the command line arguments from sys.argv
- Retrieve the search results page
  - Fetch the search results page with the requests module
- Open a browser tab for each result
  - Call the webbrowser.open() function to open the web browser

.vertical-tabs__tab
'''

# from playwright.sync_api import sync_playwright
# import sys

# print("Searching...")

# # Take search terms from CLI args
# search_term = " ".join(sys.argv[1:])

# with sync_playwright() as p:
#   browser = p.firefox.launch(channel="firefox", headless=False) # Launch browser
#   page = browser.new_page()

#   page.goto(f"https://pypi.org/search/?q={search_term}")

#   links = page.locator("a.package-snippet").all()[:5]

#   for link in links:
#       href = link.get_attribute("href")
#       if href:
#           new_page = browser.new_page()
#           new_page.goto("https://pypi.org" + href)

#   print(f"Opened top {len(links)} results for '{search_term}'")

# searchpypi.py
# Usage: python3 searchpypi.py <search terms>
# Example: python3 searchpypi.py requests

# searchpypi.py
import sys
from playwright.sync_api import sync_playwright

def main():
    if len(sys.argv) < 2:
        print("Usage: python3 searchpypi.py <search terms>")
        sys.exit(1)

    search_term = " ".join(sys.argv[1:])
    print(f"Searching for '{search_term}' on PyPI...")

    with sync_playwright() as p:
        browser = p.firefox.launch(headless=False)  # <-- Firefox browser
        page = browser.new_page()
        
        page.goto(f"https://pypi.org/search/?q={search_term}")
        page.wait_for_selector("a.package-snippet")

        links = page.query_selector_all("a.package-snippet")
        top_links = [link.get_attribute("href") for link in links[:5]]

        if not top_links:
            print(f"No results found for '{search_term}'")
            browser.close()
            return

        print(f"Opened top {len(top_links)} results for '{search_term}':")
        for href in top_links:
            new_page = browser.new_page()
            new_page.goto("https://pypi.org" + href)
            print(" - https://pypi.org" + href)

        print("\nPress CTRL+C to quit.")
        try:
            while True:
                pass
        except KeyboardInterrupt:
            browser.close()

if __name__ == "__main__":
    main()
