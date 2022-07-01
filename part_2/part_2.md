Я изучил следующую работу: https://github.com/0tchenash/HT_21.git

В целом, она написана достаточно чисто, было лишь несколько "запахов")).
Вот что бы я поменял:

1. Файл `classes/storage.py`

По идее, это наш абстрактный класс, т.е. в нем мы определяем поля и методы, которые обязательно
должны быть в дочерних классах. С этим он прекрасно справляется, но вся логика перенесена в файл
`classes/parent_class.py`. Я бы описал всю логику именно в абстрактном классе. В таком случае у 
нас не было бы необходимости создавать ступень в цепочке наследований.
Здесь есть все признаки ленивого класса. Однако, в силу отсутствия опыта работы с абстрактными 
классами, хотелось бы узнать, как они используются на практике, допускается ли в них определять
полноценные методы, а не ограничиваться лишь их перечислением? В своей работе, по крайней мере,
я сделал именно так.

2. Файл `classes/store.py`

Данный класс является, по сути, классом-посредником, т.к. он не выполняет никаких функций, а поля
в нем точно такие же, как и в родительском классе.

3. Файл `classes/parent_class.py`

а) В строках 12 и 34 можно обойтись более краткой записью.

Было:
`sum(item for item in self._items.values())`

Предлагаю:
`sum(self._items.values())`

б) В строках 13-16 обновляется словарь. В случае отсутствия ключа, мы его создаем, иначе - изменяем
значение. Данное действие поместится в одну строку:

Было:
```
if name not in self._items.keys():
    self._items[name] = amount_added
else:
    self._items[name] += amount_added
```

Предлагаю:
`self._items[name] = self._items.get(name, 0) + amount_added`

4. Файл `main.py`

Формально функция main() подходит под категорию "Длинный метод", т.к. она содержит большое кол-во
строк, но, во-первых, она и так упрощена за счет использования класса Move, а во-вторых, таково 
было условия задания и данная функция не столько выполняет роль функции, как просто является 
упрощением основной программы. Так что в данной работе ее можно не принимать во внимание, но 
сказать об этом я должен))