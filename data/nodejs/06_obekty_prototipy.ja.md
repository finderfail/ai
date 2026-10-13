# JavaScript：オブジェクト、プロトタイプ、クラス

```javascript
const user = { name: 'Aiko', greet() { return `こんにちは、${this.name}`; } };
const copy = { ...user, name: 'Yui' };
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
  constructor(name) { super(name, 'ワン'); }
}
```

- JS の継承は **プロトタイプ** 型：オブジェクトはプロトタイプへの参照を持ち、ないプロパティはそこで探される。`class` はプロトタイプの上の便利な構文。
- `#フィールド` は本物のプライベートフィールド。
- スプレッド `{ ...obj }` は **浅い** コピー。深いコピーは `structuredClone`。
- `Object.freeze` は変更を禁止する（これも浅い）。
- プロパティの確認：`Object.hasOwn(obj, 'key')`、オプショナルチェーン：`obj?.a?.b`、既定値：`x ?? 'default'`。
