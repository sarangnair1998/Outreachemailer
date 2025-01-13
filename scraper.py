import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin

def get_plaintext_content(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')

    for element in soup(['style', 'script', 'link']):
        element.decompose()

    content = soup.get_text(separator='\n', strip=True)

    links = soup.find_all('a', href=True)
    for link in links:
        link_url = urljoin(url, link['href'])
        try:
            link_response = requests.get(link_url)
            link_soup = BeautifulSoup(link_response.content, 'html.parser')
            for element in link_soup(['style', 'script', 'link']):
                element.decompose()
            content += '\n' + link_soup.get_text(separator='\n', strip=True)
        except requests.RequestException:
            continue

    return content

# url = input('Enter the URL: ')
# content = get_plaintext_content(url)
