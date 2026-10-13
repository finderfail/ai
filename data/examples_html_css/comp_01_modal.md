# Пример HTML/CSS: модальное окно на dialog

Модалка с затемнением на нативном dialog.

```html
<button onclick="modal.showModal()">Open</button>
<dialog id="modal" class="modal">
  <h2>Delete project?</h2><p>This action cannot be undone.</p>
  <form method="dialog"><button value="cancel">Cancel</button><button value="ok">Delete</button></form>
</dialog>
```

```css
.modal { width: min(90vw, 420px); padding: 24px; border: 0; border-radius: 20px; box-shadow: 0 20px 60px rgb(0 0 0 / .25); }
.modal::backdrop { background: rgb(15 23 42 / .5); backdrop-filter: blur(2px); }
.modal form { display: flex; justify-content: flex-end; gap: 8px; margin-top: 16px; }
```
