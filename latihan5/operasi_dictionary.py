profile = {
    "id": 2,
    "name": "mario",
    "hobbies": ("playing with luigi", "saving the mushroom kingdom"),
    "is_female": False,
}

print("id:", profile["id"])
print("name:", profile.get("name"))

profile["name"] = "luigi"
print("name:", profile["name"])

profile = {
    "name": "mario",
}

print("len:", len(profile), "data:", profile)

profile["favourite_color"] = "red"
print("len:", len(profile), "data:", profile)

profile.update({"race": "italian"})
print("len:", len(profile), "data:", profile)