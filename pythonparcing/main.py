# import requests

# headers = {
#     'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.84 Safari/537.36',
# }

# response = requests.get(url='http://httpbin.org/user-agent', headers=headers)
# print(response.text)

import requests

response = requests.get(url='https://vk.com/video-22756633_456239776', stream=True)
with open('crash.mp4', 'wb') as file:
    file.write(response.content)