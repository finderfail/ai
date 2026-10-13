# Node.js：EventEmitter

Node の多くのオブジェクト（サーバー、ストリーム、プロセス）は `EventEmitter` を継承している。

```javascript
const { EventEmitter, once } = require('node:events');

class Orders extends EventEmitter {
  create(order) {
    this.emit('created', order);
  }
}

const orders = new Orders();
orders.on('created', (order) => console.log('新しい注文', order.id));
orders.once('created', () => console.log('1回だけ実行'));
orders.on('error', (err) => console.error(err));
orders.create({ id: 1 });

const [payload] = await once(orders, 'created');
```

- ハンドラーは登録順に **同期的に** 呼ばれる。
- 購読者のいない `'error'` イベントはプロセスを落とす。`error` は必ず購読する。
- 購読解除：`emitter.off(event, handler)`。メモリリークは `MaxListenersExceededWarning` 警告のよくある原因。
- `events.once()` と `events.on()` で、イベント用の Promise と非同期イテレーターが得られる。
