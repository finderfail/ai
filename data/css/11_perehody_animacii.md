# CSS: переходы и анимации

**Переход (transition)** — плавное изменение свойства при смене состояния:
```css
.button {
  background: #7b5cff;
  transition: background-color 0.2s ease, transform 0.2s ease;
}
.button:hover { background: #6440f5; transform: translateY(-2px); }
```

**Анимация (@keyframes)** — проигрывается сама:
```css
@keyframes spin { to { transform: rotate(360deg); } }
.loader { animation: spin 1s linear infinite; }

@keyframes fade-in {
  from { opacity: 0; transform: translateY(8px); }
  to   { opacity: 1; transform: none; }
}
.toast { animation: fade-in 0.3s ease-out both; }
```

- Анимируйте `transform` и `opacity` — их браузер обрабатывает на GPU без перерисовки раскладки. `width`, `top`, `margin` анимировать дороже.
- Уважайте `prefers-reduced-motion`.
- Функции времени: `ease`, `linear`, `ease-in-out`, `cubic-bezier()`, `steps()`.
