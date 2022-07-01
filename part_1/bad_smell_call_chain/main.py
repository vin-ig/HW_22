# Измените класс Person так, чтобы его методы 
# оперировали внутренним состоянием, 
# а не использовали цепочку вызовов объектов


class Person:
	def __init__(self):
		self._room = 42
		self._population = 100500

	@property
	def population(self):
		return self._population

	@property
	def room(self):
		return self._room


# TODO после выполнения задания попробуйте
# сделать экземпляр класса person и вызвать новые методы.

man = Person()
print(man.population)
print(man.room)
