import requests
import os
import re

LEETCODE_API = "https://leetcode.cn/graphql/"
DAILY_QUERY = """\n    query CalendarTaskSchedule($days: Int!) {\n  calendarTaskSchedule(days: $days) {\n    contests {\n      id\n      name\n      slug\n      progress\n      link\n      premiumOnly\n    }\n    dailyQuestions {\n      id\n      name\n      slug\n      progress\n      link\n      premiumOnly\n    }\n    studyPlans {\n      id\n      name\n      slug\n      progress\n      link\n      premiumOnly\n    }\n  }\n}\n"""
# DAILY_QUERY = "\n query CalendarTaskSchedule($days: Int!) {\n calendarTaskSchedule(days: $days) {\n contests {\n id\n name\n slug\n progress\n link\n premiumOnly\n }\n dailyQuestions {\n id\n name\n slug\n progress\n link\n premiumOnly\n }\n studyPlans {\n id\n name\n slug\n progress\n link\n premiumOnly\n }\n }\n}\n ","variables"
# print(type(DAILY_QUERY))
# 获取每日一题信息
response = requests.post(LEETCODE_API, json={"query": DAILY_QUERY,"variables":{"days":0},"operationName":"CalendarTaskSchedule"})
data = response.json()["data"]["calendarTaskSchedule"]["dailyQuestions"][0]
title = data["slug"]
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
