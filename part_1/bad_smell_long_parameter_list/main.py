# У нас есть какой-то юнит, которому мы в параметры передаем
# - наше игровое поле
# - х координату
# - у координату
# - направление смещения
# - летит ли он
# - крадется ли он
# - скорость
# В этом примере есть сразу несколько запахов плохого кода. Исправьте их
#	(длинный метод, длинный список параметров)


class Unit:
	def __init__(self, field, x_coord, y_coord, move_type):
		self._x = x_coord
		self._y = y_coord
		self._move_type = move_type
		self._field = field
		
	def move(self, direction):
		speed = self._get_speed()
		
		if direction == 'UP':
			self._field.set_unit(x=self._x, y=self._y + speed, unit=self)
		elif direction == 'DOWN':
			self._field.set_unit(x=self._x, y=self._y - speed, unit=self)
		elif direction == 'LEFT':
			self._field.set_unit(x=self._x - speed, y=self._y, unit=self)
		elif direction == 'RIGTH':
			self._field.set_unit(x=self._x + speed, y=self._y, unit=self)

	def _get_speed(self):
		if self._move_type == 'fly':
			return 1.2
		elif self._move_type == 'crawl':
			return 0.5
		else:
			return 1
