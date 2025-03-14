import requests
import os
import re

LEETCODE_API = "https://leetcode.com/graphql/"

# proxies={
# 'http': 'http://127.0.0.1:7890',
# 'https': 'http://127.0.0.1:7890'
# }

headers = {
	'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/134.0.0.0 Safari/537.36 Edg/134.0.0.0'
} 
query = """

    query questionOfToday {
  activeDailyCodingChallengeQuestion {
    date
    userStatus
    link
    question {
      titleSlug
      title
      translatedTitle
      acRate
      difficulty
      freqBar
      frontendQuestionId: questionFrontendId
      isFavor
      paidOnly: isPaidOnly
      status
      hasVideoSolution
      hasSolution
      topicTags {
        name
        id
        slug
      }
    }
  }
}
    """

# 获取每日一题信息
response = requests.post(LEETCODE_API,json = {"operationName": "questionOfToday","query":query, "variables":{}})
data = response.json()["data"]["activeDailyCodingChallengeQuestion"]
title = data["question"]["title"]
link = "https://leetcode.com"+data["link"]


content = ""

with open('moban.md', 'r') as f:
    content = f.read()
content = content.replace("[[1]]",title)
content = content.replace("[[2]]",link)
# print(content)
    # f.write(content)
with open('README.md', 'w') as f:
    f.write(content)

os.system("sh ./update_readme.sh")
