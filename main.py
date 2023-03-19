
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup



options = Options()






browser = webdriver.Chrome(options=options)
browser.get('https://www.indeed.com/jobs?q=python&limit=10')
soup = BeautifulSoup(browser.page_source, "html.parser")
job_list = soup.find("ul",class_='jobsearch-ResultsList')
jobs = job_list.find_all('li',recursive=False)

for job in jobs:
    zone = job.find('div', class_="mosic-zone")
    if zone == None:
        print("job li")
    else:
        print("mosaic li")

# print(browser)
# print(browser.page_source)


