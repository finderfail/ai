# Map и Set

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
const dedupedNames = [...new Set(['а', 'б', 'а'])];
```

В отличие от обычного объекта, ключом `Map` может быть что угодно, включая объекты, и порядок вставки сохраняется. `Set` удобен для удаления дубликатов.

Keywords: map, set, cache, unique, deduplicate, javascript, node.js, js.
