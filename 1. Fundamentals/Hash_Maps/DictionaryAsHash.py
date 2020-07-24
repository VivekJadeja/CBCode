name_to_age_map = {}
name_to_age_map["Ann"] = 10
name_to_age_map["Sre"] = 11
name_to_age_map["ger"] = 23

#.keys() returns a list of all the keys in the dictionary
print(name_to_age_map.keys())

#.values() returns a list of all values in the dictionary
print(name_to_age_map.values())

#.items() returns a list tuples with all key value pairs
print(name_to_age_map.items())

#check if a key is in the dictionary within O(1) time
print("Ryan" in name_to_age_map)
print("Ann" in name_to_age_map)

# Check values for a given key in O(1) time
print(name_to_age_map.get("Ryan"))
print(name_to_age_map.get("Ann"))

#Directly accessing a key that does not exist gives an error
name_to_age_map["Ryan"]