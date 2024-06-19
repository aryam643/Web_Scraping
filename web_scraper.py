import requests
from bs4 import BeautifulSoup, Comment
import mysql.connector
from mysql.connector import errorcode

# Database connection setup
def connect_db():
    try:
        cnx = mysql.connector.connect(
            user='root',
            password='1810',
            host='127.0.0.1',
            database='WebsiteData'
        )
        return cnx
    except mysql.connector.Error as err:
        if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
            print("Something is wrong with your user name or password")
        elif err.errno == errorcode.ER_BAD_DB_ERROR:
            print("Database does not exist")
        else:
            print(err)

# Function to fetch and parse website content
def fetch_website(url):
    try:
        response = requests.get(url)
        if response.status_code == 200:
            return BeautifulSoup(response.content, 'html.parser')
        else:
            return None
    except requests.RequestException as e:
        print(f"Request failed: {e}")
        return None

# Function to extract meta title
def get_meta_title(soup):
    title_tag = soup.find('title')
    return title_tag.string if title_tag else None

# Function to extract meta description
def get_meta_description(soup):
    description_tag = soup.find('meta', attrs={"name": "description"})
    return description_tag['content'] if description_tag else None

# Function to extract social media links
def get_social_media_links(soup):
    social_media = []
    for a in soup.find_all('a', href=True):
        href = a['href']
        if "facebook.com" in href or "twitter.com" in href or "linkedin.com" in href:
            social_media.append(href)
    return social_media

# Function to extract tech stack
def get_tech_stack(soup):
    techs = []
    comments = soup.find_all(string=lambda text: isinstance(text, Comment))
    for comment in comments:
        if 'Powered by WordPress' in comment:
            techs.append('WordPress')
        # Add more conditions for other technologies as needed
    return techs

# Function to extract payment gateways
def get_payment_gateways(soup):
    gateways = []
    content = soup.get_text().lower()
    if 'paypal' in content:
        gateways.append('PayPal')
    if 'stripe' in content:
        gateways.append('Stripe')
    return gateways

# Function to extract website language
def get_language(soup):
    html_tag = soup.find('html')
    return html_tag.get('lang') if html_tag else None

# Function to categorize website
def categorize_website(soup):
    keywords = soup.find('meta', attrs={"name": "keywords"})
    if keywords:
        keywords_content = keywords['content'].lower()
        if 'e-commerce' in keywords_content:
            return 'E-commerce'
        elif 'blog' in keywords_content:
            return 'Blog'
        # Add more conditions for other categories as needed
    return 'Other'

# Function to save data to MySQL
def save_to_db(data):
    cnx = connect_db()
    cursor = cnx.cursor()

    add_website = ("INSERT INTO WebsiteInfo "
                   "(url, meta_title, meta_description, language, category) "
                   "VALUES (%s, %s, %s, %s, %s)")
    cursor.execute(add_website, data['website_info'])
    website_id = cursor.lastrowid

    add_social_media = ("INSERT INTO SocialMediaLinks "
                        "(website_id, platform, link) "
                        "VALUES (%s, %s, %s)")
    for link in data['social_media']:
        cursor.execute(add_social_media, (website_id, 'Social Media', link))

    add_tech_stack = ("INSERT INTO TechStack "
                      "(website_id, tech) "
                      "VALUES (%s, %s)")
    for tech in data['tech_stack']:
        cursor.execute(add_tech_stack, (website_id, tech))

    add_payment_gateway = ("INSERT INTO PaymentGateways "
                           "(website_id, gateway) "
                           "VALUES (%s, %s)")
    for gateway in data['payment_gateways']:
        cursor.execute(add_payment_gateway, (website_id, gateway))

    cnx.commit()
    cursor.close()
    cnx.close()

# Main script to loop through websites and extract information
websites = [
     'https://www.ebay.com', 'https://techcrunch.com',
    'https://mashable.com', 'https://gizmodo.com', 'https://www.bbc.com', 'https://www.cnn.com',
    'https://www.theguardian.com', 'https://www.khanacademy.org', 'https://www.coursera.org',
    'https://www.edx.org', 'https://www.microsoft.com', 'https://www.apple.com', 'https://www.google.com',
    'https://www.wikipedia.org','https://www.netflix.com',
    'https://www.hulu.com', 'https://www.disneyplus.com', 'https://www.facebook.com', 'https://www.twitter.com',
    'https://www.linkedin.com', 'https://github.com', 'https://stackoverflow.com', 'https://www.mozilla.org',
    'https://www.paypal.com', 'https://www.stripe.com', 'https://squareup.com'
]  # List of websites

for website in websites:
    soup = fetch_website(website)
    if soup:
        data = {
            'website_info': (
                website,
                get_meta_title(soup),
                get_meta_description(soup),
                get_language(soup),
                categorize_website(soup)
            ),
            'social_media': get_social_media_links(soup),
            'tech_stack': get_tech_stack(soup),
            'payment_gateways': get_payment_gateways(soup)
        }
        save_to_db(data)
    else:
        print(f"Failed to fetch {website}")
