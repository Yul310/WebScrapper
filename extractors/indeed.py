
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup


options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
driver = webdriver.Chrome("./chromedriver.exe", options=options)




def get_page_count(keyword):
    
    driver.get(f"https://indeed.com/jobs?q={keyword}")

    soup=BeautifulSoup(driver.page_source, 'html.parser')
    # pagination = soup.find("nav", role="navigation")
    pagination = soup.find("nav", {"aria-label":"pagination"})
    if pagination == None:
        return 1
    pages = pagination.find_all("div", recursive = False)
    count = len(pages)
    if count >=5:
        print(5)
        return 5
    else:
        print(count)
        return count

    print("pagenumber",len(pages))

# get_page_count("react")



def extract_indeed_jobs(keyword):
    pages = get_page_count(keyword)
    print(pages,"pages")
    results = []

   

    for page in range(pages):
        print(page,"page")
        final_url = f'https://indeed.com/jobs?q={keyword}&start={page*10}'
        
        driver.get(final_url)
        print("finalurl",final_url)

        if final_url == None:
            print("can't request the page")
        else:

            soup = BeautifulSoup(driver.page_source, 'html.parser')
            job_list = soup.find('ul', class_='jobsearch-ResultsList')
            jobs = job_list.find_all('li', recursive=False)

            # print(jobs)

            for job in jobs:
                zone = job.find('div', class_='mosaic-zone')
                # print("zone",zone)
                if zone == None:
                    anchor = job.select_one("h2 a")
                    title = anchor['aria-label']
                    link = anchor['href']
                    company = job.find("span", class_="companyName")
                    location = job.find("div", class_="companyLocation")
                    job_data = {
                        'link':f"https://indeed.com{link}",
                        'company':company.string,
                        'position': title,
                        'location': location.string,
                      

                    }
                    # print("jobdata",job_data)
                    results.append(job_data)

    return results

    for result in results:
            print("result",result)

# job = extract_indeed_jobs("python")
# print(len(job))

