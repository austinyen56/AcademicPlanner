from bs4 import BeautifulSoup
import requests
import bleach


def web_parse(class_num):
    dept_name = ""  # Assuming if in the future we include other departments
    if class_num < 100:
        div = "Lower-Division/CSE-"
    else:
        div = "Upper-Division/CSE-"
    class_num_str = str(class_num)
    url = "https://catalog.ucsc.edu/en/2020-2021/General-Catalog/Courses/CSE-Computer-Science-and-Engineering/" + div + class_num_str
    request_result = requests.get(url)
    request_result.raise_for_status()
    html = BeautifulSoup(request_result.text, 'html.parser')
    for a in html.find_all('a'):        # Removing hyperlinks in text
        a.replaceWithChildren()

    cc = str(html.find_all("span")[5].string).replace("CSE ", '')

    gen_descrip = str(html.find_all("p")[1]).replace("/<p>|</p>/", "")
    quarter_offered = str(html.find_all("p")[4].string).split(", ")
    print(gen_descrip)
    #return cc, quarter_offered


web_parse(30)
CLASSES = {
    "cse20": {
        "cc": 20,  # Class code
        "availability": 7,
        "prereqs": [],
        "gen_descrip": "This is a class",
        "difficulty": 4,
        "quarter_offered": ["spring", "summer", "fall", "winter"],
        "syllabus": [{"quiz": 30}, {"midterm": 30}, {"final": 30}],
        "textbook": "url",
        "haslab": False,
        "ta_helpful": 6,
        "class_type": 1,  # Math is 0, programming is 1
        "time_commit": 2,  # 1= slack, 2= some work, 3= extra work
        "ge_satis": ["mf"],
        "pref_prof": ["Larrabee"],
    },
    "cse30": {
        "cc": 30,
        "availability": 7,
        "prereqs": [],
        "difficulty": 4,
        "quarter_offered": ["spring", "summer", "fall", "winter"],
        "syllabus": [{"quiz": 30}, {"midterm": 30}, {"final": 30}],
        "textbook": "url",
        "haslab": False,
        "ta_helpful": 6,
        "class_type": 1,
        "time_commit": 2,
        "ge_satis": ["mf"],
        "pref_prof": ["Larrabee"],
    },
}
#print(CLASSES.get("cse30").get("cc"))
