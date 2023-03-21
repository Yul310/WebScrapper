
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup


options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
driver = webdriver.Chrome("./chromedriver.exe", options=options)
pageload = driver.get('https://indeed.com/jobs?q=python')

soup=BeautifulSoup(driver.page_source, 'html.parser')
job_list = soup.find('ul', class_='jobsearch-ResultsList')
jobs = job_list.find_all('li', recursive=False)

results = []

for job in jobs:
    zone = job.find('div', class_='mosaic-zone')
    if zone == None:
        anchor = job.select_one("h2 a")
        title = anchor['aria-label']
        link = anchor['href']
        company = job.find("span", class_="companyName")
        location = job.find("div", class_="companyLocation")
        job_data = {
            'company':company.string,
            'position': title,
            'location': location.string,
            'link':f"https://indeed.com{link}"

        }
        results.append(job_data)

for result in results:
    print(result)
        # print(title, link)
        # print("///////\n")


        # h2 = job.find("h2", class_="jobTitle")
        # a = h2.find("a")
       



# options = Options()
# browser = webdriver.Chrome(options=options)
# browser.get('https://www.indeed.com/jobs?q=python&limit=10')
# soup = BeautifulSoup(browser.page_source, "html.parser")
# job_list = soup.find("ul",class_='jobsearch-ResultsList')
# jobs = job_list.find_all('li',recursive=False)

# for job in jobs:
#     zone = job.find('div', class_="mosic-zone")
#     if zone == None:
#         print("job li")
#     else:
#         print("mosaic li")

# print(browser)
# print(browser.page_source)


