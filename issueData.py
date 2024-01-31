import json
import matplotlib.pyplot as plt
from datetime import datetime
from collections import defaultdict


# 数据处理


def issues_trend(data):
    date_issues_counts = defaultdict(int)
    for issues in data:
        issues_date = issues['created_at']
        date_obj = datetime.fromisoformat(issues_date)
        simple_date = date_obj.date()
        date_issues_counts[simple_date] += 1
    sorted_dates = sorted(date_issues_counts.keys())
    # 准备绘图数据
    dates = []
    counts = []
    for date in sorted_dates:
        dates.append(date)
        counts.append(date_issues_counts[date])
    # 绘制统计表
    plt.plot(dates, counts)
    plt.xlabel('Date')
    plt.ylabel('Number of Issues')
    plt.title('Issues Trend Over Time')
    plt.show()


with open(r'issues.json', 'r', encoding='utf-8') as file:
    issues_data = json.load(file)

issues_trend(issues_data)

