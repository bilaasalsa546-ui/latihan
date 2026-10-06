def get_full_name(first_name, last_name=""):
    return f"{first_name} {last_name}".strip()


res = get_full_name("Darion")

print(res)

res = get_full_name("Darion", "Mograine")

print(res)