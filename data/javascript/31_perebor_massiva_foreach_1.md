# Перебор массива: forEach и циклы — часть 1

`forEach` вызывает функцию для каждого элемента массива. Ничего не возвращает.

```javascript
const users = ['Аня', 'Борис', 'Вера'];

users.forEach((name) => {
  console.log(name);
});

users.forEach((name, index, array) => {
  console.log(`${index + 1} из ${array.length}: ${name}`);
});
```

Колбэк получает три аргумента: элемент, индекс и сам массив.

## Внутри forEach нельзя писать break

`break` и `continue` внутри `forEach` — синтаксическая ошибка, код не запустится. `return` внутри колбэка лишь завершает текущую итерацию, но не прерывает перебор. Такой код неверен:

```javascript
users.forEach((name) => {
  if (name === 'Борис') break;
});
```

## for...of — когда нужен break

Если требуется досрочный выход, используйте `for...of` — вот правильный вариант:

```javascript
for (const name of users) {
  if (name === 'Борис') break;
  console.log(name);
}

for (const [index, name] of users.entries()) {
  console.log(index, name);
}
```
