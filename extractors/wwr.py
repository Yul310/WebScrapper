from requests import get
from bs4 import BeautifulSoup


def extract_wwr_jobs(keywords):
    base_url = "https://weworkremotely.com/remote-jobs/search?term="
    

    response = get(f"{base_url}{keywords}")

    if response.status_code != 200:
        print("Can't request the website")
    else:
        soup = BeautifulSoup(response.text,"html.parser")
        jobs = soup.find_all('section',class_="jobs")
        results = []
        for job_section in jobs:
            job_posts = job_section.find_all('li')
            job_posts.pop(-1)
            for post in job_posts:
                anchors = post.find_all('a')
                anchor = anchors[1]
                link = anchor['href']
                company, kind, region = anchor.find_all('span', class_="company")
                title = anchor.find('span',class_='title')
                print(company.string,kind.string,region.string,title.string)
                job_data = {
                    'link':f"https://weworkremotely.com{link}",
                    'company':company.string,
                    'location': region.string,
                    'position' : title.string
                }
                results.append(job_data)


        return results
    
        # for result in results:
        #     print(result)
        #     print('//////////////////////')