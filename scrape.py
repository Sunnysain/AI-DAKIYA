from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup

def scrape_website(website):
    chrome_options = Options()
    chrome_options.add_argument("--headless")  # Run in headless mode
    chrome_options.add_argument("--no-sandbox")  # For running in a sandbox environment

    # Define the service with the path to chromedriver
    chrome_service = Service(executable_path="C:\AI DAKIYA\chromedriver.exe")

    # Initialize the Chrome WebDriver with the Service object
    driver = webdriver.Chrome(service=chrome_service, options=chrome_options)
    
    print(f"Connecting to {website}...")
    driver.get(website)

    html = driver.page_source
    driver.quit()  # Close the browser
    return html

def extract_body_content(html_content):
    soup = BeautifulSoup(html_content, "html.parser")
    body_content = soup.body
    if body_content:
        return str(body_content)
    return ""

def clean_body_content(body_content):
    soup = BeautifulSoup(body_content, "html.parser")

    for script_or_style in soup(["script", "style"]):
        script_or_style.extract()

    # Get text or further process the content
    cleaned_content = soup.get_text(separator="\n")
    cleaned_content = "\n".join(
        line.strip() for line in cleaned_content.splitlines() if line.strip()
    )

    return cleaned_content

def split_dom_content(dom_content, max_length=6000):
    return [
        dom_content[i : i + max_length] for i in range(0, len(dom_content), max_length)
    ]
