csv = """Вася;39\nПетя;26\nВасилий Петрович;9\nКостя;26\nЛена;28\nМаша;19"""


def read_data(data: str) -> list:
	return [{'name': line.split(';')[0], 'age': int(line.split(';')[1])} for line in data.split('\n')]


def sorting(lst: list) -> list:
	return sorted(lst, key=lambda x: x.get('age'))


def filter(lst: list, param: int) -> list:
	return [line for line in lst if line.get('age') > param]
