# Automation Project

Hello! I'm Onajokeoghene Piomoki Stevens, a first-semester student eagerly navigating the intricate landscape of Health Informatics. As I embarked on a mission to illuminate the role of artificial intelligence (AI) in healthcare organizations through a blog post, I found myself entangled in the complexities of content gathering. The sheer repetitiveness and time-consuming nature of this task sparked an idea: why not automate the process? I'm inviting you to embark on a coding journey together. This blog isn't just about me sharing ideas; it's a space where we collectively enhance a Python script and brainstorm ways to make it even more awesome. Your insights and experiences are valuable, so feel free to join in!

📝 Introduction to the Script:

In our first collaborative coding session, I've crafted a Python scaimed at automating web scraping and content aggregation for healthcare organizations using AI. This script is your ticket to streamlining the process of gathering information for your blog posts.

🐍 Script Language: Python

Before we dive into the intricacies, let's establish that the language powering this script is Python. If you're new to Python, fear not! We're in this together, and I'll guide you every step of the way. Over the next four weeks, I'll be your guide on this journey, sharing my experiences, hurdles, and triumphs as I automate web scraping and content aggregation.

# The Repetitive Challenge: Why choosing automation is the way forward
In the realm of health informatics, where the pace of innovation is relentless, staying current with the latest advancements is paramount. My blog post on healthcare organizations leveraging AI demanded a meticulous exploration of diverse sources—company websites, press releases, and industry publications. However, as I manually scoured the web for information, the monotony of the task became evident. Each website visit, each copied paragraph, each repeated action added up, consuming valuable time that could be better spent analyzing and interpreting the gathered data.
This repetitive challenge served as a catalyst for change. I envisioned a more efficient and streamlined approach, one where automation could liberate me from the shackles of monotony and empower me to focus on the essence of my blog post: providing valuable insights into the intersection of AI and healthcare. I yearned for a more efficient way to gather insights into how healthcare organizations are utilizing AI. The solution? Automation.
The repetitive nature of content gathering ignited the spark. I envisioned a world where automation could liberate me from the mundane, allowing more time for thoughtful analysis and interpretation of the gathered data. And thus, the journey to automate web scraping and content aggregation began.

## Week 1: Setting the Scene - Introduction and Python Environment Setup

Roll up your sleeves and get ready for the first step: setting up the Python environment.

# Crafting Your Python Oasis
## 1. Installing Python:
Head over to the official Python website and get the latest version compatible with your operating system. Follow the installation wizard to download python.

## 2. Pip - The Gateway to Python Libraries:
 Open your terminal or command prompt and run:

```
pip --version
```

## 3. Virtual Environments:
To keep things tidy, we'll use virtual environments. Run these commands:

```
python -m venv venv
```

Activate your virtual environment:

On Windows: venv\Scripts\activate
On macOS/Linux: source venv/bin/activate
Now, your terminal prompt should don a virtual environment cape.

## 4. Library Installation:
Install the necessary libraries with:
```
pip install requests
```
#Import necessary libraries
```
import requests
```

#Function to make an HTTP request to a website
```
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

# Example Usage
make_request(example_website)
```

In this script, we're making our first steps into automation. The function make_request takes a URL, makes an HTTP request using requests.get, and prints the content of the HTTP response. 

Replace website_url with your chosen URL, run the script, and ta-da! You've just made your inaugural automated HTTP request.

## Wrapping Up Week 1
Week 1 has been a blast. We've covered why automation is a game-changer, and you've equipped yourself with a Python environment and your first automation script.As you run the script, don't hesitate to contribute your thoughts and ideas. Found a better way to handle errors? Discovered an optimization? Let's discuss it! Drop your comments on the repository or reach out via stevensjoke4@gmail.com. This blog is our collaborative playground, and your input is invaluable. Next week, join me for the nitty-gritty of web scraping. We'll unravel HTML mysteries and acquaint ourselves with the mighty BeautifulSoup library.

Until then, happy coding! 



# Week 2: Unraveling HTML Mysteries with a Dash of Trial and Error
Hey there fellow coding adventurers! Onajokeoghene Piomoki Stevens back with you for Week 2 of our coding journey!!!

The Quest for Web Scraping Wisdom Continues
🚀 The Magic of BeautifulSoup
Before we jump into the code, let's take a moment to appreciate the magic of BeautifulSoup. It's like a wand that transforms the chaos of HTML into a playground where Python can frolic and gather information effortlessly. But, as we'll soon find out, even magic comes with its own set of rules.

💻 Code Exploration - Web Scraping Basics (Take Two!)
Our journey kicks off with a familiar script, or so we thought:

#Week 2: Web Scraping Basics (with a sprinkle of trial and error)
```
import requests
from bs4 import BeautifulSoup
```

#Function to scrape titles from a website
```
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

# Example Usage
scrape_titles(example_website)
```

Now, with our BeautifulSoup magic in place, let's see what HTML treasures we can uncover.

## 🛠️ Learning from Errors
## ✨ Handling HTML Elements That Play Hard to Get
As we progress, we realize that not all websites are created equal. Some HTML elements might be a bit elusive.


#Function to scrape titles with improved error handling
```
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


# Example Usage
scrape_titles_with_error_check(example_website)
```

Now, our script can handle the unpredictability of HTML elements with grace.

## 🕵️ Extracting Detailed Information
## 🕵️ Extracting Detailed Information
In my journey of web scraping, I've progressed beyond merely fetching random HTML headers. Now, I'm focusing on extracting detailed information, specifically targeting articles from websites. For this project, I've chosen the [PubMed website](https://pubmed.ncbi.nlm.nih.gov) as my source. PubMed is a free search engine that primarily accesses the MEDLINE database, offering a wealth of references and abstracts on life sciences and biomedical topics.

#PLEASE NOTE: Website structures, or the Document Object Model (DOM), can significantly differ from one site to another. This project of mine is tailored specifically for the DOM structure of the PubMed website, which is notably a common and popular format. However, keep in mind that adapting to different website structures may require additional modifications.

#Function to scrape detailed information from a website
```
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


# Example Usage
base_url = "https://pubmed.ncbi.nlm.nih.gov"    # The base URL for PubMed cancer search results
search_query = "/?term=cancer&page=2"           # The specific search query with pagination
full_url = base_url + search_query              # Full URL for the page we want to scrape

scrape_titles_advanced(full_url)
```

Learning Moment:
Web scraping is not just about titles. Let's dive deeper and extract more details, turning HTML into a rich source of information.

## 🌐 Navigating the Maze of Web Scraping
As we navigate through the maze of web scraping, it's essential to understand the intricacies of HTML documents. Each page is a unique puzzle waiting to be solved.

## 🧭 Scraping Through Multiple Pages
Our web scraping adventure expands as we modify our script to scrape titles from a series of pages.


#Function to scrape titles from multiple pages
```
def scrape_titles_multiple_pages(base_url, start_page, num_pages):
    for page_num in range(start_page, start_page + num_pages):
        page_url = f"{base_url}&page={page_num}"
        print("------ ARTICLE PAGE")
        scrape_titles_advanced(page_url)


# Example usage
base_website_url = "https://pubmed.ncbi.nlm.nih.gov/?term=cancer"
start_page_number = 1  # Start scraping from page 1
number_of_pages = 3  # Scrape 3 pages in total

scrape_titles_multiple_pages(base_website_url, start_page_number, number_of_pages)
```

Learning Moment:
HTML puzzles come in many pieces. Let's adapt our script to handle the complexity of multiple pages.

## ✨ Conclusion: The Journey Continues
Week 2 has been an adventure filled with mistakes, fixes, and the joy of discovery. HTML, like any good mystery, keeps us on our toes. As we continue our coding journey, remember, every error is a lesson, and every fix is a step toward mastery.

Join me next week for Week 3, where we'll face the challenges of AJAX-based pages, conquer dynamic content, and maybe even tackle a captcha or two. Until then, happy coding, fellow learners!




# Week 3: Navigating the Maze of Advanced Web Scraping
Hey fellow learners! Onajokeoghene Piomoki Stevens here, back for Week 3 of our coding escapade. If you've been following along, you know we're not just scraping the web; we're diving deep, making mistakes, and learning some advanced techniques. This week, brace yourselves as we unravel the complexities of AJAX-based pages, wrestle with dynamic content, and yes, face off against the notorious captchas.

The Learning Curve Continues
🚀 Embracing Advanced Techniques
As we delve into advanced web scraping, it's like stepping into a new realm. AJAX-based pages, dynamic content, and captchas—these are the challenges that separate the novice from the adept. But remember, we're here to learn, make mistakes, and come out stronger on the other side.

💻 Code Exploration - Tackling AJAX-Based Pages
Our code journey starts with AJAX-based pages. You know, those pages that love to load content asynchronously, throwing a wrench into our scraping plans.

# Week 3: Learning from AJAX Challenges
In this automation project, I leverage Selenium and BeautifulSoup to scrape real-time weather data from AccuWeather, a prime example of a website with dynamically updated content. Weather data, due to its inherently fluctuating nature, is updated frequently, making it an ideal candidate for practicing web scraping on sites with AJAX-based, dynamic content.

The script initiates a Selenium WebDriver to interact with the AccuWeather website, ensuring accurate simulation of a user's browsing experience. This is crucial for accessing content that is loaded dynamically through JavaScript. The WebDriver waits for specific elements to appear, indicating that the AJAX content has been loaded.

Once the dynamic content is loaded, BeautifulSoup is employed to parse the HTML of the page. The script specifically targets elements that represent nearby weather locations, extracting both their names and corresponding URLs. This demonstration of extracting specific data points from a dynamically changing webpage showcases the powerful combination of Selenium for web interaction and BeautifulSoup for HTML parsing.

```
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup
```

#Declare variable to hold website with AJAX data  
```
ajax_url = 'https://www.accuweather.com'
```

#Function to scrape titles from an AJAX-based page
```
def scrape_ajax_page_selenium(url):
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

# Example Usage
scrape_ajax_page_selenium(ajax_url)
```

Learning Moment:
Dynamic content is like a surprise party—you need to wait for it. We use Selenium to be patient and let the dynamic content shine before we scrape.

By implementing this script, users can gain insights into handling modern web pages that rely heavily on JavaScript for content rendering, a common challenge in web scraping endeavors.

#PLEASE NOTE: This code is tailored to match the DOM (Document Object Model) structure of the AccuWeather website, and thus might require modifications to suit other websites. The effectiveness of web scraping scripts is highly dependent on the specific HTML structure and dynamic content loading behaviors of the target website. Therefore, it is crucial to first understand the structure and behavior of the website intended to be scraped before automating its scraping process. This understanding will guide the selection of appropriate elements to target and the necessary wait conditions in Selenium, ensuring successful data extraction.

## 🎭 Navigating the Circus of Captchas
And then, there are captchas—a real circus in the world of web scraping. But, like any circus act, there's a trick to it.

#Function to scrape titles while facing the challenge of captchas
```
def scrape_with_captcha_handling(url):
    try:
        # Uh-oh, a wild captcha appears!
        raise Exception("Captcha Challenge")

    except Exception as e:
        print(f"Captcha encountered. Handling with a solution: {e}")

        # An example of captcha handling (in a perfect world with user intervention)
        user_response = input("Please solve the captcha and press Enter to continue.")
        if user_response:
            scrape_ajax_page_dynamic(url)
```

Learning Moment:
Captcha—our arch-nemesis. In an ideal world, we'd need human intervention. But hey, we're learning the ropes of handling the unexpected.

## ✨ Reflecting on the Journey
Week 3 has been a rollercoaster of learning and adapting. From AJAX challenges to dancing with dynamic content and facing off against captchas, we've grown as web scrapers. It's not just about the code; it's about the journey—making mistakes, learning from them, and evolving our script as we encounter new challenges.

Join me next week for the grand finale—Week 4, where we'll optimize our web scraping script, ensure scalability, and explore ways to maintain ethical and responsible web scraping practices.

Until then, keep coding, keep exploring, and remember—mistakes are just stepping stones on the path to mastery!


# Week 4: The Grand Finale - Scaling Up and Ethical Scraping Practices
Hello fellow coding comrades! Onajokeoghene Piomoki Stevens back with you for the grand finale, Week 4 of our web scraping adventure. We've come a long way, faced errors, conquered HTML mysteries, and now it's time to level up our script. In this ultimate week, we'll explore how to optimize our web scraping script, ensure scalability, and delve into the realm of ethical and responsible scraping practices.

## The Climax of Our Coding Journey
🚀 Optimizing for Success
As we embark on the final leg of our journey, optimization becomes key. We want our script to be swift, efficient, and ready for whatever the web throws at it.

💻 Code Exploration - Scaling Up the Script
Our journey begins with scaling up our script to handle larger datasets and more complex scenarios.


### Week 4: Scaling Up the Script (with a dash of optimization)
import requests
from bs4 import BeautifulSoup

#Function to scrape titles from multiple pages
```
def scrape_titles_multiple_pages(base_url, start_page, num_pages):
    for page_num in range(start_page, start_page + num_pages):
        page_url = f"{base_url}&page={page_num}"
        print("------ ARTICLE PAGE")
        scrape_titles_advanced(page_url)
```

Learning Moment:
Optimization doesn't mean just speed; it means making our script versatile enough to handle various scenarios. Now, we're not just scraping titles; we're diving into details, page after page.

🔄 Avoiding the Pitfalls of Over-Scraping
While we're eager to gather information, it's crucial to avoid over-scraping and putting unnecessary strain on websites. Let's introduce a delay:

#Adding a delay between requests
```
def scrape_titles_multiple_pages(base_url, start_page, num_pages):
    for page_num in range(start_page, start_page + num_pages):
        page_url = f"{base_url}&page={page_num}"
        print("------ ARTICLE PAGE")
        scrape_titles_advanced(page_url)
        time.sleep(1)   # Adding a 1-second delay between requests
```
Learning Moment:
We're not just coders; we're responsible web citizens. In the updated scrape_titles_multiple_pages function code, adding a delay shows respect for the websites we interact with.

🌐 Ethical Scraping Practices
As our script becomes more powerful, we must also be mindful of ethical considerations. We're not here to overwhelm or harm; we're here to learn and gather information responsibly.

🚦 Respecting Robots.txt

#Checking for the presence of robots.txt before scraping
```
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

# Example Usage
# check_robots_txt('https://example.com')    # No robots.txt file Found
check_robots_txt('https://cnn.com')        # Has a robots.txt file
```

Learning Moment:
Before we scrape, let's be good guests. Checking robots.txt is like knocking on the door before entering—it's polite and respects the rules set by the website.

⚖️ Understanding Website Policies and Terms of Service

#Checking website policies and terms of service
```
# Function for checking website policies and terms of service
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

# Helper Function that searches for links containing specified keywords
def find_link_by_keywords(soup, keywords):
    for keyword in keywords:
        link = soup.find('a', text=lambda text: text and keyword in text.lower())
        if link:
            return link['href']
    return None

# Example Usage
check_website_policies('https://cnn.com')
```

Learning Moment:
Let's be informed users. Checking website policies and terms of service ensures we understand the rules of engagement.

✨ Conclusion: A Journey Well-Traveled
And there you have it, fellow learners! Week 4, the grand finale of our web scraping adventure. We've optimized our script, embraced ethical practices, and learned the importance of responsibility in the world of web scraping.

As you continue your coding journey, remember that each line of code is a step toward mastery. Keep exploring, keep learning, and most importantly, code with respect for the digital world.

Until our paths cross again, happy coding!

