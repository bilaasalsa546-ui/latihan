text = "hello python"

print("text:", text)
print("length:", len(text))

print(text[0])

for c in text:
    print(c)

for i in range(0, len(text)):
    print(text[i])

print(text[1:5])
print(text[7:])
print(text[:4])