profile = {
    "id": 2,
    "name": "mario",
    "is_female": False,
}

profile.pop("id")
print(profile)

profile = {
    "id": 2,
    "name": "mario",
    "is_female": False,
}

del profile["id"]
print(profile)