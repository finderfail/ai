# Хранение паролей — часть 1

Пароли никогда не хранят в открытом виде и не шифруют обратимо — их хешируют медленным алгоритмом с солью.

Подходящие алгоритмы: **argon2id** (предпочтительно), **bcrypt**, **scrypt**, **PBKDF2**.

Непригодны: MD5, SHA-1, SHA-256 без растяжения — они слишком быстрые и перебираются миллиардами вариантов в секунду.

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
