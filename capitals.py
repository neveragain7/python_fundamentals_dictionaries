countries = input().split(", ")
capitals = input().split(", ")

atlas = dict(zip(countries, capitals))

for country, capital in atlas.items():
    print(f"{country} -> {capital}")
