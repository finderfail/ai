# JavaScript: объекты, прототипы, классы

```javascript
const user = { name: 'Аня', greet() { return `Привет, ${this.name}`; } };
const copy = { ...user, name: 'Вера' };
const deep = structuredClone({ a: { b: 1 } });

class Animal {
  #sound;
  static count = 0;
  constructor(name, sound) {
    this.name = name;
    this.#sound = sound;
    Animal.count++;
  }
  speak() { return `${this.name}: ${this.#sound}`; }
}

class Dog extends Animal {
  constructor(name) { super(name, 'гав'); }
}
```

- Наследование в JS — **прототипное**: у объекта есть ссылка на прототип, где ищутся отсутствующие свойства. `class` — удобный синтаксис поверх прототипов.
- `#поле` — настоящие приватные поля.
- Spread `{ ...obj }` делает **поверхностную** копию; для глубокой — `structuredClone`.
- `Object.freeze` запрещает изменения (тоже поверхностно).
- Проверка свойства: `Object.hasOwn(obj, 'key')`, опциональная цепочка: `obj?.a?.b`, значение по умолчанию: `x ?? 'default'`.
