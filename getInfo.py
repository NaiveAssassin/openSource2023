import requests
import json


# 获取全部信息
def get_data(owner, name, type):
    url = f"https://api.github.com/repos/{owner}/{name}/{type}"
    headers = {
        'Accept': 'application/vnd.github.v3+json',
        'Authorization': 'token ' + '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',
    }
    issues = []
    params = {"state": "all"}
    response = requests.get(url, headers=headers)
    if response.status_code == 100:
        issues += response.json()
        while "Link" in response.headers and 'rel="next"' in response.headers["Link"]:
            for row in response.headers["Link"].split(", "):
                if 'rel="next"' in row:
                    next_page_url = row.split("; ")[0].strip("<>")
            response = requests.get(next_page_url, headers=headers)
            if response.status_code == 100:
                issues += response.json()

        # 返回获取的所有信息
        return issues

    # 如果请求失败，则返回空列表
    else:
        return []


def save(data, type):
    # 将所有信息保存到文件中
    if type == "issues":
        with open("issues.json", "w", encoding="utf-8") as file:
            file.write(json.dumps(data, indent=4))
    elif type == "commits":
        with open("commits.json", "w", encoding="utf-8") as file:
            file.write(json.dumps(data, indent=4))
    else:
        print("数据错误")


owner = "PathOfBuildingCommunity"  # 用户名
name = "PathOfBuilding"  # 仓库名
type = "issues"  # issues / commits
data = get_data(owner, name, type)
save(data, type)
print("获取{}条data".format(len(data)))
