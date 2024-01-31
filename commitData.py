import json
from collections import Counter
import matplotlib.pyplot as plt
from datetime import datetime
from collections import defaultdict


# 数据处理

def commit_counts(data):
    authors = [commit['commit']['author']['name'] for commit in data]
    # 使用Counter来统计每个作者的提交次数
    counts = Counter(authors)
    # 绘制统计表
    plt.bar(counts.keys(), counts.values())
    plt.xlabel('Author')
    plt.ylabel('Number of Commits')
    plt.title('Commit Counts by Author')
    plt.show()


def commit_trend(data):
    date_commit_counts = defaultdict(int)
    for commit in data:
        commit_date = commit['commit']['author']['date']
        date_obj = datetime.fromisoformat(commit_date)
        simple_date = date_obj.date()
        date_commit_counts[simple_date] += 1
    sorted_dates = sorted(date_commit_counts.keys())
    # 准备绘图数据
    dates = []
    counts = []
    for date in sorted_dates:
        dates.append(date)
        counts.append(date_commit_counts[date])
    # 绘制统计表
    plt.plot(dates, counts)
    plt.xlabel('Date')
    plt.ylabel('Number of Commits')
    plt.title('Commit Trend Over Time')
    plt.show()


with open(r'commits.json', 'r', encoding='utf-8') as file:
    commits_data = json.load(file)

commit_counts(commits_data)
commit_trend(commits_data)

