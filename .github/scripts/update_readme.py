import requests
import os
import re

LEETCODE_API = "https://leetcode.com/graphql"
DAILY_QUERY = """
query questionOfToday {
  activeDailyCodingChallengeQuestion {
    link
    question {
      title
    }
  }
}
"""

# 获取每日一题信息
response = requests.post(LEETCODE_API, json={"query": DAILY_QUERY})
data = response.json()["data"]["activeDailyCodingChallengeQuestion"]
title = data["question"]["title"]
link = f"https://leetcode.com{data['link']}"

# 更新 README.md
readme_path = os.path.join(os.getcwd(), "README.md")
with open(readme_path, "r") as f:
    content = f.read()

new_content = re.sub(
    r'<!-- LEETCODE_DAILY_START -->.*<!-- LEETCODE_DAILY_END -->',
    f'<!-- LEETCODE_DAILY_START -->\n📖 **Today\'s Question:** [{title}]({link})\n<!-- LEETCODE_DAILY_END -->',
    content,
    flags=re.DOTALL
)

with open(readme_path, "w") as f:
    f.write(new_content)
