# クラス

```javascript
class Server {
  #connections = 0;

  constructor(port) {
    this.port = port;
  }

  static create(port) {
    return new Server(port);
  }

  get connections() {
    return this.#connections;
  }

  open() {
    this.#connections += 1;
    return this;
  }
}

class SecureServer extends Server {
  constructor(port, cert) {
    super(port);
    this.cert = cert;
  }
}
```

`#` 付きのフィールド（`#connections`）はプライベートで、クラスの外からはアクセスできません。`static` はインスタンスではなくクラス自体のメソッドを作ります。

Keywords: class, constructor, extends, static, private field, javascript, node.js, js.
