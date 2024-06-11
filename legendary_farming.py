items = {"shards": 0, "fragments": 0, "motes": 0}
obtained_item = ""
junk = {}

while obtained_item == "":
    data = input().split()
    for index in range(0, len(data), 2):
        material = data[index + 1].lower()
        quantity = int(data[index])

        if material == "shards":
            items["shards"] += quantity
            if items["shards"] >= 250:
                obtained_item = "Shadowmourne"
                break
        elif material == "fragments":
            items["fragments"] += quantity
            if items["fragments"] >= 250:
                obtained_item = "Valanyr"
                break
        elif material == "motes":
            items["motes"] += quantity
            if items["motes"] >= 250:
                obtained_item = "Dragonwrath"
                break
        else:
            if material in junk:
                junk[material] += quantity
            else:
                junk[material] = quantity

if obtained_item == "Shadowmourne":
    items["shards"] -= 250
elif obtained_item == "Valanyr":
    items["fragments"] -= 250
elif obtained_item == "Dragonwrath":
    items["motes"] -= 250

print(f"{obtained_item} obtained!")
sorted_items = sorted(items.items(), key=lambda kvp: (-kvp[1], kvp[0]))
for key, value in sorted_items:
    print(f"{key}: {value}")
sorted_junk = sorted(junk.items(), key=lambda kvp: kvp[0])
for key, value in sorted_junk:
    print(f"{key}: {value}")
