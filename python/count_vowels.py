text = 'Python is awesome'

aeiou = 'aeiou'
count = 0
for a in text:
    if a.lower() in aeiou:
        count += 1

print(f"모음 개수: {count}")