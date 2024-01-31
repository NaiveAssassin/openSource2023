import re
import matplotlib.pyplot as plt
from collections import defaultdict

with open(r'commit_Info.txt', 'r', encoding='utf-8') as file:
    commits_data = file.read()

# 统计提交者数量
author_pattern = r'Author: (.+?) <(.+?)>'
author_matches = re.findall(author_pattern, commits_data)
author_counts = defaultdict(int)
for author, _ in author_matches:
    author_counts[author] += 1
sorted_author_counts = dict(sorted(author_counts.items(), key=lambda item: item[1], reverse=True))
for author, count in sorted_author_counts.items():
    print("{author}: {count} commits")