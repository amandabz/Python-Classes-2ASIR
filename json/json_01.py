import json

x = '{"name":"John", "city":"New York", "age": 30}'

y = json.loads(x)

print(y["city"])

