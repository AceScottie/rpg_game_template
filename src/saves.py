import os, pickle

if os.path.isfile("saves.sav"):
	with open("saves.sav", "rb") as f:
		bob = pickle.loads(f.read())
else:
	print("cant open save")

print("checking inv")
print(bob.inventory)
print("checking equiptment")
print(bob.equiptment)