import requests
url = 'https://api.github.com/users/wangrongsheng/repos'
r = requests.get(url)

# 打印出状态码
print('status code',r.status_code)
# status code 200 转态码 200表示成功

response_dict = r.json()
#  打印
print(response_dict)

