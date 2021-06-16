word = input()
new = ""
for w in word:
  if w.islower():
    new+=w.upper()
  else:
    new+=w.lower()

print(new)
