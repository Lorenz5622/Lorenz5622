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
link = data["link"]


content = ""

with open('backup.md', 'r') as f:
    content = f.read()
content = content.replace("[[1]]",title)
content = content.replace("[[2]]",link)
# print(content)
    # f.write(content)
with open('README.md', 'w') as f:
    f.write(content)

os.system("sh ./update_readme.sh")
