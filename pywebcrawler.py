import requests
import re
import urllib.parse as ulp

def request(url):
    try:
        return requests.get("https://" +url)
    except requests.exceptions.ConnectionError:
        print("error")
        pass

target_url = "https://www.facebook.com"
target_links = []

def extract_links_from(url):
    response = requests.get(target_url)
    print(response)
    return re.findall('(?:href=")(.*?)"',response.content.decode('ISO-8859-1'))

def crawl(url):
    href_links = extract_links_from(url)
    for link in href_links:
        link = ulp.urljoin(target_url,link)

        if "#" in link:
            link = link.split("#")[0]
        if target_url in link and link not in target_links:
            target_links.append(link)
            print(link)
            crawl(link)


crawl(target_url)