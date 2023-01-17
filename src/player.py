import pickle
from character_sheet import stats, character, item, sword, bow, dagger

class potion(item):
	def __init__(self):
		super().__init__(name="Healing Potion", value=5, weight=2)

class god_sword(sword):
	def __init__(self):
		super().__init__(name="The Mighty God Sword", value=100, weight=30)
		self.set('base_damage', 30)
		self.set('range_damage', 5)
		self.set('crit_chace', 10)
		self.set('crit_mult', 3)

class player(character):
	def __init__(self):
		self.stats = stats(strength=10, intelligence=20)
		super().__init__(22, "Bob", self.stats)
		self.god_sword = god_sword()
		self.healing_pot = potion()
		self.equiptment.equipt(self.god_sword, 'left')
		self.inventory.add_item(self.healing_pot)
bob=player()
with open("saves.sav", "wb") as f:
	pickle.dump(bob, f)


