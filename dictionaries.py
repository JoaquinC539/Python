
# band = {
#     "vocals": "Plants",
#     "guitar": "Page"
# }
# band2 = dict(vocals="Plant", guitar="Page")
# print(band)
# print(band2)
# print(type(band2))
# print(len(band))

# print(band["vocals"])
# print(band.get("guitar"))

# print(band.keys())
# print(band.values())

# print(band.items())
# print("guitar" in band)
# print("triangke" in band)

# band["vocals"] = "Coverdale"
# band.update({"bass": "JPJ"})
# print(band)

# print(band.pop("bass"))
# print(band)
# print(band.popitem())
# print(band)

# band["drums"] = "Bonham"
# del band["drums"]
# print(band)

# band2.clear()
# print(band2)

# Nested dictionaries

member1 = {
    "name": "Plant",
    "instrument": "vocals"

}
member2 = {
    "name": "Page",
    "instrument": "guitar"
}

band = {
    "member1": member1,
    "member2": member2
}
print(band)
print(band["member1"]["name"])

nums = {1, 2, 3, 4}
nums2 = set((1, 2, 3, 4))
print(nums)
print(nums2)
print(type(nums2))
print(len(nums))

nums = {1, 2, 2, 3}

print(nums)

print(2 in nums)
