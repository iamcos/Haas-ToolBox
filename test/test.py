from engine import my_engine


class Monkey:
	def eat(self):
		print("Eating")

class Human(Monkey):
	def talk(self):
		print("talking")


class Car():
	a = 5

	def __init__(self) -> None:
		self._engine = my_engine
		pass

	def ride(self):
		self._engine.tir_tir()
		print("riding")
