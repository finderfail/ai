# Классы

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

Поля с решёткой (`#connections`) приватны и недоступны снаружи класса. `static` создаёт метод самого класса, а не экземпляра.

Keywords: class, constructor, extends, static, private field, javascript, node.js, js.
