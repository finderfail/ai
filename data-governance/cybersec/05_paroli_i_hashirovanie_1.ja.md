# パスワードの保存 — その1

パスワードは平文で保存したり、復号できる形で暗号化したりしてはいけません。ソルト付きの低速なアルゴリズムでハッシュ化します。

適したアルゴリズム：**argon2id**（推奨）、**bcrypt**、**scrypt**、**PBKDF2**。

不適切：MD5、SHA-1、ストレッチングなしの SHA-256。速すぎて、毎秒数十億通りを総当たりされます。

```python
import hashlib
import secrets

salt = secrets.token_hex(16)
password_hash = hashlib.scrypt(
    password.encode("utf-8"),
    salt=bytes.fromhex(salt),
    n=2**14, r=8, p=1, dklen=32,
).hex()
```
