# Map と Set

```javascript
const cache = new Map();
cache.set('key', { value: 1 });
cache.get('key');
cache.has('key');
cache.delete('key');
cache.size;

for (const [key, value] of cache) {
  console.log(key, value);
}

const unique = new Set([1, 2, 2, 3]);
const asArray = [...unique];
const dedupedNames = [...new Set(['a', 'b', 'a'])];
```

普通のオブジェクトと違い、`Map` のキーにはオブジェクトを含め何でも使え、挿入順も保たれます。`Set` は重複の除去に便利です。

Keywords: map, set, cache, unique, deduplicate, javascript, node.js, js.
