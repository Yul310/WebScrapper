# from extractors.indeed import extract_indeed_jobs
# from extractors.wwr import extract_wwr_jobss
# from file import save_to_file

# keyword = input("What do you want to search for?")



# indeed = extract_indeed_jobs(keyword)
# wwr = extract_wwr_jobs(keyword)
# jobs = indeed + wwr

# save_to_file(keyword, jobs)

from flask import Flask, render_template,request


app = Flask("JobScrapper")

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/search")
def search():
    print(request.args)
    keyword = request.args.get("keyword")
    return render_template("search.html",keyword = keyword)

app.run("0.0.0.0")


