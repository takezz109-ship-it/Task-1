#student name: mumandamdam frank randy
#department: software engineering
#matricule number: 520225

places=["ukraine, egypt, tanziana, zimbabwe"]
print("original list")
print(places) 
print("\Alphabetical order:")
print(sorted(places)) 
print("\nStill original list:")
print(places) 
print("\nReverse alphabetical order:")
print(sorted(places, reverse=True))
print("\nStill original list:")
print(places)

places.reverse()
print("\nList after reverse();")
print(places) 

places.reverse()
print("\nList after reverse() again")
print(places)

places.sort()
print("\nPermanently sorted alphabetically")
print(places)

places.sort(reverse=True)
print("\npermannently sorted in reverse alphabetical order :")
print(places)