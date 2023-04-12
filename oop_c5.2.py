import requests
import json

r = requests.get("https://baconipsum.com/api/?type=meat-and-filler")
r = json.loads(r.content)

print(r[0])
# texts = json.loads(r.content)

# print(type(texts))

# for text in texts:
#     print(text[:50], '\n')
