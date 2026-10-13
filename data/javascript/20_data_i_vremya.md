# Дата и время

```javascript
const now = new Date();
const iso = now.toISOString();
const fromIso = new Date('2026-08-20T10:30:00Z');
const timestamp = Date.now();

const formatted = now.toLocaleString('ru-RU', {
  dateStyle: 'short',
  timeStyle: 'short'
});

const tomorrow = new Date(now);
tomorrow.setDate(tomorrow.getDate() + 1);

const diffMs = tomorrow - now;
const diffHours = Math.round(diffMs / 1000 / 60 / 60);
```

Месяцы в `Date` нумеруются с нуля: январь это 0, декабрь это 11. Разность двух дат даёт миллисекунды.

Keywords: date, time, timestamp, iso, format date, javascript, node.js, js.
