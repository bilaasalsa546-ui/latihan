message1 = "hello world"
message2 = message1
message3 = "hello world"

print(f"message1 == message2: {message1 == message2}")
print(f"message1 == message3: {message1 == message3}")
print(f"message2 == message3: {message2 == message3}")

print(f"message1 is message2: {message1 is message2}")
print(f"message1 is message3: {message1 is message3}")
print(f"message2 is message3: {message2 is message3}")