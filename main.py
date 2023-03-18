from requests import get
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

driver = webdriver.Chrome()
driver.get('https://kr.indeed.com/jobs?q=python&l=&from=searchOnHP&vjk=89395b6ac5014113')

from bs4 import BeautifulSoup
from extractors.wwr import extract_wwr_jobs

# base_url = 'https://www.indeed.com/jobs?q='
# search_term = "python"
# end_url = "&l=&vjk=d598cdf1dbd6f494"
# test_url = "https://www.indeed.com/jobs?q=python&l=&vjk=d598cdf1dbd6f494"
# response = get(f"{base_url}{search_term}{end_url}")
response = get(f"{test_url}")

if response.status_code != 200:
    print(response)
    print("Can't request page")
else:
    print(response.text)

# jobs = extract_wwr_jobs('python')
# print(jobs)

