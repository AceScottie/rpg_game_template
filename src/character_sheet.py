import random

class stats(object):
	strength = 0
	intelegence = 0
	wisdom = 0
	speed = 0

	def __init__(self, **kwargs):
		self.__dict__.update(**kwargs)

	def set(self, attr, value):
		self.__setattr__(attr, value)






class item(object):
	name = ""
	value = 0
	weight = 0.0
	def __init__(self, name='', value=0, weight=0.0):
		self.name = name
		self.value = value
		self.weignt = weight


class weapon(item):
	def __init__(self, name='', value=0, weight=0.0):
		super().__init__(name=name, value=value, weight=weight)
		self.space = 1 ##the amount of hands to cary
		self.base_damage = 0
		self.range_damage = 0
		self.damage_type = ""
		self.crit_chace = 0
		self.crit_mult = 0

	def set(self, attr, value):
		setattr(self, attr, value)

	def _is_crit(self)->bool:
		return random.randint() > self.crit_chace

	def damage(self):
		if self._is_crit():
			return self.base_damage*self.crit_mult
		else:
			return random.randint(self.base_damage-self.range_damage, self.base_damage+self.range_damage)

class sword(weapon):
	def __init__(self, **kwargs):
		assert 'name' in kwargs.keys() and 'value' in kwargs.keys() and 'weight' in kwargs.keys()
		super().__init__(kwargs.pop('name', ''), kwargs.pop('value', ''), kwargs.pop('weight', ''))
		self.__dict__.update(**kwargs)
		self.damage_type = "slash"

class bow(weapon):
	def __init__(self, **kwargs):
		assert 'name' in kwargs.keys() and 'value' in kwargs.keys() and 'weight' in kwargs.keys()
		super().__init__(self, kwargs.pop('name', ''), kwargs.pop('value', ''), kwargs.pop('weight', ''))
		self.__dict__.update(**kwargs)
		self.damage_type = "pierce"

class dagger(weapon):
	def __init__(self, **kwargs):
		assert 'name' in kwargs.keys() and 'value' in kwargs.keys() and 'weight' in kwargs.keys()
		super().__init__(self, kwargs.pop('name', ''), kwargs.pop('value', ''), kwargs.pop('weight', ''))
		self.__dict__.update(**kwargs)
		self.damage_type = "stab"

class inventory:
	def __init__(self):
		self.slot =[[None]*10 for i in range(5)]

	def _get_free_slot(self):
		for i in range(len(self.slot)):
			return i, self.slot[i].index(None)
		return -1, -1
	def add_item(self, initem):
		if not isinstance(initem, item):
			print("is not an item")
			return
		slotx, sloty = self._get_free_slot()
		print(f"adding item {initem.name} to {slotx}, {sloty}")
		self.slot[slotx][sloty] = initem

	def _get_weight(self):
		w = 0
		for row in self.slot:
			for name, item in row.items():
				w += item.weslotst
	@property
	def slots(self):
		return self.slot

	def __str__(self):
		out = []
		for row in self.slot:
			for i in row:
				if isinstance(i, item):
					x = {'name':i.name, 'value':i.value, 'weight':i.weignt}
				else:
					x = {'name':'', 'value':0, 'weight':0}
				out.append(x)
		return ',\n'.join([str(_) for _ in out])

	


class hand:
	left = None
	right = None

	def equipt(self, at, value):
		if not isinstance(value, weapon):
			raise
		else:
			setattr(self, at, value)

class equiptment:
	def __init__(self):
		self.head = item(name='', value=0, weight=0)
		self.body = item(name='', value=0, weight=0)
		self.legs = item(name='', value=0, weight=0)
		self.hands = hand()

	def weight(self):
		return self.head.weight + self.body.weight + self.legs.weight

	def equipt(self, weapon, hand):
		try:
			self.hands.equipt(hand, weapon)
		except:
			print("That cannot go into your hand")

	def __str__(self):
		out = []
		i = [self.head, self.body, self.legs, self.hands.left, self.hands.right]
		for eq in i:
			if isinstance(eq, item) or isinstance(eq, weapon):
				x = {'name':eq.name, 'value':eq.value, 'weight':eq.weignt}
			else:
				x = {'name':'', 'value':0, 'weight':0}
			out.append(x)
		return ',\n'.join([str(_) for _ in out])

class character:
	age = 0
	name = ""

	def __init__(self, age:int, name:str, base_stats:stats):
		self.base_stats = stats
		self.stats = stats()

		self.statuses = {'poisened':False, 'encumbered':False}

		self.inventory = inventory()
		self.equiptment = equiptment()

	def carry_capacity(self):
		return self.strength*10

	def is_encumbered(self):
		if self.carry_capacity - (self.inventory.weight+self.equipt.weight):
			self.statuses['encumbered'] = True
			self.stats.speed = self.base_stats.speed/2
		else:
			self.stats.speed = self.base_stats.speed