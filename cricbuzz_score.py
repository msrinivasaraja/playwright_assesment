from playwright.sync_api import sync_playwright
with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    page = browser.new_page()
    page.goto("https://cricbuzz.com/" , wait_until="domcontentloaded")
    # Replace this with the actual selector you identified
    match = page.locator('.my-2').first
    score_element = match.locator("span.font-medium").nth(1)
    # Wait for the score element
    score_element.wait_for(state="visible", timeout=30000)

    # Extract score
    score = score_element.inner_text()
    print(score)
    page.screenshot(path="score.png")
    browser.close()