import requests
from bs4 import BeautifulSoup

file_path = r"issue_title_history.txt"
for i in range(1, 78):
    url = 'https://github.com/alibaba/arthas/issues?page=' + str(i) + '&q=is%3Aissue'

    content = requests.get(url).text
    soup = BeautifulSoup(content)
    all_issue = soup.findAll("a", attrs={
        "class": "Link--primary v-align-middle no-underline h4 js-navigation-open markdown-title"})
    with open(file_path, "a", encoding="utf-8") as file:
        for item in all_issue:
            file.write(str(item.string))
            file.write("\n")
    file.close()