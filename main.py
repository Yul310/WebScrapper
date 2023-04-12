# from extractors.indeed import extract_indeed_jobs
# from extractors.wwr import extract_wwr_jobss
# from file import save_to_file

# keyword = input("What do you want to search for?")


# indeed = extract_indeed_jobs(keyword)
# wwr = extract_wwr_jobs(keyword)
# jobs = indeed + wwr

# save_to_file(keyword, jobs)

from flask import Flask, render_template, request, redirect
from extractors.indeed import extract_indeed_jobs
from extractors.wwr import extract_wwr_jobs


app = Flask("JobScrapper")
db={}

@app.route("/")
def home():
    return render_template("home.html")


@app.route("/search")
def search():
    print(request.args)
    keyword = request.args.get("keyword")
    print("keykey",keyword)

    if keyword == None or keyword == "":
        print("no no keyword")
        return redirect("/")
    else:
        print("yes keyword",keyword)
        if keyword in db:
            jobs = db[keyword]
        else:
            indeed = extract_indeed_jobs(keyword)
            wwr = extract_wwr_jobs(keyword)
            jobs = indeed + wwr
            db[keyword] = jobs
        return render_template("search.html", keyword=keyword, jobs=jobs)


app.run("0.0.0.0")
