# 日付と時刻

```javascript
const now = new Date();
const iso = now.toISOString();
const fromIso = new Date('2026-08-20T10:30:00Z');
const timestamp = Date.now();

const formatted = now.toLocaleString('ja-JP', {
  dateStyle: 'short',
  timeStyle: 'short'
});

const tomorrow = new Date(now);
tomorrow.setDate(tomorrow.getDate() + 1);

const diffMs = tomorrow - now;
const diffHours = Math.round(diffMs / 1000 / 60 / 60);
```

`Date` の月は0始まりです：1月が0、12月が11。2つの日付の差はミリ秒になります。

Keywords: date, time, timestamp, iso, format date, javascript, node.js, js.
