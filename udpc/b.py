votes = list(input())
result = {'U': 0, 'D': 0, 'P': 0, 'C': 0}

for letter in votes:
    if letter in 'UC':
        result['U'] += 1
        result['C'] += 1
    else:
        result['D'] += 1
        result['P'] += 1


a, b, c, d = result['U'], result['D'], result['P'], result['C']
k = max(a, b, c)

for key in result.keys():
    if key == 'C':
        continue
    if result[key] == k:
        print(key, end = "")