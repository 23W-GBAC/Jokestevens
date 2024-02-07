import time
import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# =========================
# Function Definitions
# =========================

# Function to make an HTTP request to a website
def make_request(url):
    try:
        # Attempt to make an HTTP request to the specified URL
        response = requests.get(url)
        response.raise_for_status()  # Raise an HTTPError for bad responses (4xx or 5xx)

        # Display the content of the HTTP response
        print("HTTP Response Content:")
        print(response.content)

    except requests.exceptions.RequestException as e:
        print(f"Error making the HTTP request: {e}")

# Function to scrape titles from a website
def scrape_titles(url):
    try:
        # Make an HTTP request
        response = requests.get(url)
        response.raise_for_status()

        # Create a BeautifulSoup object
        soup = BeautifulSoup(response.content, 'html.parser')  # Create a BeautifulSoup object

        # Find all h1 tags
        titles = soup.find_all('h1')  # Use find_all on the BeautifulSoup object

        # Display the titles
        print("Titles:")
        for title in titles:
            print(title.text)

    except requests.exceptions.RequestException as e:
        print(f"Error making the HTTP request: {e}")

# Function to scrape titles with error check
def scrape_titles_with_error_check(url):
    try:
        # Making the HTTP request
        response = requests.get(url)
        response.raise_for_status()

        # Creating a BeautifulSoup object
        soup = BeautifulSoup(response.content, 'html.parser')

        # Finding all 'h2' tags
        titles = soup.find_all('h2')

        # Check if any 'h2' tags were found
        if not titles:  # This checks if the list is empty
            print("No 'h2' titles found on the page.")
        else:
            # Displaying the titles
            print("Titles:")
            for title in titles:
                print(title.text)

    except requests.exceptions.RequestException as e:
        print(f"Error making the HTTP request: {e}")

# Function to scrape titles with advanced parsing
def scrape_titles_advanced(url):
    try:
        # Making the HTTP request
        response = requests.get(url)
        response.raise_for_status()

        # Creating a BeautifulSoup object
        soup = BeautifulSoup(response.content, 'html.parser')

        # Finding all 'article' tags
        articles = soup.find_all('article', class_='full-docsum')

        # Check if any 'article' tags were found
        if not articles:
            print("No articles found on the page.")
        else:
            # Displaying the titles and URLs
            print("Articles:")
            for article in articles:
                title_tag = article.find('a', class_='docsum-title')
                if title_tag:
                    title = title_tag.text.strip()
                    url = 'https://pubmed.ncbi.nlm.nih.gov' + title_tag['href']
                    print(f"Title: {title}")
                    print(f"URL: {url}\n")

    except requests.exceptions.RequestException as e:
        print(f"Error making the HTTP request: {e}")

# Function to scrape titles from multiple pages
def scrape_titles_multiple_pages(base_url, start_page, num_pages):
    for page_num in range(start_page, start_page + num_pages):
        page_url = f"{base_url}&page={page_num}"
        print("------ ARTICLE PAGE")
        scrape_titles_advanced(page_url)
        time.sleep(1)  # Adding a 1-second delay between requests

# Function checking for the presence of robots.txt before scraping
def check_robots_txt(url):
    try:
        # Constructing the robots.txt URL
        robots_url = f"{url}/robots.txt"

        # Making the HTTP request
        response = requests.get(robots_url)
        response.raise_for_status()

        # Displaying the content of robots.txt
        print("Robots.txt Content:")
        print(response.text)

    except requests.exceptions.RequestException as e:
        print(f"Error making the HTTP request: {e}")

# Function to check website policies and terms of service, if any
def check_website_policies(url):
    try:
        # Making the HTTP request
        response = requests.get(url)
        response.raise_for_status()

        # Extracting and displaying website policies and terms of service
        soup = BeautifulSoup(response.content, 'html.parser')
        policy_keywords = ['policy', 'privacy']
        terms_keywords = ['terms', 'conditions']

        policies = find_link_by_keywords(soup, policy_keywords)
        terms = find_link_by_keywords(soup, terms_keywords)

        print("Website Policies:")
        print(policies if policies else "Not found")

        print("Terms of Service:")
        print(terms if terms else "Not found")

    except requests.exceptions.RequestException as e:
        print(f"Error making the HTTP request: {e}")

# Helper Function (to check_website_policies function) that searches for links containing specified keywords
def find_link_by_keywords(soup, keywords):
    for keyword in keywords:
        link = soup.find('a', text=lambda text: text and keyword in text.lower())
        if link:
            return link['href']
    return None

# Function to scrape AJAX-based dynamic content
def scrape_ajax_page(url):
    try:
        # Initialize Selenium WebDriver
        driver = webdriver.Chrome()
        driver.get(url)

        # Wait for the AJAX content to load
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CLASS_NAME, 'nearby-location')))

        # Parse the page source with BeautifulSoup
        soup = BeautifulSoup(driver.page_source, 'html.parser')

        # Find all nearby location elements
        locations = soup.find_all('a', class_='nearby-location weather-card')

        # Extract and print the location names and URLs
        print("Nearby Locations and URLs:")
        for location in locations:
            location_name = location.find('span', class_='text title no-wrap').text.strip()
            location_url = location['href']
            print(f"{location_name}: {ajax_url}{location_url}")

    except Exception as e:
        print(f"Error: {e}")

    finally:
        # Close the WebDriver
        driver.quit()

# Function to handle captcha challenges while scraping
def scrape_with_captcha_handling(url):
    try:
        # Uh-oh, a wild captcha appears!
        raise Exception("Captcha Challenge")

    except Exception as e:
        print(f"Captcha encountered. Handling with a solution: {e}")

        # An example of captcha handling (in a perfect world with user intervention)
        user_response = input("Please solve the captcha and press Enter to continue.")
        if user_response:
            scrape_ajax_page(ajax_url)


# ===========================
# Example Usage of Functions
# ===========================
if __name__ == "__main__":
    example_website = 'https://example.com'
    pubmed_url = "https://pubmed.ncbi.nlm.nih.gov"
    cnn_url = 'https://cnn.com'
    accuweather_url = 'https://www.accuweather.com'

    # =========================
    # CALL FUNCTIONS as needed
    # PLEASE UNCOMMENT TO RUN!
    # =========================

    # Example Usages (functions: make_request, scrape_titles, scrape_titles_with_error_check)
    # make_request(example_website)
    # scrape_titles(example_website)
    # scrape_titles_with_error_check(example_website)

    # Example Usage (functions: scrape_titles_advanced, scrape_titles_multiple_pages)
    base_url = pubmed_url  # The base URL for PubMed cancer search results
    search_query = "/?term=cancer"  # The specific search query with pagination
    webpage_number = "&page=2"
    full_url = base_url + search_query + webpage_number  # Full URL for the page we want to scrape
    # scrape_titles_advanced(full_url)

    base_website_url = base_url + search_query
    start_page_number = 1  # Start scraping from page 1
    number_of_pages = 3  # Scrape 3 pages in total
    # scrape_titles_multiple_pages(base_website_url, start_page_number, number_of_pages)

    # Example Usage (functions: check_robots_txt, check_website_policies)
    # check_robots_txt(example_website)    # No robots.txt page Found
    # check_robots_txt(cnn_url)        # Has a robots.txt page
    # check_website_policies(cnn_url)

    # Example Usage (function: scrape_ajax_page)
    ajax_url = accuweather_url
    # scrape_ajax_page(ajax_url)
